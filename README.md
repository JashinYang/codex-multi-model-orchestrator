# Codex Multi-Model Orchestrator

[![Validate skill](https://github.com/JashinYang/codex-multi-model-orchestrator/actions/workflows/validate.yml/badge.svg)](https://github.com/JashinYang/codex-multi-model-orchestrator/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Codex Skill for deciding when to work directly, when to use a high-capability decision pass, and when to run independent agent batches, then integrating and validating the result.

> This repository contains agent-facing instructions. It is not a standalone CLI, model runtime, hosted service, or permission grant.

## Scope

This is a Codex multi-agent orchestration skill, not a general-purpose prompt. It assumes Codex's collaboration catalog, delegation tools, and skill-invocation syntax, and it references the model labels "Sol", "Terra", "Luna", and "DeepSeek" as routing hints.

The routing principles (screen simple tasks, treat untrusted data as data, record decisions, keep one integration owner, do not assume permissions, cost and latency awareness) are portable to any agent. The Codex-specific mechanics live in the "Availability gate" and "Delegation procedure" sections of [`SKILL.md`](SKILL.md).

## What it does

This Skill turns the predictable failure modes of multi-agent work (work split before dependencies are understood, overlapping edits, habit-based model selection, results reported without evidence) into an explicit, reviewable workflow: screen simple tasks, separate plan-only recommendations from authorized execution, resolve exact model IDs, give each batch an owner and acceptance checks, and reserve integration for one accountable owner. The full routing rules live in [`SKILL.md`](SKILL.md).

This Skill governs internal routing only. Network access, credentials, publication, destructive changes, and other external side effects require separate authorization.

## Quick start

1. Copy the whole Skill folder (`SKILL.md` and `references/`) into a Codex skill directory named `multi-model-orchestrator` (commonly `$CODEX_HOME/skills/multi-model-orchestrator/`; use the configured directory for your environment).
2. Choose a mode explicitly:

   ```text
   Use $multi-model-orchestrator in plan-only mode to recommend a safe route for this task.
   ```

   ```text
   Use $multi-model-orchestrator in execute mode to plan and execute this task.
   ```

3. State the outcome, constraints, files or systems in scope, what internal delegation is authorized, and how success should be verified.

The Skill checks the current catalog at runtime. Labels such as Sol, Terra, Luna, or DeepSeek are routing hints; only exact identifiers exposed by the active catalog may be used. If the catalog or delegation tool is unavailable, the Skill reports the limitation instead of inventing an identifier or silently falling back.

## Worked examples and references

The [`examples/`](examples/) directory shows the expected reasoning shape:

- [Cross-module refactor](examples/cross-module-refactor.md)
- [Security investigation](examples/security-investigation.md)
- [Bulk research and classification](examples/bulk-research.md)

For batched work, read the [execution contract](references/execution-contract.md). For untrusted input or security-sensitive work, read the [security boundary](references/security-boundary.md).

The [`evals/`](evals/) directory contains prompt-level regression cases in [`cases.json`](evals/cases.json). Run `python scripts/validate_eval_cases.py` to validate the case schema, or `python scripts/run_behavioral_eval.py` to run the cases through a Codex runtime and check the selected route (see [`evals/README.md`](evals/README.md)).

## Installation and usage notes

Keep `SKILL.md` and its `references/` directory together. After installation, invoke `$multi-model-orchestrator` explicitly once to confirm discovery. If your environment does not expose a collaboration catalog or delegation tool, use plan-only or a direct path only after the user permits that fallback.

Do not ask the Skill to perform external or destructive actions beyond the authorization already provided by the user. Batch contracts default to read-only and must name exact paths, permissions, owners, outputs, and acceptance checks.

## Validation and maintenance

Every push or pull request to `main` runs [`.github/workflows/validate.yml`](.github/workflows/validate.yml), which checks the Skill frontmatter, required documentation, file integrity (no encoding corruption or broken links), and evaluation-case schema. GitHub Actions updates are tracked by [Dependabot](.github/dependabot.yml). Changes to agent behavior should update an example or evaluation case and report final verification evidence.

For contribution expectations, see [`CONTRIBUTING.md`](CONTRIBUTING.md). For vulnerability reports, see [`SECURITY.md`](SECURITY.md).

## Repository layout

```text
SKILL.md                           # Entry-point Skill instructions
references/execution-contract.md  # Batch, permissions, lifecycle, and handoff rules
references/security-boundary.md   # Threat model and default-deny controls
examples/                          # Worked routing examples
evals/cases.json                   # Machine-readable regression cases
evals/README.md                    # Evaluation guidance and metrics
scripts/check_skill_files.py      # Encoding and link integrity check (CI)
scripts/run_behavioral_eval.py    # Behavioral eval harness (local, needs a runtime)
scripts/validate_eval_cases.py    # Deterministic case-schema validator
agents/openai.yaml                # Optional UI metadata
.github/workflows/validate.yml     # Documentation and behavior-fixture validation
.github/ISSUE_TEMPLATE/            # Structured issue intake
.github/PULL_REQUEST_TEMPLATE/     # Review checklist
SECURITY.md                        # Private vulnerability reporting policy
LICENSE                            # MIT license
```

## License

This project is available under the MIT License. See [LICENSE](LICENSE).
