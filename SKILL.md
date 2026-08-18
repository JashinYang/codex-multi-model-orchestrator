---
name: multi-model-orchestrator
description: Coordinate complex work with multiple available subagent models. Use when a user asks to delegate, parallelize, or select Sol, Terra, Luna, DeepSeek V4 Flash, or DeepSeek V4 Pro for a task, and when independent workstreams benefit from deliberate model routing.
---

# Multi-model orchestration

Plan before delegating. Use subagents only when the user asks for delegation or parallel work, or governing instructions explicitly authorize it.

## Availability gate

1. Read the current collaboration tool's available-model catalog.
2. Use only a model listed there. Never invent a model identifier or claim that an unavailable model was called.
3. Treat model names below as routing preferences, not an entitlement. If a requested model is absent, say so and use a fallback only when the user permits it.
4. Use `fork_turns: "none"` whenever choosing a subagent model explicitly, and give the subagent a self-contained task.

## Stage 0 — rule screen

Do a lightweight rules-only screen before involving Sol:

- **Direct path:** one clear, reversible outcome; one narrow area of change; no material ambiguity; and no consequential external action. Use one suitable agent directly. Do not spend a separate Sol call merely to classify it.
- **Sol decision path:** any uncertainty about scope or coupling; two or more likely workstreams; cross-module work; meaningful rework risk; architecture, security, or irreversible impact. Have Sol make the dispatch decision before other agents begin.

The purpose of the screen is to avoid both avoidable Sol overhead on trivial work and cheap-model misrouting on consequential work.

## Stage 1 — Sol decides execution shape

On the Sol decision path, require a concise decision record: intensity, why the work is coupled or independent, direct-Sol versus batch shape, ownership boundaries, and acceptance evidence. Do not delegate this global decision to Luna, DeepSeek V4 Flash, or another execution agent.

Assess task intensity:

| Intensity | Signals | Default execution shape |
| --- | --- | --- |
| Low | One clear outcome; familiar, reversible, or mechanical work | One agent; do not add coordination overhead |
| Medium | A few files or checks, clear acceptance criteria, and limited coupling | Batch only if at least two outputs are independent |
| High | Cross-module reasoning, uncertain diagnosis, integration, or material rework risk | Sol alone when the work is tightly coupled; otherwise batch independent investigation/implementation, then let Sol integrate |
| Critical | Architecture, security, irreversible impact, or conflicting evidence | Sol owns decisions and final validation; delegate only evidence-gathering or isolated checks |

Run Sol alone when one coherent reasoning trace matters more than parallelism: the task touches the same core files, later choices depend on earlier findings, or splitting would duplicate context. Split into batches only when the workstreams have separate outcomes, low file overlap, and a concrete handoff. Do not split a task merely because it is large.

## Stage 2 — route selected batches

Choose autonomously among models listed in the current catalog. Respect a model named by the user. Do not use a static family preference or infer that a model is cheaper or faster from its name.

| Batch signal | First candidate | Other candidate |
| --- | --- | --- |
| Architecture, hard diagnosis, conflicting evidence, or final integration | Sol | DeepSeek V4 Pro |
| General implementation, code review, or focused research | Terra | DeepSeek V4 Pro or GPT-5.5 |
| Bounded but quality-sensitive task with enough latency budget | Luna at `max` | Terra |
| High-volume extraction, classification, or independent checks | DeepSeek V4 Flash | GPT-5.4 mini |
| Complex coding/reasoning with clear acceptance tests | DeepSeek V4 Pro | Terra or Sol |

Treat the table as a shortlist, not a guarantee. When Luna is available, prefer Luna at `max` for an isolated, quality-sensitive batch with enough latency budget. Choose the candidate that is available and has the lowest evidenced total cost for the required quality and deadline. Use a short benchmark or historical measurements when available; otherwise state the uncertainty and favor the candidate with the safer quality fit.

Treat “DeepSeek V4 Flash” and “DeepSeek V4 Pro” as labels, not model IDs. Read the catalog and use its exact identifier only when it exposes the model.

## Cost and latency gate

1. Before selecting DeepSeek primarily for cost, consult its official pricing page on that day. DeepSeek V4 prices vary by peak/off-peak window and may change.
2. Compare prices only when the billing basis is comparable. Do not compare direct DeepSeek API token prices with a Codex subscription, bundled allowance, or third-party relay price as though they were equivalent.
3. Estimate cost from expected cache-hit input, cache-miss input, and output tokens. Include retry and verification work for agent tasks.
4. Treat speed as unknown unless same-task latency measurements exist in the current environment. A vendor performance claim is not a cross-model latency benchmark.

## Reasoning effort

Use the lowest effort that can reliably satisfy the task, except that Luna defaults to `max` when selected and when the current catalog and session policy permit an explicit override. Do not lower Luna unless the user requests a latency/cost tradeoff.

Start Terra at `medium`, raise it to `high` for complex implementation or investigation, and reserve Sol `xhigh` or `max` for architecture, high-risk decisions, and final integration. For DeepSeek, use its documented thinking mode only if the exposed integration supports it; do not translate ChatGPT reasoning-effort labels into DeepSeek parameters without documentation. Do not claim an effort or thinking mode was applied unless the delegation call accepts it.

## Delegation procedure

1. Apply the Stage 0 rule screen.
2. On the direct path, use one suitable available agent and validate the result.
3. On the Sol decision path, obtain Sol's concise decision record, then choose Sol alone or a batched shape.
4. For a batched shape, identify independent workstreams and shared files. Do not delegate overlapping edits unless one agent owns the merge.
5. Assign each subagent one outcome, scope, constraints, and required evidence; start only independent batches concurrently.
6. Reserve Sol for cross-cutting decisions, conflict resolution, integration, and final validation whenever the task is high or critical.
7. Collect results, inspect changes, resolve conflicts, and run relevant validation before reporting completion.

## Prompt pattern

```text
Use $multi-model-orchestrator. First classify task intensity and decide whether
the task passes the direct-path rule screen. If it does not, have Sol issue a
concise decision record and decide whether Sol should complete the work alone or
whether independent batches justify delegation. For batches, select the best
available model using task fit, needed reasoning, comparable cost, and measured
latency. Use Luna at max when selected. Avoid concurrent edits to the same file.
Summarize the execution-shape decision, each delegation, and final validation.
```

## Guardrails

- Do not delegate merely to create activity; work directly on small changes.
- Do not ask a subagent to make external or destructive changes beyond the user's authorization.
- Do not describe a model as active until the delegation call succeeds.
- If no requested routing model is available, stop before delegation and give the user the available choices.
