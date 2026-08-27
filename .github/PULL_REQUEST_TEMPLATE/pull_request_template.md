## Summary

Describe the user problem and the focused change.

## Behavior and scope

- What decision, guardrail, example, or document changed?
- Does this change affect agent-facing instructions or GitHub Actions?
- Which files are intentionally not changed?

## Validation

- [ ] I ran the local validation command or the GitHub Actions equivalent.
- [ ] I ran `python scripts/validate_eval_cases.py` when evaluation cases or their schema changed.
- [ ] I added or updated an example/evaluation case for behavior changes.
- [ ] I checked that model identifiers come from the current catalog rather than being invented.
- [ ] I checked for overlapping file ownership and accidental external actions.
- [ ] I checked batch permissions, cancellation/retry behavior, and partial-result reporting when applicable.
- [ ] I updated README, examples, or CHANGELOG when user-visible behavior changed.

## Security

- [ ] No credentials, private prompts, exploit details, or unapproved destinations are included.
- [ ] I considered prompt injection, permission changes, network access, secret handling, and third-party workflow/action changes.
