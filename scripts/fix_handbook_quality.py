#!/usr/bin/env python3
"""
Dev-Handbook Quality Fix Script
================================
Fixes three categories of issues across all 945 notebooks:

1. Removes repetitive boilerplate meta-instruction phrases
2. Labels unlabeled markdown code fences (```) → (```text)
3. Converts ASCII-art-only code cells to markdown text blocks

Usage:
    python3 scripts/fix_handbook_quality.py [--dry-run] [--section SECTION]

Options:
    --dry-run    Show what would be changed without writing files
    --section    Only process one handbook section (e.g. 'flask', 'python')
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Boilerplate patterns to remove
# ---------------------------------------------------------------------------

# These phrases were inserted programmatically by a rewrite script and
# interrupt the reading flow without adding educational value.
BOILERPLATE_PATTERNS: list[re.Pattern] = [
    # "A first-time learner usually gets the most value from this chapter..."
    re.compile(
        r"A first-time learner usually gets the most value from this chapter by asking "
        r"what problem this topic solves, what changes when you apply it correctly, "
        r"and what breaks when you misunderstand it\. "
        r"The sections below are much easier to follow once that thread is visible\.\s*",
        re.IGNORECASE,
    ),
    # "You do not need to memorize every term on first read..."
    re.compile(
        r"You do not need to memorize every term on first read\. "
        r"Focus on the responsibility this topic carries, the situations where it becomes "
        r"useful, and the small signals that tell you you are using it well\. "
        r"The rest of the chapter fills in the supporting detail around that core idea\.\s*",
        re.IGNORECASE,
    ),
    # "If this topic is new, keep translating each new term..."
    re.compile(
        r"If this topic is new, keep translating each new term into a simple question: "
        r"what job does it do, when would you reach for it, and what would you confuse it "
        r"with if you were moving too quickly\? That habit makes the section easier to retain\.\s*",
        re.IGNORECASE,
    ),
    # "The easiest way to read this section is to keep one plain-language question in view..."
    re.compile(
        r"The easiest way to read this section is to keep one plain-language question in "
        r"view: what is [^?]+\? Once that job is clear, the terminology stops feeling "
        r"arbitrary and the details start to line up\.\s*",
        re.IGNORECASE,
    ),
    # "If the wording here feels abstract at first, anchor it to the concrete job..."
    re.compile(
        r"If the wording here feels abstract at first, anchor it to the concrete job "
        r"[^.]+performs in a real system\. That mental model makes the definitions "
        r"easier to retain and easier to use later\.\s*",
        re.IGNORECASE,
    ),
    # "A beginner usually learns this material faster by connecting each setup step..."
    re.compile(
        r"A beginner usually learns this material faster by connecting each setup step "
        r"to its purpose rather than treating it as a checklist\. "
        r"Keep asking what each piece enables and what would fail if you skipped it\.\s*",
        re.IGNORECASE,
    ),
    # "Keep comparing the job each option does best, the tradeoff it introduces..."
    re.compile(
        r"Keep comparing the job each option does best, the tradeoff it introduces, "
        r"and the clues that tell you which one fits the situation in front of you\.\s*",
        re.IGNORECASE,
    ),
    # Shorter "A beginner usually learns..." variant
    re.compile(
        r"A beginner usually learns this material faster by connecting each setup step "
        r"to its purpose rather than treating it as a checklist\.\s*",
        re.IGNORECASE,
    ),
    # "If this topic is new to you, keep translating it back to three practical ideas..."
    re.compile(
        r"If this topic is new to you, keep translating it back to three practical ideas: "
        r"what job it does, when you would reach for it, and which nearby concepts it is easy "
        r"to confuse with\. That lens will make the details in this chapter feel connected "
        r"instead of memorized\.\s*",
        re.IGNORECASE,
    ),
    # Generic "keep translating each new term" variants
    re.compile(
        r"keep translating (?:it back to three practical ideas|each new term)[^.]+\.\s*",
        re.IGNORECASE,
    ),
]


def remove_boilerplate(source: str) -> tuple[str, int]:
    """Remove all boilerplate phrases from a markdown string.
    Returns (cleaned_source, count_removed).
    """
    removed = 0
    for pattern in BOILERPLATE_PATTERNS:
        new_source, n = pattern.subn("", source)
        removed += n
        source = new_source
    # Clean up multiple consecutive blank lines left by removal
    source = re.sub(r"\n{3,}", "\n\n", source)
    return source, removed


# ---------------------------------------------------------------------------
# Code fence language detection
# ---------------------------------------------------------------------------

LANG_HINTS: list[tuple[re.Pattern, str]] = [
    # Python
    (re.compile(r"^\s*(import |from \w+ import |def |class |@\w+|if __name__)", re.M), "py"),
    # Bash / shell
    (re.compile(r"^\s*(#!/(bin|usr)|sudo |apt |npm |pip |docker |kubectl |git |brew |curl |wget |export |source |echo |\$ )", re.M), "bash"),
    # JavaScript / TypeScript (rough)
    (re.compile(r"^\s*(const |let |var |function |=>|require\(|import .* from|module\.exports|console\.log)", re.M), "js"),
    # TypeScript (more specific)
    (re.compile(r":\s*(string|number|boolean|void|any|unknown|never|Record<|Array<|Promise<)", re.M), "ts"),
    # SQL
    (re.compile(r"^\s*(SELECT |INSERT |UPDATE |DELETE |CREATE |DROP |ALTER |GRANT |REVOKE )", re.M | re.I), "sql"),
    # JSON
    (re.compile(r'^\s*[\{\[]', re.M), "json"),
    # YAML
    (re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*:\s+\S", re.M), "yaml"),
    # HTML
    (re.compile(r"<(html|head|body|div|span|p|a|ul|li|h[1-6])\b", re.I), "html"),
    # Dockerfile
    (re.compile(r"^\s*(FROM |RUN |COPY |ADD |ENV |WORKDIR |EXPOSE |CMD |ENTRYPOINT )", re.M), "dockerfile"),
    # C#
    (re.compile(r"^\s*(using |namespace |public class |private |protected |internal |override |async Task|new \w+\()", re.M), "csharp"),
    # Solidity
    (re.compile(r"^\s*(pragma solidity|contract |mapping\(|event |emit |uint|address)", re.M), "solidity"),
]

ASCII_ART_CHARS = set("┌│└─┬┴├┤╔║╗╚╝╠╣╬═┼┐┘")


def is_ascii_art(source: str) -> bool:
    """Return True if source is primarily ASCII art / diagram."""
    lines = source.strip().split("\n")
    if len(lines) < 2:
        return False
    box_lines = sum(1 for l in lines if any(ch in l for ch in ASCII_ART_CHARS))
    return box_lines >= max(2, len(lines) * 0.25)


def detect_language(source: str) -> str:
    """Detect the programming language of a code block. Returns language tag."""
    if is_ascii_art(source):
        return "text"
    for pattern, lang in LANG_HINTS:
        if pattern.search(source):
            return lang
    # Check for common output / console patterns
    if re.search(r"^\s*(Error:|Warning:|INFO|DEBUG|WARN|Traceback|File \"|line \d+)", source, re.M):
        return "text"
    # If it has no obvious code and looks like prose/output, use text
    lines = source.strip().split("\n")
    prose_lines = sum(
        1 for l in lines if re.match(r"^\s*[A-Z][a-z]", l) and "=" not in l and "(" not in l
    )
    if prose_lines > len(lines) * 0.5:
        return "text"
    return "text"


def fix_unlabeled_fences(source: str) -> tuple[str, int]:
    """Add language tags to unlabeled ``` code fences.
    Correctly handles nested/inside states so closing fences are never modified.
    Returns (fixed_source, count_fixed).
    """
    fixed = 0
    output = []
    i = 0
    lines = source.split("\n")
    inside_fence = False
    current_fence_char = ""

    while i < len(lines):
        line = lines[i]

        if inside_fence:
            # Look for the matching closing fence
            if line.rstrip() == current_fence_char or line.startswith(current_fence_char + "\n") or line == current_fence_char:
                inside_fence = False
                current_fence_char = ""
            output.append(line)
            i += 1

        else:
            # Check for a labeled opening fence (already has a language)
            labeled_match = re.match(r"^(`{3,})(\w+)", line)
            if labeled_match:
                inside_fence = True
                current_fence_char = labeled_match.group(1)
                output.append(line)
                i += 1

            # Check for an unlabeled opening fence
            elif re.match(r"^(`{3,})\s*$", line):
                fence_char = re.match(r"^(`{3,})", line).group(1)
                # Collect block content to detect language
                block_lines = []
                j = i + 1
                while j < len(lines):
                    closing = lines[j].rstrip()
                    if closing == fence_char:
                        break
                    block_lines.append(lines[j])
                    j += 1
                block_content = "\n".join(block_lines)
                lang = detect_language(block_content)
                output.append(f"{fence_char}{lang}")
                output.extend(block_lines)
                if j < len(lines):
                    output.append(lines[j])  # closing fence
                i = j + 1
                fixed += 1

            else:
                output.append(line)
                i += 1

    return "\n".join(output), fixed


