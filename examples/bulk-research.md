# Worked example: bulk research and classification

This is an illustrative routing record for a high-volume task with independent items.

## Request

> Classify 200 public issue reports into duplicate, documentation, bug, security, or needs-more-information, and produce a review queue.

## Execution shape

- Split the items into independent batches with stable IDs.
- Give every batch the same taxonomy, examples, and output schema.
- Give every batch an owner, exact input range, allowed output path, read-only permission scope, and acceptance check.
- Do not let a batch close issues, contact users, or make external changes.
- Reserve a final validation pass for sampling, disagreement review, and duplicate consistency.

If one batch fails, record it as failed and stop only its dependents. Other batches may finish when they are side-effect-free, but the deliverable must identify the missing range and remain partial until the integration owner reviews it.

## Cost and quality controls

- Use the current model catalog rather than hard-coded identifiers.
- Estimate input, output, retry, and verification tokens before selecting a high-volume route.
- Review a fixed sample from every batch.
- Re-run disagreements with the same evidence and record the reason for the final label.
- Record the exact catalog model IDs and mark cost or latency as unknown when comparable evidence is unavailable.

## Deliverable

Return a machine-readable table plus a short queue summary. Report uncertainty instead of forcing a label when the evidence is insufficient.
