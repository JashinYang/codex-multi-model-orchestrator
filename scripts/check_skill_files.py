"""Validate that Skill files have no encoding corruption and that internal Markdown links resolve.

Fails the build if any tracked text file contains a U+FFFD replacement character
(the signature of a mojibake/encoding regression) or if a relative Markdown link
points to a path that does not exist in the repository.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

TEXT_GLOBS = ("**/*.md", "**/*.json", "**/*.py", "**/*.yml", "**/*.yaml", "**/*.txt")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_RE = re.compile(r"^(https?://|mailto:|#)")


def _skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def check_no_replacement_characters() -> list[str]:
    problems: list[str] = []
    for glob in TEXT_GLOBS:
        for path in REPO_ROOT.glob(glob):
            if _skip(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if "\ufffd" in text:
                count = text.count("\ufffd")
                problems.append(f"{path.relative_to(REPO_ROOT)}: {count} U+FFFD replacement character(s)")
    return problems


def check_markdown_links() -> list[str]:
    problems: list[str] = []
    for path in REPO_ROOT.glob("**/*.md"):
        if _skip(path):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if EXTERNAL_RE.match(target):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                problems.append(f"{path.relative_to(REPO_ROOT)}: broken link -> {target}")
    return problems


def main() -> int:
    problems = check_no_replacement_characters() + check_markdown_links()
    if problems:
        print("Skill file validation failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("Skill files contain no encoding corruption and all internal links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
