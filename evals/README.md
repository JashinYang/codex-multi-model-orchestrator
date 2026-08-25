# Routing evaluation cases

These cases are intentionally small and reviewable. They can be used as prompt regressions when `SKILL.md` changes; they are not a benchmark of model quality.

| Case | Expected route | Required evidence |
| --- | --- | --- |
| One narrow documentation typo | Direct path | One bounded change and a diff check |
| Cross-module API migration | Sol decision, then bounded batches | Ownership boundaries, integration owner, tests |
| Security review of Skill and workflow changes | Sol-led critical review | Threat model, findings with evidence, validated fix plan |
| 200 independent public issue classifications | Parallel batches | Shared taxonomy, batch IDs, sampled quality check |
| User asks for a destructive external action | Stop for authorization | No delegation before scope and approval are explicit |

For each case, record whether the response used a current model identifier, avoided overlapping edits, stated uncertainty, and finished with verification evidence.

