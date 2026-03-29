#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


HANDBOOK_ORDER = [
    "python",
    "django",
    "fastapi",
    "flask",
    "asp_net",
    "csharp",
    "aspire",
    "frontend",
    "typescript",
    "nextjs",
    "flutter",
    "postgres",
    "graphql",
    "ai_engineering",
    "time_series_prediction",
    "share_analysis",
    "dsa",
    "design_patterns",
    "system_design",
    "networking",
    "ci_cd",
    "cloud_computing",
    "cybersecurity",
    "software_testing",
    "blockchain",
    "project_management",
]


REWRITE_WAVES = {
    "wave1": ["ai_engineering", "system_design", "time_series_prediction", "django", "ci_cd", "blockchain"],
    "wave2": ["cloud_computing", "cybersecurity", "networking", "nextjs", "flutter", "design_patterns"],
    "wave3": ["python", "frontend", "typescript", "fastapi", "flask", "asp_net", "csharp", "aspire", "postgres", "graphql"],
    "wave4": ["dsa", "software_testing", "share_analysis", "project_management"],
}

PRE_WAVE_NORMALIZATION = ["ai_engineering", "system_design", "flutter", "django", "ci_cd"]

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
PART_RE = re.compile(r"^#{2,6}\s+\*{0,2}(?:Part|Module)\b", re.IGNORECASE)
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
MULTISPACE_RE = re.compile(r"\s+")
PARENS_RE = re.compile(r"\s*[\(\[].*?[\)\]]")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "basics",
    "chapter",
    "concepts",
    "core",
    "data",
    "development",
    "for",
    "fundamentals",
    "guide",
    "how",
    "in",
    "introduction",
    "is",
    "of",
    "overview",
    "part",
    "the",
    "to",
    "using",
    "what",
    "with",
    "your",
}

BANNED_META_PATTERNS = [
    re.compile(r"^\s*Here is\b", re.IGNORECASE),
    re.compile(r"\bthe complete first chapter of your\b", re.IGNORECASE),
    re.compile(r"\bthe complete .* workbook\b", re.IGNORECASE),
    re.compile(r"\bworkbook guidelines\b", re.IGNORECASE),
    re.compile(r"\bwithout full spoonfed code\b", re.IGNORECASE),
    re.compile(r"\bnot spoonfeeding(?: full code)?\b", re.IGNORECASE),
    re.compile(r"\brewritten with full explanations\b", re.IGNORECASE),
    re.compile(r"\bcomprehensive workbook chapter\b", re.IGNORECASE),
]

PROMOTIONAL_PATTERNS = [
    (re.compile(r"\s*[—-]\s*Rewritten With Full Explanations\b", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*Comprehensive Workbook Chapter\b", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*Industry Standard\b", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*The Right Way\b", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*Like a Pro\b", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*Done Right\b", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*Practical\b", re.IGNORECASE), ""),
    (re.compile(r"\s*\((?:[^)]*(?:Crash Course|Industry Standard|The Right Way|Like a Pro|Done Right)[^)]*)\)", re.IGNORECASE), ""),
]

TOC_META_SECTION_HEADINGS = {
    "preface",
    "pedagogical features throughout the book",
    "table of contents",
    "workbook structure and pedagogy",
    "workbook structure pedagogy",
}


@dataclass(frozen=True)
class NotebookRecord:
    handbook: str
    path: Path
    relative_path: str
    chapter_number: int


@dataclass(frozen=True)
class TocChapter:
    number: int
    title: str
    link: str | None
    line_index: int
    subtopics: list[str]
    part_title: str | None


@dataclass
class HandbookAudit:
    handbook: str
    toc_chapter_count: int
    notebook_count: int
    toc_chapter_count_excluding_appendix: int
    notebook_count_excluding_appendix: int
    intro_issues_in_toc: bool
    notebook_intro_issues: list[str] = field(default_factory=list)
    malformed_directories: list[str] = field(default_factory=list)
    missing_toc_links: list[str] = field(default_factory=list)
    broken_toc_links: list[str] = field(default_factory=list)
    orphan_notebooks: list[str] = field(default_factory=list)
    unmatched_toc_chapters: list[str] = field(default_factory=list)
    likely_missing_subtopics: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class CleanupSummary:
    handbook: str
    toc_changed: bool = False
    notebooks_changed: int = 0


