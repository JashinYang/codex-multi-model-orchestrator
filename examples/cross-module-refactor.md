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
| Authorization | Internal delegation only; no network or publication |
| Permission scope | Read in-scope modules; write only to each batch's assigned paths |
| Acceptance evidence | Tests, type checks, unchanged behavior, and a final diff review |

## Batches

1. `map-contract`: map the existing configuration contract and call sites; read-only; no dependencies.
2. `implement-layer`: implement the typed configuration layer and migration adapter; depends on `map-contract`; owns only implementation paths.
3. `update-tests`: update tests and add regression coverage for old and new paths; depends on `map-contract`; owns test paths.
4. `update-docs`: update documentation after the implementation shape is stable; depends on `implement-layer`; owns documentation paths.

The integration owner resolves contract changes before merging batch output. A batch that discovers a shared dependency reports it instead of editing another batch's files.

If a prerequisite fails, stop dependent batches. Independent, side-effect-free mapping or test work may finish, but the final report must remain partial until the integrated tree passes validation.

## Validation

- Run the repository's tests and type checks.
- Search for stale configuration names.
- Compare behavior at the old and new entry points.
- Review the final diff for overlapping or accidental edits.