# ---------------------------------------------------------------------------
# ASCII-art code cell → markdown conversion
# ---------------------------------------------------------------------------

def should_convert_to_markdown(cell: dict) -> bool:
    """Return True if a code cell should become a markdown text block."""
    src = "".join(cell.get("source", []))
    if not src.strip():
        return False
    # Must be primarily ASCII art with no real code constructs
    if not is_ascii_art(src):
        return False
    real_code_markers = [
        "def ", "class ", "import ", "function ", "const ", "let ", "var ",
        "SELECT ", "CREATE ", "INSERT ", "DELETE ", "FROM ", "WHERE ",
        "#!/", ".method(", "->", "::", "npm ", "pip ", "docker ", "kubectl ",
        "require(", "module.", "export ", "return ", "print(",
    ]
    if any(m in src for m in real_code_markers):
        return False
    return True


def code_cell_to_markdown_text(cell: dict) -> dict:
    """Convert an ASCII-art code cell to a markdown cell with ```text fence."""
    src = "".join(cell.get("source", []))
    new_src = f"```text\n{src.rstrip()}\n```"
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [new_src],
    }


# ---------------------------------------------------------------------------
# Notebook processing
# ---------------------------------------------------------------------------

def process_notebook(path: Path, dry_run: bool = False) -> dict:
    """Process a single notebook. Returns stats dict."""
    stats = {
        "boilerplate_removed": 0,
        "fences_fixed": 0,
        "cells_converted": 0,
        "changed": False,
    }

    try:
        text = path.read_text(encoding="utf-8")
        nb = json.loads(text)
    except Exception as e:
        print(f"  ERROR reading {path}: {e}", file=sys.stderr)
        return stats

    new_cells = []
    changed = False

    for cell in nb.get("cells", []):
        cell_type = cell.get("cell_type", "")

        if cell_type == "markdown":
            src = "".join(cell.get("source", []))

            # 1. Remove boilerplate
            new_src, n_removed = remove_boilerplate(src)
            stats["boilerplate_removed"] += n_removed

            # 2. Fix unlabeled code fences
            new_src, n_fixed = fix_unlabeled_fences(new_src)
            stats["fences_fixed"] += n_fixed

            if new_src != src:
                changed = True
                cell = dict(cell)
                cell["source"] = [new_src]

            new_cells.append(cell)

        elif cell_type == "code":
            if should_convert_to_markdown(cell):
                new_cells.append(code_cell_to_markdown_text(cell))
                stats["cells_converted"] += 1
                changed = True
            else:
                new_cells.append(cell)

        else:
            new_cells.append(cell)

    stats["changed"] = changed

    if changed and not dry_run:
        nb["cells"] = new_cells
        new_text = json.dumps(nb, ensure_ascii=False, indent=1)
        path.write_text(new_text, encoding="utf-8")

    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fix handbook quality issues")
    parser.add_argument("--dry-run", action="store_true", help="Don't write any files")
    parser.add_argument("--section", help="Only process this handbook section")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent

    if args.section:
        notebooks = sorted((repo_root / args.section).rglob("*.ipynb"))
    else:
        notebooks = sorted(repo_root.rglob("*.ipynb"))

    # Exclude checkpoints
    notebooks = [n for n in notebooks if ".ipynb_checkpoints" not in str(n)]

    total_stats = {
        "files": 0,
        "files_changed": 0,
        "boilerplate_removed": 0,
        "fences_fixed": 0,
        "cells_converted": 0,
    }

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Processing {len(notebooks)} notebooks...")
    print()

    for nb_path in notebooks:
        rel = nb_path.relative_to(repo_root)
        stats = process_notebook(nb_path, dry_run=args.dry_run)
        total_stats["files"] += 1

        if stats["changed"]:
            total_stats["files_changed"] += 1
            total_stats["boilerplate_removed"] += stats["boilerplate_removed"]
            total_stats["fences_fixed"] += stats["fences_fixed"]
            total_stats["cells_converted"] += stats["cells_converted"]
            if stats["boilerplate_removed"] or stats["fences_fixed"] or stats["cells_converted"]:
                parts = []
                if stats["boilerplate_removed"]:
                    parts.append(f"{stats['boilerplate_removed']} boilerplate")
                if stats["fences_fixed"]:
                    parts.append(f"{stats['fences_fixed']} fences")
                if stats["cells_converted"]:
                    parts.append(f"{stats['cells_converted']} cells→md")
                print(f"  ✓ {rel}  [{', '.join(parts)}]")

    print()
    print("=" * 60)
    print(f"Files processed  : {total_stats['files']}")
    print(f"Files changed    : {total_stats['files_changed']}")
    print(f"Boilerplate removed: {total_stats['boilerplate_removed']}")
    print(f"Code fences labeled: {total_stats['fences_fixed']}")
    print(f"ASCII cells → MD : {total_stats['cells_converted']}")
    print("=" * 60)

    if args.dry_run:
        print("\n[DRY RUN] No files were modified.")


if __name__ == "__main__":
    main()
