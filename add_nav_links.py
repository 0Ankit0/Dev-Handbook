#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from urllib.parse import unquote


def chapter_number(path: Path) -> int:
    match = re.match(r"^\s*(\d+)", path.name)
    return int(match.group(1)) if match else 10**9


def discover_notebooks(handbook_dir: Path) -> list[Path]:
    notebooks = [
        path
        for path in handbook_dir.rglob("*.ipynb")
        if path.is_file() and ".ipynb_checkpoints" not in path.parts
    ]
    notebooks.sort(key=lambda item: (chapter_number(item), item.relative_to(handbook_dir).as_posix()))
    return notebooks




def discover_toc_order(handbook_dir: Path, notebooks: list[Path]) -> list[Path]:
    toc_path = handbook_dir / "TOC.md"
    if not toc_path.exists():
        return notebooks

    notebook_lookup = {path.relative_to(handbook_dir).as_posix(): path for path in notebooks}
    ordered: list[Path] = []
    seen: set[Path] = set()
    link_patterns = [
        re.compile(r"\[Chapter \d+: [^\]]+\]\(([^)]+)\)"),
        re.compile(r"\[\d+\. [^\]]+\]\(([^)]+)\)"),
        re.compile(r"\[[^\]]+\]\(([^)]+\.ipynb)\)"),
    ]
    for line in toc_path.read_text(encoding="utf-8").splitlines():
        for pattern in link_patterns:
            match = pattern.search(line)
            if not match:
                continue
            relative = unquote(match.group(1).strip())
            notebook = notebook_lookup.get(relative)
            if notebook and notebook not in seen:
                ordered.append(notebook)
                seen.add(notebook)
            break

    if not ordered:
        return notebooks
    for notebook in notebooks:
        if notebook not in seen:
            ordered.append(notebook)
    return ordered


def source_to_text(source: object) -> str:
    if isinstance(source, str):
        return source
    if isinstance(source, list):
        return "".join(source)
    return ""


def text_to_source(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def is_nav_cell(cell: dict) -> bool:
    if cell.get("cell_type") != "markdown":
        return False
    text = source_to_text(cell.get("source"))
    return (
        "Table of Contents" in text
        and ("Previous" in text or "&larr;" in text)
        and ("Next" in text or "&rarr;" in text)
    )


def relative_href(from_path: Path, to_path: Path) -> str:
    return Path(os.path.relpath(to_path, from_path.parent)).as_posix()


def nav_html(handbook_dir: Path, notebook: Path, previous_notebook: Path | None, next_notebook: Path | None) -> str:
    toc_path = handbook_dir / "TOC.md"
    toc_href = relative_href(notebook, toc_path)

    if previous_notebook is None:
        previous_html = "  <span style='color:gray; font-size:1.05em;'>Previous</span>"
    else:
        previous_href = relative_href(notebook, previous_notebook)
        previous_html = (
            f"  <a href='{previous_href}' style='font-weight:bold; font-size:1.05em;'>&larr; Previous</a>"
        )

    if next_notebook is None:
        next_html = "  <span style='color:gray; font-size:1.05em;'>Next</span>"
    else:
        next_href = relative_href(notebook, next_notebook)
        next_html = f"  <a href='{next_href}' style='font-weight:bold; font-size:1.05em;'>Next &rarr;</a>"

    return (
        "<div style='width:100%; display:flex; justify-content:space-between; align-items:center; margin: 1em 0;'>\n"
        f"{previous_html}\n"
        f"  <a href='{toc_href}' style='font-weight:bold; font-size:1.05em; text-align:center;'>Table of Contents</a>\n"
        f"{next_html}\n"
        "</div>\n"
    )


def update_notebook(handbook_dir: Path, notebook_path: Path, previous_notebook: Path | None, next_notebook: Path | None) -> bool:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    if cells and is_nav_cell(cells[-1]):
        cells.pop()

    html = nav_html(handbook_dir, notebook_path, previous_notebook, next_notebook)
    nav_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": text_to_source(html),
    }
    cells.append(nav_cell)
    notebook["cells"] = cells
    new_text = json.dumps(notebook, indent=1) + "\n"
    old_text = notebook_path.read_text(encoding="utf-8")
    if new_text == old_text:
        return False
    notebook_path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Append previous/next navigation to handbook notebooks.")
    parser.add_argument("targets", nargs="+", help="One or more handbook directories.")
    args = parser.parse_args()

    root = Path.cwd()
    total_updated = 0

    for target in args.targets:
        handbook_dir = root / target
        if not handbook_dir.is_dir():
            print(f"{target}: skipped (directory not found)")
            continue
        notebooks = discover_toc_order(handbook_dir, discover_notebooks(handbook_dir))
        print(f"{target}: found {len(notebooks)} notebook(s)")
        updated = 0
        for index, notebook_path in enumerate(notebooks):
            previous_notebook = notebooks[index - 1] if index > 0 else None
            next_notebook = notebooks[index + 1] if index + 1 < len(notebooks) else None
            if update_notebook(handbook_dir, notebook_path, previous_notebook, next_notebook):
                updated += 1
        total_updated += updated
        print(f"{target}: updated {updated} notebook(s)")

    print(f"\nUpdated {total_updated} notebook(s) with navigation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
