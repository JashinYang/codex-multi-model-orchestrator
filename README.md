# Codex Multi-Model Orchestrator

[![Validate skill](https://github.com/JashinYang/codex-multi-model-orchestrator/actions/workflows/validate.yml/badge.svg)](https://github.com/JashinYang/codex-multi-model-orchestrator/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Codex Skill for deciding when to work directly, when to use a high-capability decision pass, and when to run independent agent batches—then integrating and validating the result.

> This repository contains agent-facing instructions. It is not a standalone CLI, model runtime, hosted service, or permission grant.

## Why this exists

Complex coding and research tasks often fail for predictable reasons: work is split before dependencies are understood, several agents edit the same file, a model is selected by habit, or a result is reported without evidence. This Skill turns those failure modes into an explicit, reviewable workflow:

- screen simple tasks before adding coordination overhead;
- separate plan-only recommendations from authorized execution;
- resolve the current collaboration catalog and use exact model IDs;
- give each batch an owner, bounded paths, permissions, and acceptance checks;
- treat repository, web, tool, and model text as untrusted data;
- account for retry, cost, latency, cancellation, and partial failure; and
- reserve integration and final validation for one accountable owner.

## Quick start

1. Copy the whole Skill folder—`SKILL.md` and `references/`—into a Codex skill directory named `multi-model-orchestrator` (commonly `$CODEX_HOME/skills/multi-model-orchestrator/`; use the configured directory for your environment).
2. Choose a mode explicitly:

   ```text
   Use $multi-model-orchestrator in plan-only mode to recommend a safe route for this task.
   ```

   ```text
   Use $multi-model-orchestrator in execute mode to plan and execute this task.
   ```

3. State the outcome, constraints, files or systems in scope, what internal delegation is authorized, and how success should be verified.

The Skill checks the current catalog at runtime. Labels such as Sol, Terra, Luna, or DeepSeek are routing hints; only exact identifiers exposed by the active catalog may be used. If the catalog or delegation tool is unavailable, the Skill reports the limitation instead of inventing an identifier or silently falling back.

## What it does

| Work signal | Default shape | Responsibility |
| --- | --- | --- |
| One clear, reversible outcome | Direct path | One suitable agent completes and validates the work |
| Uncertain scope, coupling, or rework risk | Decision path | A decision-capable agent records intensity, ownership, shape, and evidence |
| Independent outputs with low file overlap | Bounded batches | Each batch has one outcome, owner, permission scope, and handoff |
| Architecture, security, or irreversible impact | Decision-led integration | One accountable owner controls cross-cutting decisions and final validation |

This Skill governs internal routing only. Network access, credentials, publication, destructive changes, and other external side effects require separate authorization.

## When to use it

Use this Skill for:

- cross-module implementation or refactoring;
- architecture and security decisions;
- difficult diagnosis with conflicting evidence;
- research, implementation, and testing that can proceed independently; or
- high-volume extraction, classification, or quality checks.

For one narrow, reversible change with clear acceptance criteria, the direct path is usually better than adding coordination overhead.

## Worked examples and references

The [`examples/`](examples/) directory shows the expected reasoning shape:

- [Cross-module refactor](examples/cross-module-refactor.md)
- [Security investigation](examples/security-investigation.md)
- [Bulk research and classification](examples/bulk-research.md)

For batched work, read the [execution contract](references/execution-contract.md). For untrusted input or security-sensitive work, read the [security boundary](references/security-boundary.md).

The [`evals/`](evals/) directory contains prompt-level regression cases in [`cases.json`](evals/cases.json). Run `python scripts/validate_eval_cases.py` to validate the case schema locally.

## Installation and usage notes

Keep `SKILL.md` and its `references/` directory together. After installation, invoke `$multi-model-orchestrator` explicitly once to confirm discovery. If your environment does not expose a collaboration catalog or delegation tool, use plan-only or a direct path only after the user permits that fallback.

Do not ask the Skill to perform external or destructive actions beyond the authorization already provided by the user. Batch contracts default to read-only and must name exact paths, permissions, owners, outputs, and acceptance checks.

## Validation and maintenance

Every push or pull request to `main` runs [`.github/workflows/validate.yml`](.github/workflows/validate.yml), which checks the Skill frontmatter, required documentation, and evaluation-case schema. GitHub Actions updates are tracked by [Dependabot](.github/dependabot.yml). Changes to agent behavior should update an example or evaluation case and report final verification evidence.

For contribution expectations, see [`CONTRIBUTING.md`](CONTRIBUTING.md). For vulnerability reports, see [`SECURITY.md`](SECURITY.md).

## Repository layout

```text
SKILL.md                           # Entry-point Skill instructions
references/execution-contract.md  # Batch, permissions, lifecycle, and handoff rules
references/security-boundary.md   # Threat model and default-deny controls
examples/                          # Worked routing examples
evals/cases.json                   # Machine-readable regression cases
evals/README.md                    # Evaluation guidance and metrics
scripts/validate_eval_cases.py     # Deterministic case-schema validator
.github/workflows/validate.yml     # Documentation and behavior-fixture validation
.github/ISSUE_TEMPLATE/            # Structured issue intake
.github/PULL_REQUEST_TEMPLATE/     # Review checklist
SECURITY.md                        # Private vulnerability reporting policy
LICENSE                            # MIT license
```

## License

This project is available under the MIT License. See [LICENSE](LICENSE).
