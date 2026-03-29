#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import quote


PART_RE = re.compile(r"^#{2,6}\s+\*{0,2}(?:Part|Module)\b", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
PARENS_RE = re.compile(r"\s*[\(\[].*?[\)\]]")
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
MULTISPACE_RE = re.compile(r"\s+")
STOPWORDS = {
    "a",
    "an",
    "and",
    "architecture",
    "basics",
    "chapter",
    "concepts",
    "core",
    "data",
    "development",
    "for",
    "fundamentals",
    "guide",
    "in",
    "introduction",
    "of",
    "system",
    "the",
    "to",
    "with",
}


@dataclass(frozen=True)
class NotebookMatch:
    number: int
    relative_path: str
    title: str
    path_hint: str


@dataclass(frozen=True)
class ParsedChapterLine:
    style: str
    prefix: str
    number: int
    title: str
    existing_link: str | None


def strip_markdown(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return MULTISPACE_RE.sub(" ", text).strip()


def normalize_title(text: str) -> str:
    text = strip_markdown(text)
    text = PARENS_RE.sub("", text)
    text = text.replace("&", " and ")
    text = text.lower()
    text = NON_ALNUM_RE.sub(" ", text)
    return MULTISPACE_RE.sub(" ", text).strip()


def title_tokens(text: str) -> set[str]:
    return {token for token in normalize_title(text).split() if token not in STOPWORDS and len(token) > 2}


def similarity_score(left: str, right: str) -> float:
    normalized_left = normalize_title(left)
    normalized_right = normalize_title(right)
    if not normalized_left or not normalized_right:
        return 0.0
    if normalized_left == normalized_right:
        return 1.0
    ratio = SequenceMatcher(None, normalized_left, normalized_right).ratio()
    left_tokens = title_tokens(left)
    right_tokens = title_tokens(right)
    overlap = len(left_tokens & right_tokens) / max(len(left_tokens | right_tokens), 1)
    contains = 1.0 if normalized_left in normalized_right or normalized_right in normalized_left else 0.0
    return max(ratio, overlap, (ratio + overlap + contains) / 3)


def discover_notebooks(handbook_dir: Path) -> list[NotebookMatch]:
    matches: list[NotebookMatch] = []
    for path in handbook_dir.rglob("*.ipynb"):
        if not path.is_file() or ".ipynb_checkpoints" in path.parts:
            continue
        match = re.match(r"^\s*(\d+)\.\s*(.+)\.ipynb$", path.name)
        if not match:
            continue
        number = int(match.group(1))
        title = match.group(2).replace("_", " ")
        relative_path = path.relative_to(handbook_dir).as_posix()
        path_hint = path.parent.name.replace("_", " ")
        matches.append(
            NotebookMatch(
                number=number,
                relative_path=relative_path,
                title=title,
                path_hint=path_hint,
            )
        )
    matches.sort(key=lambda item: (item.number, item.relative_path))
    return matches


def parse_chapter_line(line: str) -> ParsedChapterLine | None:
    stripped = line.strip()
    patterns = [
        (
            "bold_chapter_link",
            re.compile(r"^\*\*\[Chapter (\d+): (.+?)\]\(([^)]+)\)\*\*\s*$"),
        ),
        (
            "bold_chapter",
            re.compile(r"^\*\*Chapter (\d+): (.+?)\*\*\s*$"),
        ),
        (
            "heading_bold_chapter",
            re.compile(r"^(#{2,6}\s+)\*\*\[Chapter (\d+): (.+?)\]\(([^)]+)\)\*\*\s*$"),
        ),
        (
            "heading_plain_chapter_link",
            re.compile(r"^(#{2,6}\s+)\[Chapter (\d+): (.+?)\]\(([^)]+)\)\s*$"),
        ),
        (
            "heading_bold_chapter",
            re.compile(r"^(#{2,6}\s+)\*\*Chapter (\d+): (.+?)\*\*\s*$"),
        ),
        (
            "heading_plain_chapter",
            re.compile(r"^(#{2,6}\s+)Chapter (\d+): (.+?)\s*$"),
        ),
        (
            "heading_bold_numbered",
            re.compile(r"^(#{2,6}\s+)\*\*\[(\d+)\. (.+?)\]\(([^)]+)\)\*\*\s*$"),
        ),
        (
            "heading_numbered_link",
            re.compile(r"^(#{2,6}\s+)\[(\d+)\. (.+?)\]\(([^)]+)\)\s*$"),
        ),
        (
            "heading_bold_numbered",
            re.compile(r"^(#{2,6}\s+)\*\*(\d+)\. (.+?)\*\*\s*$"),
        ),
        (
            "heading_numbered",
            re.compile(r"^(#{2,6}\s+)(\d+)\. (.+?)\s*$"),
        ),
        (
            "list_bold_link",
            re.compile(r"^(\d+\.\s+)\*\*\[(.+?)\]\(([^)]+)\)\*\*\s*$"),
        ),
        (
            "list_link",
            re.compile(r"^(\d+\.\s+)\[(.+?)\]\(([^)]+)\)\s*$"),
        ),
        (
            "list_bold",
            re.compile(r"^(\d+\.\s+)\*\*(.+?)\*\*\s*$"),
        ),
        (
            "bullet_chapter_link",
            re.compile(r"^([*-]\s+)\[Chapter (\d+): (.+?)\]\(([^)]+)\)\s*$"),
        ),
        (
            "bullet_chapter",
            re.compile(r"^([*-]\s+)Chapter (\d+): (.+?)\s*$"),
        ),
        (
            "bullet_numbered_link",
            re.compile(r"^([*-]\s+)\[(\d+)\. (.+?)\]\(([^)]+)\)\s*$"),
        ),
        (
            "bullet_numbered",
            re.compile(r"^([*-]\s+)(\d+)\. (.+?)\s*$"),
        ),
    ]
    for style, pattern in patterns:
        match = pattern.match(stripped)
        if not match:
            continue
        groups = match.groups()
        if style == "bold_chapter_link":
            number, title, link = groups
            return ParsedChapterLine(style, "", int(number), title, link)
        if style == "bold_chapter":
            number, title = groups
            return ParsedChapterLine(style, "", int(number), title, None)
        if style in {"heading_bold_chapter", "heading_plain_chapter_link"}:
            prefix, number, title, link = groups
            return ParsedChapterLine(style, prefix, int(number), title, link)
        if style == "heading_plain_chapter":
            prefix, number, title = groups
            return ParsedChapterLine(style, prefix, int(number), title, None)
        if style in {"heading_bold_numbered", "heading_numbered_link"}:
            prefix, number, title, link = groups
            return ParsedChapterLine(style, prefix, int(number), title, link)
        if style == "heading_numbered":
            prefix, number, title = groups
            return ParsedChapterLine(style, prefix, int(number), title, None)
        if style in {"list_bold_link", "list_link"}:
            prefix, title, link = groups
            number = int(prefix.split(".", 1)[0])
            return ParsedChapterLine(style, prefix, number, title, link)
        if style == "list_bold":
            prefix, title = groups
            number = int(prefix.split(".", 1)[0])
            return ParsedChapterLine(style, prefix, number, title, None)
        if style in {"bullet_chapter_link", "bullet_numbered_link"}:
            prefix, number, title, link = groups
            return ParsedChapterLine(style, prefix, int(number), title, link)
        if style in {"bullet_chapter", "bullet_numbered"}:
            prefix, number, title = groups
            return ParsedChapterLine(style, prefix, int(number), title, None)
    return None


def render_linked_line(parsed: ParsedChapterLine, relative_path: str) -> str:
    encoded = quote(relative_path, safe="/")
    title = strip_markdown(parsed.title)
    if parsed.style == "heading_bold_chapter":
        return f"{parsed.prefix}**[Chapter {parsed.number}: {title}]({encoded})**"
    if parsed.style == "bold_chapter_link":
        return f"**[Chapter {parsed.number}: {title}]({encoded})**"
    if parsed.style == "bold_chapter":
        return f"**[Chapter {parsed.number}: {title}]({encoded})**"
    if parsed.style == "heading_plain_chapter_link":
        return f"{parsed.prefix}[Chapter {parsed.number}: {title}]({encoded})"
    if parsed.style == "heading_plain_chapter":
        return f"{parsed.prefix}[Chapter {parsed.number}: {title}]({encoded})"
    if parsed.style == "heading_bold_numbered":
        return f"{parsed.prefix}**[{parsed.number}. {title}]({encoded})**"
    if parsed.style in {"heading_numbered_link", "heading_numbered"}:
        return f"{parsed.prefix}[{parsed.number}. {title}]({encoded})"
    if parsed.style == "list_bold_link":
        return f"{parsed.prefix}**[{title}]({encoded})**"
    if parsed.style == "list_link":
        return f"{parsed.prefix}[{title}]({encoded})"
    if parsed.style == "list_bold":
        return f"{parsed.prefix}**[{title}]({encoded})**"
    if parsed.style in {"bullet_chapter_link", "bullet_chapter"}:
        return f"{parsed.prefix}[Chapter {parsed.number}: {title}]({encoded})"
    if parsed.style in {"bullet_numbered_link", "bullet_numbered"}:
        return f"{parsed.prefix}[{parsed.number}. {title}]({encoded})"
    return f"{parsed.prefix}[{title}]({encoded})"


def find_best_notebook(
    notebooks: list[NotebookMatch],
    chapter_number: int,
    chapter_title: str,
    part_hint: str | None,
) -> NotebookMatch | None:
    candidates = [notebook for notebook in notebooks if notebook.number == chapter_number]
    if not candidates:
        return None
    best_match: NotebookMatch | None = None
    best_score = -1.0
    for candidate in candidates:
        score = similarity_score(chapter_title, candidate.title)
        if part_hint:
            score += similarity_score(part_hint, candidate.path_hint) * 0.2
        if score > best_score:
            best_score = score
            best_match = candidate
    return best_match


def update_toc_file(toc_path: Path) -> int:
    handbook_dir = toc_path.parent
    notebooks = discover_notebooks(handbook_dir)
    lines = toc_path.read_text(encoding="utf-8").splitlines()
    updated_lines: list[str] = []
    changes = 0
    current_part: str | None = None

    for line in lines:
        stripped = line.strip()
        if PART_RE.match(stripped):
            current_part = strip_markdown(stripped)
        elif re.match(r"^#{1,6}\s+", stripped):
            current_part = None
        parsed = parse_chapter_line(line)
        if not parsed:
            updated_lines.append(line)
            continue
        if parsed.style.startswith("list_") and current_part is None:
            updated_lines.append(line)
            continue
        notebook = find_best_notebook(notebooks, parsed.number, parsed.title, current_part)
        if not notebook:
            updated_lines.append(line)
            continue
        new_line = render_linked_line(parsed, notebook.relative_path)
        if new_line != stripped:
            changes += 1
        updated_lines.append(new_line)

    toc_path.write_text("\n".join(updated_lines).rstrip() + "\n", encoding="utf-8")
    return changes


def iter_toc_paths(root: Path, targets: list[str] | None) -> list[Path]:
    if targets:
        toc_paths = []
        for target in targets:
            path = (root / target / "TOC.md").resolve()
            if path.exists():
                toc_paths.append(path)
        return toc_paths
    return sorted(path for path in root.glob("*/TOC.md") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate chapter links in handbook TOCs.")
    parser.add_argument(
        "targets",
        nargs="*",
        help="Optional handbook directories. When omitted, every top-level handbook TOC is updated.",
    )
    args = parser.parse_args()

    root = Path.cwd()
    toc_paths = iter_toc_paths(root, args.targets)
    if not toc_paths:
        print("No TOC.md files found.")
        return 1

    total_changes = 0
    for toc_path in toc_paths:
        changes = update_toc_file(toc_path)
        total_changes += changes
        print(f"{toc_path.parent.name}/TOC.md: updated {changes} link(s)")

    print(f"\nUpdated {len(toc_paths)} TOC file(s) with {total_changes} total change(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
