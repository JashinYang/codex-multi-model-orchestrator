# Security Policy

## Supported versions

The latest version on the default `main` branch is supported. Older revisions may not receive security fixes.

## Reporting a vulnerability

Please use GitHub's private vulnerability reporting for this repository. Do not include exploit details, credentials, tokens, or other sensitive material in a public issue.

If private reporting is unavailable, open a minimal public issue that only asks the maintainer to enable a private channel; do not disclose the vulnerability there.

## Skill-specific concerns

Because `SKILL.md` is loaded as agent-facing instructions, behavior-changing edits deserve the same review care as executable changes. In particular, do not add hidden network destinations, requests to reveal secrets, instructions to bypass approvals, or model identifiers that are not present in the current collaboration catalog.

## Disclosure

Please allow time for the maintainer to investigate and prepare a fix before public disclosure. Do not test against services or data you do not own or have permission to access.

