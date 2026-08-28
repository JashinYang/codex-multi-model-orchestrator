"""Behavioral eval: run the routing cases through Codex and check the selected route.

Unlike 'validate_eval_cases.py' (schema only), this harness actually invokes an agent
for each prompt in 'evals/cases.json' and compares the route it selects against the
case's 'expected_route'. It requires an authenticated Codex runtime, so it is a local
tool and is intentionally not part of the default CI path.

Install the Skill first (so '$multi-model-orchestrator' is discoverable), then run:

    python scripts/run_behavioral_eval.py --model gpt-5.4-mini
    python scripts/run_behavioral_eval.py --limit 3

For a deterministic plumbing test that does not call a model, pass '--runner' with a
command that prints a route line, for example:

    python scripts/run_behavioral_eval.py --runner "echo route: sol"
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = REPO_ROOT / "evals" / "cases.json"
ROUTE_RE = re.compile(r"\broute\s*[:=]\s*(direct|sol|batch|stop)\b", re.IGNORECASE)


def load_cases() -> list[dict]:
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    cases = data["cases"]
    if not isinstance(cases, list) or not cases:
        raise ValueError("evals/cases.json must contain a non-empty 'cases' list")
    return cases


def build_prompt(case: dict) -> str:
    return (
        "Invoke the $multi-model-orchestrator skill in plan-only mode for the request below, "
        "then answer with exactly one line of the form "
        "'route: <direct|sol|batch|stop>' and nothing after that line.\n\n"
        f"Request: {case['prompt']}"
    )


def extract_route(text: str) -> str | None:
    match = ROUTE_RE.search(text)
    return match.group(1).lower() if match else None


def run_codex(prompt: str, model: str | None) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "last.txt"
        cmd = [
            "codex", "exec",
            "--ephemeral",
            "--skip-git-repo-check",
            "--sandbox", "read-only",
            "--color", "never",
        ]
        if model:
            cmd += ["-m", model]
        cmd += ["-o", str(out), prompt]
        subprocess.run(cmd, check=True, cwd=REPO_ROOT)
        return out.read_text(encoding="utf-8")


def run_case(case: dict, model: str | None, runner: str | None) -> str:
    prompt = build_prompt(case)
    if runner:
        proc = subprocess.run(
            runner.replace("{prompt}", prompt),
            shell=True,
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        return proc.stdout
    return run_codex(prompt, model)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=None, help="Model passed to 'codex exec' (defaults to the configured model when omitted).")
    parser.add_argument("--limit", type=int, default=None, help="Run only the first N cases.")
    parser.add_argument(
        "--runner",
        default=None,
        help="Override the per-case command (shell string) for plumbing tests; "
             "the placeholder {prompt} is replaced with the built prompt.",
    )
    args = parser.parse_args()

    cases = load_cases()
    if args.limit:
        cases = cases[: args.limit]

    failures: list[tuple[str, str]] = []
    for case in cases:
        try:
            output = run_case(case, args.model, args.runner)
        except Exception as exc:  # noqa: BLE001
            failures.append((case["id"], f"runner error: {exc}"))
            continue
        route = extract_route(output)
        if route != case["expected_route"]:
            failures.append((case["id"], f"expected {case['expected_route']!r}, got {route!r}"))

    total = len(cases)
    passed = total - len(failures)
    print(f"Behavioral eval: {passed}/{total} passed")
    if failures:
        print("Failures:")
        for case_id, message in failures:
            print(f"  - {case_id}: {message}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
