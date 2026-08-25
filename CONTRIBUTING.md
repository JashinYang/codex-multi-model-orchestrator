# Contributing

Thanks for helping improve `multi-model-orchestrator`.

## Before opening a change

- Read [`SKILL.md`](SKILL.md) and the relevant worked examples.
- Explain the user problem and the expected behavior change.
- Keep changes focused; avoid adding coordination overhead for its own sake.
- Do not include credentials, private prompts, exploit details, or unapproved external actions.

## Skill changes

Changes to `SKILL.md` can affect downstream Agent behavior. A pull request should explain:

1. which decision or guardrail changes;
2. why the current behavior is insufficient;
3. which example or evaluation case covers the change; and
4. how the result was verified.

Do not invent model identifiers. Use only names exposed by the current collaboration catalog at runtime.

## Pull requests

- Use a descriptive title.
- Update README, examples, or the changelog when user-visible behavior changes.
- Run the local validation command below before opening the PR.

```powershell
python -c "from pathlib import Path; import re; s=Path('SKILL.md').read_text(encoding='utf-8'); assert s.startswith('---\n'); end=s.find('\n---\n',4); assert end != -1; f={k.strip():v.strip() for k,v in (line.split(':',1) for line in s[4:end].splitlines() if ':' in line)}; assert re.fullmatch(r'[a-z0-9-]+', f['name']); assert Path('README.md').read_text(encoding='utf-8').strip(); print('validated', f['name'])"
```

The maintainer owns final integration and validation for behavior-changing edits.

