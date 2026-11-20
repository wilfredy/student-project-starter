#!/usr/bin/env python3
"""Validate this repository's skill metadata, inline file links, and routing."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "student-project-starter"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---(?:\n|$)", re.DOTALL)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
# This repository uses inline Markdown links; fenced examples are excluded.
LINK = re.compile(r"\]\(([^()\n]+)\)")


def prose(text: str) -> str:
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, tail = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def main() -> int:
    errors: list[str] = []
    skills = sorted(SKILL.rglob("SKILL.md"))
    markdown = sorted({*ROOT.glob("README*.md"), *ROOT.glob("docs/**/*.md"), *SKILL.rglob("*.md")})
    names: set[str] = set()
    graph: dict[Path, set[Path]] = {p: set() for p in markdown}
    links = 0

    def fail(path: Path, message: str) -> None:
        errors.append(f"{path.relative_to(ROOT)}: {message}")

    if not (SKILL / "SKILL.md").is_file():
        fail(SKILL, "main SKILL.md is missing")

    license_path = SKILL / "LICENSE"
    repository_license = ROOT / "LICENSE"
    if (not license_path.is_file() or not repository_license.is_file()
            or license_path.read_bytes() != repository_license.read_bytes()):
        fail(license_path, "installable skill must carry the repository's license notice")

    for path in skills:
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            fail(path, "missing YAML frontmatter")
            continue
        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            fail(path, f"invalid YAML: {exc}")
            continue
        if not isinstance(metadata, dict):
            fail(path, "frontmatter must be a mapping")
            continue
        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
            fail(path, "name must be 1–64 lowercase letters/digits with single hyphens")
        else:
            if name != path.parent.name:
                fail(path, "name must match its containing folder")
            if name in names:
                fail(path, f"duplicate skill name: {name}")
            names.add(name)
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            fail(path, "description must contain 1–1024 characters")
        elif any(c in description for c in "<>") or description.startswith("[TODO:"):
            fail(path, "description contains invalid markup or an unfinished placeholder")

    for path in markdown:
        for raw in LINK.findall(prose(path.read_text(encoding="utf-8"))):
            target = raw.strip().removeprefix("<").removesuffix(">")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            links += 1
            if not destination.is_relative_to(ROOT):
                fail(path, f"file link escapes the repository: {target}")
            elif not destination.exists():
                fail(path, f"broken file link: {target}")
            else:
                graph[path].add(destination)

    visited: set[Path] = set()
    pending = [SKILL / "SKILL.md"]
    while pending:
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)
        pending.extend(graph.get(current, ()))
    for path in SKILL.rglob("*.md"):
        if path not in visited:
            fail(path, "not reachable from the main skill's file links")

    ui = SKILL / "agents" / "openai.yaml"
    try:
        ui_data = yaml.safe_load(ui.read_text(encoding="utf-8"))
        interface = ui_data.get("interface") if isinstance(ui_data, dict) else None
        if not isinstance(interface, dict):
            fail(ui, "interface must be a mapping")
        else:
            for key in ("display_name", "short_description", "default_prompt"):
                if not isinstance(interface.get(key), str) or not interface[key].strip():
                    fail(ui, f"missing interface.{key}")
            prompt = interface.get("default_prompt")
            if isinstance(prompt, str) and "$student-project-starter" not in prompt:
                fail(ui, "default prompt must invoke the main skill")
    except (OSError, yaml.YAMLError) as exc:
        fail(ui, f"cannot read UI metadata: {exc}")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(skills)} skills, {links} relative file links, reachable instructions, UI metadata, and license.")
    print("External URLs, heading anchors, assistant behavior, and live providers are not tested by this check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
