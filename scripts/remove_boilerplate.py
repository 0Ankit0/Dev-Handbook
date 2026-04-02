#!/usr/bin/env python3
"""Remove boilerplate phrases from all .ipynb notebooks in fastapi/ and django/."""
import json
import re
from pathlib import Path

BOILERPLATE_PHRASES = [
    "A first read goes better when you connect every new idea to a concrete responsibility and a concrete use case. Once those anchors are in place, the terminology in this section becomes much easier to reuse accurately.",
    "Sections like this become clearer when you separate capabilities from tradeoffs. As you read, ask what each option is optimized for and what complexity you accept in exchange.",
    "The hard part here is usually not the syntax but the boundary between similar ideas.",
    "A helpful beginner shortcut here is to ask why the system is split this way at all. Once the separation of responsibilities is clear, the patterns feel like practical decisions instead of abstract rules.",
    "Architecture material sounds bigger than it is if you read it only as terminology. Start by identifying the responsibility of each part and the reason those responsibilities are separated; the structure usually becomes much clearer from there.",
    "The important beginner shift here is moving from \"it works on my machine\" to \"it behaves predictably in a real environment.\" Each step matters because it reduces surprises when the software runs elsewhere.",
    "If this section feels dense, pause and identify the data structure or model first. Most of the APIs here make more sense once you know what is being stored, queried, or transformed.",
    "Production-oriented material makes more sense when you see it as reliability work. The tools and steps here exist to make behavior repeatable, observable, and safer to change.",
    "Whenever a process has several stages, beginners benefit from tracing the handoff between them. Follow the order carefully and notice what information each step receives, transforms, and passes on.",
]

ROOT = Path("/media/ankit/Programming/Projects/Dev-Handbook")
DIRS = [ROOT / "fastapi", ROOT / "django"]


def clean_cell_source(source_lines: list[str]) -> tuple[list[str], bool]:
    text = "".join(source_lines)
    original = text

    for phrase in BOILERPLATE_PHRASES:
        text = text.replace(phrase, "")

    if text == original:
        return source_lines, False

    # Collapse 3+ consecutive newlines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Strip leading/trailing whitespace only (don't strip internal content)
    text = text.strip('\n')

    if not text.strip():
        return [], True

    # Re-split into lines, each ending with \n except the last
    lines = text.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        else:
            result.append(line)

    return result, True


def process_notebook(path: Path) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    modified_count = 0
    for cell in nb['cells']:
        if cell.get('cell_type') != 'markdown':
            continue
        new_source, changed = clean_cell_source(cell['source'])
        if changed:
            cell['source'] = new_source
            modified_count += 1

    if modified_count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"  {path.relative_to(ROOT)}: {modified_count} cell(s) modified")

    return modified_count


def main():
    total_cells = 0
    total_files = 0
    for d in DIRS:
        notebooks = sorted(d.rglob("*.ipynb"))
        print(f"\n=== {d.name}/ ({len(notebooks)} notebooks) ===")
        for nb_path in notebooks:
            count = process_notebook(nb_path)
            if count:
                total_files += 1
                total_cells += count

    print(f"\nDone. {total_cells} cells modified across {total_files} notebooks.")


if __name__ == "__main__":
    main()
