# Worked example: cross-module refactor

This is an illustrative routing record, not a claim that the Skill should always create parallel work.

## Request

> Move the authentication configuration from three modules into one typed configuration layer. Update callers, tests, and documentation without changing runtime behavior.

## Rule screen

This is not a good direct-path task: it has cross-module coupling, a shared configuration contract, and a meaningful regression risk.

## Execution-shape decision

| Field | Decision |
| --- | --- |
| Intensity | High |
| Shape | Sol decides, then bounded batches |
| Shared owner | One integration owner for the configuration contract |
| File boundary | Each batch owns separate modules; no concurrent edits to the shared contract |
| Acceptance evidence | Tests, type checks, unchanged behavior, and a final diff review |

## Batches

1. Map the existing configuration contract and call sites.
2. Implement the typed configuration layer and migration adapter.
3. Update tests and add regression coverage for old and new paths.
4. Update documentation after the implementation shape is stable.

The integration owner resolves contract changes before merging batch output. A batch that discovers a shared dependency reports it instead of editing another batch's files.

## Validation

- Run the repository's tests and type checks.
- Search for stale configuration names.
- Compare behavior at the old and new entry points.
- Review the final diff for overlapping or accidental edits.