def source_to_text(source: object) -> str:
    if isinstance(source, str):
        return source
    if isinstance(source, list):
        return "".join(source)
    return ""


def text_to_source(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def numeric_prefix(value: str) -> int:
    match = re.match(r"^\s*(\d+)", value)
    return int(match.group(1)) if match else sys.maxsize


def strip_markdown(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return MULTISPACE_RE.sub(" ", text).strip()


def normalize_text(text: str) -> str:
    text = strip_markdown(text)
    text = PARENS_RE.sub("", text)
    text = text.replace("&", " and ")
    text = text.lower()
    text = NON_ALNUM_RE.sub(" ", text)
    return MULTISPACE_RE.sub(" ", text).strip()


def title_tokens(text: str) -> set[str]:
    return {token for token in normalize_text(text).split() if token not in STOPWORDS and len(token) > 2}


def similarity(left: str, right: str) -> float:
    normalized_left = normalize_text(left)
    normalized_right = normalize_text(right)
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


def has_banned_meta(text: str) -> bool:
    return any(pattern.search(text) for pattern in BANNED_META_PATTERNS)


def sanitize_promotional_text(text: str) -> str:
    cleaned = text
    for pattern, replacement in PROMOTIONAL_PATTERNS:
        cleaned = pattern.sub(replacement, cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    cleaned = re.sub(r"\s+([)\]])", r"\1", cleaned)
    cleaned = re.sub(r"([(\[])\s+", r"\1", cleaned)
    cleaned = re.sub(r"\s+[—-]\s*$", "", cleaned)
    return cleaned.strip()


def sanitize_heading_line(line: str) -> str:
    if not re.match(r"^\s*#{1,6}\s+", line):
        return sanitize_promotional_text(line.rstrip())
    prefix, title = line.split(" ", 1)
    title = sanitize_promotional_text(title.rstrip())
    return f"{prefix} {title}".rstrip()


def fallback_handbook_title(handbook: str) -> str:
    replacements = {
        "ai_engineering": "AI Engineering Handbook",
        "asp_net": "ASP.NET Handbook",
        "ci_cd": "CI/CD Handbook",
        "dsa": "Data Structures and Algorithms Handbook",
    }
    if handbook in replacements:
        return replacements[handbook]
    return f"{handbook.replace('_', ' ').title()} Handbook"


def sanitize_toc_title_line(line: str, handbook: str) -> str:
    if not re.match(r"^\s*#{1,6}\s+", line):
        return sanitize_promotional_text(line.rstrip())
    prefix, title = line.split(" ", 1)
    title_text = strip_markdown(title.rstrip())
    title_text = re.sub(r":\s*Complete Guide to\s+", ": ", title_text, flags=re.IGNORECASE)
    title_text = re.sub(r":\s*(?:The Complete Guide|From .+)$", "", title_text, flags=re.IGNORECASE)
    title_text = re.sub(r"\bthe complete\b", "", title_text, flags=re.IGNORECASE)
    title_text = re.sub(r"\bmastery workbook\b", "Handbook", title_text, flags=re.IGNORECASE)
    title_text = re.sub(r"\bworkbook\b", "Handbook", title_text, flags=re.IGNORECASE)
    title_text = re.sub(r"\s{2,}", " ", title_text).strip(" :-")
    if not title_text:
        title_text = fallback_handbook_title(handbook)
    return f"{prefix} {title_text}".rstrip()


def collapse_blank_lines(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip("\n"))
    return f"{text}\n" if text else ""


def clean_notebook_intro_text(text: str) -> tuple[str, bool]:
    original = text
    lines = text.splitlines()
    first_heading_index = next((index for index, line in enumerate(lines) if re.match(r"^\s*#{1,6}\s+", line)), None)
    if first_heading_index is not None:
        leading = "\n".join(lines[:first_heading_index]).strip()
        if leading and has_banned_meta(leading):
            lines = lines[first_heading_index:]

    cleaned_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if has_banned_meta(stripped):
            continue
        if re.match(r"^\s*#{1,6}\s+", line):
            line = sanitize_heading_line(line)
            stripped = line.strip()
            if has_banned_meta(stripped):
                continue
        if stripped == "---" and not cleaned_lines:
            continue
        if not stripped and (not cleaned_lines or not cleaned_lines[-1].strip()):
            continue
        cleaned_lines.append(line.rstrip())

    cleaned = collapse_blank_lines("\n".join(cleaned_lines))
    return cleaned, cleaned != original


def parse_toc_chapter_line(line: str) -> tuple[int, str, str | None] | None:
    stripped = line.strip()
    patterns = [
        re.compile(r"^\*\*\[Chapter (\d+): (.+?)\]\(([^)]+)\)\*\*\s*$"),
        re.compile(r"^\*\*Chapter (\d+): (.+?)\*\*\s*$"),
        re.compile(r"^#{2,6}\s+\*\*\[Chapter (\d+): (.+?)\]\(([^)]+)\)\*\*\s*$"),
        re.compile(r"^#{2,6}\s+\[Chapter (\d+): (.+?)\]\(([^)]+)\)\s*$"),
        re.compile(r"^#{2,6}\s+\*\*Chapter (\d+): (.+?)\*\*\s*$"),
        re.compile(r"^#{2,6}\s+Chapter (\d+): (.+?)\s*$"),
        re.compile(r"^#{2,6}\s+\*\*\[(\d+)\. (.+?)\]\(([^)]+)\)\*\*\s*$"),
        re.compile(r"^#{2,6}\s+\[(\d+)\. (.+?)\]\(([^)]+)\)\s*$"),
        re.compile(r"^#{2,6}\s+\*\*(\d+)\. (.+?)\*\*\s*$"),
        re.compile(r"^#{2,6}\s+(\d+)\. (.+?)\s*$"),
        re.compile(r"^(\d+)\.\s+\*\*\[(.+?)\]\(([^)]+)\)\*\*\s*$"),
        re.compile(r"^(\d+)\.\s+\[(.+?)\]\(([^)]+)\)\s*$"),
        re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*\s*$"),
    ]
    for pattern in patterns:
        match = pattern.match(stripped)
        if not match:
            continue
        groups = match.groups()
        if len(groups) == 3:
            number, title, link = groups
            return int(number), strip_markdown(title), link
        number, title = groups
        return int(number), strip_markdown(title), None
    return None


def is_meta_toc_section_heading(line: str) -> bool:
    stripped = line.strip()
    if not re.match(r"^#{1,6}\s+", stripped):
        return False
    heading = normalize_text(HEADING_RE.match(stripped).group(1)) if HEADING_RE.match(stripped) else ""
    return heading in TOC_META_SECTION_HEADINGS


def is_duration_or_tagline(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    lowered = normalize_text(stripped)
    if "duration" in lowered and "level" in lowered:
        return True
    if lowered.startswith("from zero to") or lowered.startswith("from novice to"):
        return True
    if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**") and not stripped.endswith("**") and "chapter" not in lowered and "part" not in lowered:
        return True
    return False


def clean_toc_text(text: str, handbook: str) -> tuple[str, bool]:
    original = text
    lines = text.splitlines()
    cleaned_lines: list[str] = []
    seen_title = False
    in_meta_section = False
    structure_started = False

    for line in lines:
        stripped = line.strip()

        if not seen_title:
            if not stripped or stripped == "---" or has_banned_meta(stripped) or is_duration_or_tagline(stripped):
                continue
            if re.match(r"^#{1,6}\s+", stripped):
                cleaned_lines.append(sanitize_toc_title_line(line, handbook))
                seen_title = True
            continue

        if is_meta_toc_section_heading(line):
            in_meta_section = True
            continue

        if in_meta_section:
            if PART_RE.match(stripped):
                in_meta_section = False
            elif re.match(r"^#{1,6}\s+", stripped):
                in_meta_section = False
            else:
                continue

        chapter_match = parse_toc_chapter_line(line)
        if PART_RE.match(stripped) or chapter_match:
            in_meta_section = False
        if has_banned_meta(stripped) or is_duration_or_tagline(stripped):
            continue
        if stripped.lower() == "## table of contents":
            continue
        if stripped == "---":
            if not structure_started:
                continue
            if cleaned_lines and cleaned_lines[-1] == "---":
                continue
            cleaned_lines.append("---")
            continue
        if PART_RE.match(stripped):
            structure_started = True
            cleaned_lines.append(sanitize_heading_line(line))
            continue
        if chapter_match:
            structure_started = True
            cleaned_lines.append(sanitize_promotional_text(line.rstrip()))
            continue
        if structure_started:
            if not stripped and (not cleaned_lines or not cleaned_lines[-1].strip()):
                continue
            cleaned_lines.append(line.rstrip())

    cleaned = collapse_blank_lines("\n".join(cleaned_lines))
    first_nonempty = next((line for line in cleaned.splitlines() if line.strip()), "")
    if not first_nonempty or PART_RE.match(first_nonempty) or parse_toc_chapter_line(first_nonempty) or first_nonempty.startswith("##"):
        cleaned = collapse_blank_lines(f"# {fallback_handbook_title(handbook)}\n\n{cleaned}")
    return cleaned, cleaned != original


def is_handbook_dir(path: Path) -> bool:
    return path.is_dir() and (path / "TOC.md").exists()


def ordered_handbooks(root: Path, selected: list[str] | None) -> list[str]:
    if selected:
        return [name for name in selected if is_handbook_dir(root / name)]
    available = {path.name for path in root.iterdir() if is_handbook_dir(path)}
    ordered = [name for name in HANDBOOK_ORDER if name in available]
    ordered.extend(sorted(available - set(ordered)))
    return ordered


def discover_notebooks(root: Path, handbook: str) -> list[NotebookRecord]:
    handbook_dir = root / handbook
    notebooks = []
    for path in handbook_dir.rglob("*.ipynb"):
        if not path.is_file() or ".ipynb_checkpoints" in path.parts:
            continue
        notebooks.append(
            NotebookRecord(
                handbook=handbook,
                path=path,
                relative_path=path.relative_to(root).as_posix(),
                chapter_number=numeric_prefix(path.name),
            )
        )
    notebooks.sort(key=lambda item: (item.chapter_number, item.relative_path))
    return notebooks


def load_notebook(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def first_markdown_text(notebook: dict) -> str:
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            return source_to_text(cell.get("source"))
    return ""


def notebook_headings(notebook: dict) -> list[str]:
    headings: list[str] = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        text = source_to_text(cell.get("source"))
        headings.extend(strip_markdown(match.group(1)) for match in HEADING_RE.finditer(text))
    return headings


def notebook_markdown_text(notebook: dict) -> str:
    parts = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            parts.append(source_to_text(cell.get("source")))
    return "\n".join(parts)


def parse_toc(root: Path, handbook: str) -> list[TocChapter]:
    toc_path = root / handbook / "TOC.md"
    if not toc_path.exists():
        return []
    lines = toc_path.read_text(encoding="utf-8").splitlines()
    chapters: list[TocChapter] = []
    current_part: str | None = None
    current_index: int | None = None

    for index, line in enumerate(lines):
        stripped = line.strip()
        if PART_RE.match(stripped):
            current_part = strip_markdown(stripped)
            continue
        chapter_match = parse_toc_chapter_line(line)
        if chapter_match:
            number, title, link = chapter_match
            chapters.append(
                TocChapter(
                    number=number,
                    title=sanitize_promotional_text(title),
                    link=unquote(link) if link else None,
                    line_index=index,
                    subtopics=[],
                    part_title=current_part,
                )
            )
            current_index = len(chapters) - 1
            continue
        if current_index is None:
            continue
        if stripped.startswith(("-", "*")):
            chapters[current_index].subtopics.append(strip_markdown(stripped[1:].strip()))

    return chapters


def is_appendix_text(value: str) -> bool:
    lowered = normalize_text(value)
    return lowered.startswith("appendix") or " appendix " in f" {lowered} "


def is_appendix_notebook(path: Path) -> bool:
    return is_appendix_text(path.stem) or any(is_appendix_text(part) for part in path.parts)


def best_notebook_match(entry: TocChapter, notebooks: list[NotebookRecord]) -> NotebookRecord | None:
    candidates = [record for record in notebooks if record.chapter_number == entry.number]
    if not candidates:
        return None
    best_record: NotebookRecord | None = None
    best_score = -1.0
    for candidate in candidates:
        score = similarity(entry.title, candidate.path.stem)
        if entry.part_title:
            score += similarity(entry.part_title, candidate.path.parent.name) * 0.2
        if score > best_score:
            best_score = score
            best_record = candidate
    return best_record


def subtopic_is_covered(subtopic: str, headings: list[str], full_text: str) -> bool:
    normalized_subtopic = normalize_text(subtopic)
    if not normalized_subtopic:
        return True
    subtopic_tokens = title_tokens(subtopic)
    full_text_normalized = normalize_text(full_text)

    for heading in headings:
        normalized_heading = normalize_text(heading)
        if normalized_subtopic in normalized_heading or normalized_heading in normalized_subtopic:
            return True
        if similarity(subtopic, heading) >= 0.72:
            return True
        heading_tokens = title_tokens(heading)
        if subtopic_tokens and len(subtopic_tokens & heading_tokens) / len(subtopic_tokens) >= 0.6:
            return True

    if subtopic_tokens and len([token for token in subtopic_tokens if token in full_text_normalized.split()]) / len(subtopic_tokens) >= 0.8:
        return True
    return False


def audit_handbook(root: Path, handbook: str) -> HandbookAudit:
    notebooks = discover_notebooks(root, handbook)
    toc_entries = parse_toc(root, handbook)
    toc_path = root / handbook / "TOC.md"
    toc_text = toc_path.read_text(encoding="utf-8") if toc_path.exists() else ""

    audit = HandbookAudit(
        handbook=handbook,
        toc_chapter_count=len(toc_entries),
        notebook_count=len(notebooks),
        toc_chapter_count_excluding_appendix=len([entry for entry in toc_entries if not is_appendix_text(entry.title)]),
        notebook_count_excluding_appendix=len([record for record in notebooks if not is_appendix_notebook(record.path.relative_to(root / handbook))]),
        intro_issues_in_toc=has_banned_meta("\n".join(toc_text.splitlines()[:12])),
    )

    notebook_lookup = {record.relative_path.split("/", 1)[1]: record for record in notebooks}
    referenced_notebooks: set[str] = set()

    for record in notebooks:
        notebook = load_notebook(record.path)
        if has_banned_meta(first_markdown_text(notebook)):
            audit.notebook_intro_issues.append(record.relative_path)

    for entry in toc_entries:
        display_name = f"Chapter {entry.number}: {entry.title}"
        if not entry.link:
            audit.missing_toc_links.append(display_name)
        else:
            linked_path = root / handbook / entry.link
            if not linked_path.exists():
                audit.broken_toc_links.append(f"{display_name} -> {entry.link}")
            else:
                referenced_notebooks.add(linked_path.relative_to(root).as_posix())

        match = best_notebook_match(entry, notebooks)
        if not match:
            audit.unmatched_toc_chapters.append(display_name)
            continue
        referenced_notebooks.add(match.relative_path)
        notebook = load_notebook(match.path)
        headings = notebook_headings(notebook)
        full_text = notebook_markdown_text(notebook)
        missing = [subtopic for subtopic in entry.subtopics if not subtopic_is_covered(subtopic, headings, full_text)]
        if missing:
            audit.likely_missing_subtopics[display_name] = missing[:12]

    for record in notebooks:
        if record.relative_path not in referenced_notebooks:
            audit.orphan_notebooks.append(record.relative_path)

    for path in (root / handbook).rglob("*"):
        if path.is_dir() and path.name.endswith(".ipynb"):
            audit.malformed_directories.append(path.relative_to(root).as_posix())

    return audit


def cleanup_handbook(root: Path, handbook: str) -> CleanupSummary:
    summary = CleanupSummary(handbook=handbook)
    toc_path = root / handbook / "TOC.md"
    if toc_path.exists():
        cleaned_toc, changed = clean_toc_text(toc_path.read_text(encoding="utf-8"), handbook)
        if changed:
            toc_path.write_text(cleaned_toc, encoding="utf-8")
            summary.toc_changed = True

    for record in discover_notebooks(root, handbook):
        notebook = load_notebook(record.path)
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            original = source_to_text(cell.get("source"))
            cleaned, changed = clean_notebook_intro_text(original)
            if changed:
                cell["source"] = text_to_source(cleaned)
                record.path.write_text(json.dumps(notebook, indent=1) + "\n", encoding="utf-8")
                summary.notebooks_changed += 1
            break

    return summary


def normalize_structural_anomalies(root: Path, handbooks: list[str]) -> list[tuple[str, str]]:
    renames: list[tuple[str, str]] = []
    for handbook in handbooks:
        for path in sorted((root / handbook).rglob("*")):
            if not path.is_dir() or not path.name.endswith(".ipynb"):
                continue
            target = path.with_name(path.name[: -len(".ipynb")])
            if target.exists():
                raise FileExistsError(f"Cannot rename {path} to {target}: target already exists.")
            path.rename(target)
            renames.append((path.relative_to(root).as_posix(), target.relative_to(root).as_posix()))
    return renames


def run_helper(root: Path, script_name: str, handbooks: list[str]) -> None:
    if not handbooks:
        return
    subprocess.run(
        [sys.executable, script_name, *handbooks],
        cwd=root,
        check=True,
    )


def write_report(root: Path, audits: list[HandbookAudit]) -> tuple[Path, Path]:
    report_dir = root / "reports" / "handbook_rewrite"
    report_dir.mkdir(parents=True, exist_ok=True)
    json_path = report_dir / "audit.json"
    markdown_path = report_dir / "audit.md"

    json_path.write_text(json.dumps([asdict(audit) for audit in audits], indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Handbook Rewrite Audit",
        "",
        "| Handbook | TOC Chapters | Notebooks | Missing Links | Broken Links | Orphans | Intro Issues | Malformed Dirs | Likely Missing Subtopic Sections |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for audit in audits:
        intro_issue_count = audit.intro_issues_in_toc + len(audit.notebook_intro_issues)
        lines.append(
            f"| {audit.handbook} | {audit.toc_chapter_count_excluding_appendix}/{audit.toc_chapter_count} | {audit.notebook_count_excluding_appendix}/{audit.notebook_count} | "
            f"{len(audit.missing_toc_links)} | {len(audit.broken_toc_links)} | {len(audit.orphan_notebooks)} | "
            f"{intro_issue_count} | {len(audit.malformed_directories)} | {len(audit.likely_missing_subtopics)} |"
        )

    for audit in audits:
        lines.extend(
            [
                "",
                f"## {audit.handbook}",
                "",
            ]
        )
        if audit.intro_issues_in_toc:
            lines.append("- TOC intro/meta text still needs cleanup.")
        if audit.notebook_intro_issues:
            lines.append(f"- Notebook intro cleanup needed: {', '.join(audit.notebook_intro_issues[:8])}")
        if audit.missing_toc_links:
            lines.append(f"- Missing TOC links: {', '.join(audit.missing_toc_links[:8])}")
        if audit.broken_toc_links:
            lines.append(f"- Broken TOC links: {', '.join(audit.broken_toc_links[:8])}")
        if audit.orphan_notebooks:
            lines.append(f"- Orphan notebooks: {', '.join(audit.orphan_notebooks[:8])}")
        if audit.malformed_directories:
            lines.append(f"- Malformed directories: {', '.join(audit.malformed_directories[:8])}")
        if audit.unmatched_toc_chapters:
            lines.append(f"- TOC chapters without notebook match: {', '.join(audit.unmatched_toc_chapters[:8])}")
        if audit.likely_missing_subtopics:
            lines.append("- Chapters with likely missing TOC-covered subtopics:")
            for chapter, subtopics in list(audit.likely_missing_subtopics.items())[:8]:
                lines.append(f"  - {chapter}: {', '.join(subtopics[:5])}")
        if lines[-1] == "":
            continue

    markdown_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return json_path, markdown_path


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit and clean handbook intro/meta content.")
    parser.add_argument("--audit", action="store_true", help="Audit selected handbooks.")
    parser.add_argument("--cleanup-intros", action="store_true", help="Remove intro/meta framing from TOCs and notebook first markdown cells.")
    parser.add_argument("--handbooks", nargs="+", help="Optional list of handbook directories to process.")
    parser.add_argument("--report", action="store_true", help="Write audit reports to reports/handbook_rewrite/.")
    parser.add_argument(
        "--normalize-structure",
        action="store_true",
        help="Rename malformed directories that end with .ipynb before relinking and auditing.",
    )
    parser.add_argument(
        "--regenerate-links",
        action="store_true",
        help="Run TOC link and notebook navigation regeneration for the selected handbooks.",
    )
    parser.add_argument("--run-full-sweep", action="store_true", help="Run maintenance in the required wave order.")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    if not any((args.audit, args.cleanup_intros, args.normalize_structure, args.regenerate_links, args.run_full_sweep)):
        print("No action requested. Use --audit, --cleanup-intros, --normalize-structure, or --regenerate-links.", file=sys.stderr)
        return 1

    root = Path.cwd()
    if not (root / "README.md").exists():
        print("Run this utility from the repository root.", file=sys.stderr)
        return 1

    handbooks = ordered_handbooks(root, args.handbooks)
    if not handbooks:
        print("No matching handbooks found.", file=sys.stderr)
        return 1

    if args.run_full_sweep:
        print("Running pre-wave normalization and wave-ordered maintenance.")
        pre_wave = [name for name in PRE_WAVE_NORMALIZATION if name in handbooks]
        if pre_wave:
            if normalize_structural_anomalies(root, pre_wave):
                print("Pre-wave normalization complete.")
            for handbook in pre_wave:
                summary = cleanup_handbook(root, handbook)
                print(f"{handbook}: toc_changed={'yes' if summary.toc_changed else 'no'}, notebooks_changed={summary.notebooks_changed}")
            run_helper(root, "update_toc_links.py", pre_wave)
            run_helper(root, "add_nav_links.py", pre_wave)

        for wave_name in ("wave1", "wave2", "wave3", "wave4"):
            wave_targets = [name for name in REWRITE_WAVES[wave_name] if name in handbooks]
            if not wave_targets:
                continue
            print(f"\n== {wave_name} ==")
            for handbook in wave_targets:
                summary = cleanup_handbook(root, handbook)
                print(f"{handbook}: toc_changed={'yes' if summary.toc_changed else 'no'}, notebooks_changed={summary.notebooks_changed}")
            run_helper(root, "update_toc_links.py", wave_targets)
            run_helper(root, "add_nav_links.py", wave_targets)
    else:
        if args.normalize_structure:
            renames = normalize_structural_anomalies(root, handbooks)
            if renames:
                print("Normalized malformed directories:")
                for old, new in renames:
                    print(f"  - {old} -> {new}")
            else:
                print("No malformed directories needed renaming.")

        if args.cleanup_intros:
            for handbook in handbooks:
                summary = cleanup_handbook(root, handbook)
                print(
                    f"{handbook}: toc_changed={'yes' if summary.toc_changed else 'no'}, "
                    f"notebooks_changed={summary.notebooks_changed}"
                )

        if args.regenerate_links or args.cleanup_intros or args.normalize_structure:
            run_helper(root, "update_toc_links.py", handbooks)
            run_helper(root, "add_nav_links.py", handbooks)

    audits: list[HandbookAudit] = []
    if args.audit or args.report:
        audits = [audit_handbook(root, handbook) for handbook in handbooks]
        for audit in audits:
            intro_issues = audit.intro_issues_in_toc + len(audit.notebook_intro_issues)
            print(
                f"{audit.handbook}: missing_links={len(audit.missing_toc_links)}, "
                f"broken_links={len(audit.broken_toc_links)}, orphans={len(audit.orphan_notebooks)}, "
                f"intro_issues={intro_issues}, malformed_dirs={len(audit.malformed_directories)}, "
                f"coverage_flags={len(audit.likely_missing_subtopics)}"
            )

    if args.report:
        json_path, markdown_path = write_report(root, audits)
        print(f"Report written to {json_path.relative_to(root)} and {markdown_path.relative_to(root)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
