"""Validate the machine-readable routing evaluation cases."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


VALID_ROUTES = {"direct", "sol", "batch", "stop"}
VALID_AUTHORIZATION = {"none", "internal_delegation", "external_action"}
VALID_REQUESTED_SCOPE = {"external_action", "write", "network", "credentials"}
ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_string_list(value: object, field: str, case_id: str) -> None:
    require(isinstance(value, list) and value, f"{case_id}: {field} must be a non-empty list")
    require(
        all(isinstance(item, str) and item.strip() for item in value),
        f"{case_id}: {field} must contain non-empty strings",
    )


def validate(path: Path) -> int:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"case file is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"case file is not valid JSON: {exc}") from exc

    require(isinstance(data, dict), "top-level value must be an object")
    require(data.get("schema_version") == 1, "schema_version must be 1")
    cases = data.get("cases")
    require(isinstance(cases, list) and cases, "cases must be a non-empty list")

    seen: set[str] = set()
    required_fields = {
        "id",
        "prompt",
        "expected_route",
        "authorization",
        "required_evidence",
        "safety_expectations",
    }

    for index, case in enumerate(cases, start=1):
        require(isinstance(case, dict), f"case {index} must be an object")
        missing = required_fields.difference(case)
        require(not missing, f"case {index} is missing: {', '.join(sorted(missing))}")

        case_id = case["id"]
        require(isinstance(case_id, str) and ID_PATTERN.fullmatch(case_id), f"case {index}: invalid id")
        require(case_id not in seen, f"duplicate case id: {case_id}")
        seen.add(case_id)

        require(isinstance(case["prompt"], str) and case["prompt"].strip(), f"{case_id}: prompt is empty")
        require(case["expected_route"] in VALID_ROUTES, f"{case_id}: invalid expected_route")
        require(case["authorization"] in VALID_AUTHORIZATION, f"{case_id}: invalid authorization")
        if "requested_scope" in case:
            require(case["requested_scope"] in VALID_REQUESTED_SCOPE, f"{case_id}: invalid requested_scope")
        validate_string_list(case["required_evidence"], "required_evidence", case_id)
        validate_string_list(case["safety_expectations"], "safety_expectations", case_id)

    return len(cases)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    default_path = Path(__file__).resolve().parents[1] / "evals" / "cases.json"
    parser.add_argument("path", nargs="?", type=Path, default=default_path)
    args = parser.parse_args()

    try:
        count = validate(args.path)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"Validated {count} routing evaluation cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
