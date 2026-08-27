# Execution contract

Use this reference whenever a task leaves the direct path. The contract makes parallel work bounded, reviewable, and safe to resume. Keep it in the task handoff or decision record; never put credentials, private tokens, or sensitive prompt text in it.

## Decision record

Record the following before dispatch:

```text
route: direct | sol | batch
intensity: low | medium | high | critical
reason: why this route fits the scope, coupling, and risk
authorization: what internal delegation is allowed; what is excluded
catalog_snapshot: time, available exact model IDs, relevant capabilities
integration_owner: one accountable agent/person
acceptance: checks and evidence required before reporting success
```

If the record cannot identify an integration owner or acceptance evidence, do not dispatch a batch.

## Batch contract

Every batch must have a stable, unique `batch_id` and declare:

| Field | Requirement |
| --- | --- |
| `goal` | One outcome that can be reviewed independently |
| `inputs` | Files, findings, or references the batch may read |
| `allowed_paths` | Exact files or directories it may change; default is none |
| `dependencies` | Batch IDs that must succeed first, or `none` |
| `owner` | Agent responsible for the handoff and evidence |
| `model_id` | Exact identifier returned by the current catalog |
| `permissions` | Separate read, write, network, credential, and external-action scope |
| `output` | Stable format, including file changes or a machine-readable result |
| `acceptance` | Checks, tests, or evidence required for this batch |
| `risk_notes` | Uncertainty, assumptions, and possible side effects |

Default permissions are:

```text
read: in-scope task inputs only
write: none
network: none
credentials: none
external_actions: none
```

Grant a permission only for the specific batch that needs it, and never treat a model's request for broader access as authorization. A batch must not modify a path owned by another active batch.

## Lifecycle and partial failure

Use these states: `planned`, `dispatched`, `running`, `blocked`, `succeeded`, `failed`, `cancelled`, and `integrated`.

- Do not mark a batch `succeeded` without its required evidence.
- If a prerequisite fails or is cancelled, stop dependent batches and state the reason.
- Independent batches may finish after a failure only when they are side-effect-free and the integration owner agrees it is useful.
- Retry only with a bounded count, backoff, and an idempotent operation. Never retry an external side effect blindly.
- Propagate cancellation to queued and running work when the user cancels the task.
- A resumed task must use a new attempt identifier or verify the previous attempt's durable state before repeating work.
- Partial results must be reported as partial; do not imply that integration or full validation occurred.

## Handoff and integration

Each handoff should state:

```text
batch_id:
status:
result:
files_changed:
checks_run:
evidence:
assumptions:
unresolved_risks:
next_action:
```

The integration owner inspects every claimed file change, verifies that paths and permissions were respected, resolves conflicts, and runs the relevant checks on the integrated tree. The final report should include the route, exact model IDs and effort actually applied, changed files, checks, cost/latency assumptions, authorized external actions, and remaining uncertainty.
