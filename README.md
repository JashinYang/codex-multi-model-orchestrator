# Codex Multi-Model Orchestrator

A Codex skill for planning and coordinating complex work across multiple AI models.

It screens simple tasks, routes independent work to the best available model, and keeps one agent responsible for integration and final validation.

## What it helps with

- Break complex requests into independent workstreams.
- Choose an execution shape: one agent, a Sol-led workflow, or parallel batches.
- Route architecture, implementation, research, extraction, and validation work by task fit.
- Keep ownership boundaries clear and avoid overlapping edits.
- Account for verification, retry, cost, and latency uncertainty before reporting success.

## When to use it

Use this skill when a task has meaningful coupling or rework risk, such as:

- Cross-module implementation or refactoring
- Architecture and security decisions
- Difficult diagnosis with conflicting evidence
- Research, implementation, and testing that can proceed independently
- High-volume extraction, classification, or quality checks

For one narrow, reversible change with clear acceptance criteria, the direct path is usually better than adding coordination overhead.

## Installation

Copy \`SKILL.md\` into a Codex skill directory named \`multi-model-orchestrator\`.

The repository layout is intentionally minimal:

\`\`\`text
SKILL.md    # Codex skill instructions
README.md   # This overview
LICENSE     # MIT license
\`\`\`

## Usage

Invoke the skill explicitly:

\`\`\`text
Use $multi-model-orchestrator to plan and execute this task.
\`\`\`

Include the desired outcome, constraints, files or systems in scope, and how success should be verified.

## Routing preferences

Model names below are routing preferences, not guarantees. The exact model identifier must come from the current collaboration catalog.

| Work signal | First candidate | Typical responsibility |
| --- | --- | --- |
| Architecture, hard diagnosis, conflicting evidence, or final integration | Sol | Make the execution-shape decision and own cross-cutting validation |
| General implementation, code review, or focused research | Terra | Deliver a bounded implementation or investigation |
| Isolated, quality-sensitive work with enough latency budget | Luna at \`max\` | Produce a focused, high-quality batch |
| High-volume extraction, classification, or independent checks | DeepSeek V4 Flash | Process many independent items |
| Complex coding or reasoning with clear acceptance tests | DeepSeek V4 Pro | Handle difficult, testable implementation work |

\`DeepSeek V4 Flash\` and \`DeepSeek V4 Pro\` are descriptive labels. Use the exact identifier exposed by the current integration rather than inventing one.

## Execution flow

1. **Screen the task.** Use one suitable agent for a clear, reversible outcome. Escalate to Sol when scope, coupling, risk, or rework is uncertain.
2. **Choose the shape.** Sol records the intensity, coupling, ownership boundaries, and acceptance evidence.
3. **Run independent batches.** Delegate only when outputs are genuinely independent and file ownership does not overlap.
4. **Integrate and verify.** Inspect changes, resolve conflicts, run the relevant checks, and report evidence rather than assumptions.

## Cost and latency

Do not infer speed or price from a model name. When DeepSeek is selected primarily for cost, compare the official pricing for that day using a comparable billing basis, and include expected retries and verification work. Treat latency as unknown unless the current environment has same-task measurements.

## Validation

Changes to this repository are checked by \`.github/workflows/validate.yml\`. The workflow verifies that the required files exist and that \`SKILL.md\` contains valid frontmatter with \`name\` and \`description\`.

## License

This project is available under the MIT License. See [LICENSE](LICENSE).

## Example prompt

\`\`\`text
Use $multi-model-orchestrator. First classify task intensity and decide whether
the direct path is sufficient. If not, have Sol choose between a single-agent
workflow and independent batches. Route each batch by task fit, avoid edits to
the same file, and finish with integration and validation evidence.
\`\`\`
