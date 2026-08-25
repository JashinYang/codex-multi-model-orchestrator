# Codex Multi-Model Orchestrator

[![Validate skill](https://github.com/JashinYang/codex-multi-model-orchestrator/actions/workflows/validate.yml/badge.svg)](https://github.com/JashinYang/codex-multi-model-orchestrator/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Codex Skill for deciding when to work directly, when to ask Sol for an execution-shape decision, and when to run independent batches—then integrating and validating the result.

> This repository contains instructions for Codex. It is not a standalone CLI, model runtime, or hosted service.

## Why this exists

Complex coding and research tasks often fail for predictable reasons: the work is split before its dependencies are understood, several agents edit the same file, a model is selected by habit instead of task fit, or a result is reported without evidence of validation.

This Skill turns those failure modes into an explicit workflow:

- screen simple tasks before adding coordination overhead;
- ask Sol to choose the execution shape when scope, coupling, or risk is unclear;
- route independent batches using the current collaboration catalog;
- keep ownership boundaries and shared-file rules visible;
- account for retry, cost, and latency uncertainty; and
- reserve integration and final validation for an accountable agent.

## Quick start

1. Copy `SKILL.md` into a Codex skill directory named `multi-model-orchestrator`.
2. Invoke it explicitly:

   ```text
   Use $multi-model-orchestrator to plan and execute this task.
   ```

3. Include the desired outcome, constraints, files or systems in scope, and how success should be verified.

The Skill checks the current model catalog at runtime. Model names in this repository are routing preferences, not guarantees or static identifiers.

## What it does

| Work signal | Default shape | Responsibility |
| --- | --- | --- |
| One clear, reversible outcome | Direct path | One suitable agent completes and validates the work |
| Uncertain scope, coupling, or rework risk | Sol decision path | Sol records intensity, ownership, shape, and acceptance evidence |
| Independent outputs with low file overlap | Parallel batches | Each batch has one outcome and a concrete handoff |
| Architecture, security, or irreversible impact | Sol-led integration | Sol owns cross-cutting decisions and final validation |

## When to use it

Use this Skill for work such as:

- cross-module implementation or refactoring;
- architecture and security decisions;
- difficult diagnosis with conflicting evidence;
- research, implementation, and testing that can proceed independently; or
- high-volume extraction, classification, or quality checks.

For one narrow, reversible change with clear acceptance criteria, the direct path is usually better than adding coordination overhead.

## Worked examples

The [`examples/`](examples/) directory shows the expected reasoning shape without pretending that every task needs parallelism:

- [Cross-module refactor](examples/cross-module-refactor.md)
- [Security investigation](examples/security-investigation.md)
- [Bulk research and classification](examples/bulk-research.md)

The [`evals/`](evals/) directory contains a small, reviewable set of routing cases for regression checks.

## Installation and usage notes

This repository intentionally stays minimal: `SKILL.md` is the reusable artifact. Keep the user prompt specific about scope and acceptance evidence. Do not ask the Skill to perform external or destructive actions beyond the authorization already provided by the user.

## Validation and maintenance

Every push or pull request to `main` runs [`.github/workflows/validate.yml`](.github/workflows/validate.yml), which checks the Skill frontmatter and required documentation. GitHub Actions updates are tracked by [Dependabot](.github/dependabot.yml).

For contribution expectations, see [`CONTRIBUTING.md`](CONTRIBUTING.md). For vulnerability reports, see [`SECURITY.md`](SECURITY.md).

## Repository layout

```text
SKILL.md                         # Codex Skill instructions
README.md                        # Overview and quick start
examples/                        # Worked routing examples
evals/                           # Reviewable regression cases
.github/workflows/validate.yml   # Documentation and frontmatter validation
.github/ISSUE_TEMPLATE/          # Structured issue intake
.github/PULL_REQUEST_TEMPLATE/   # Review checklist
SECURITY.md                      # Private vulnerability reporting policy
LICENSE                          # MIT license
```

## License

This project is available under the MIT License. See [LICENSE](LICENSE).

