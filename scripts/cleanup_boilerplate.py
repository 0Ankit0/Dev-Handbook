#!/usr/bin/env python3
"""Remove leftover boilerplate phrases from DSA and networking notebooks."""

import json
import glob
import re

BASE = '/media/ankit/Programming/Projects/Dev-Handbook'

BOILERPLATE_PHRASES = [
    "A first read goes better when you connect every new idea to a concrete responsibility and a concrete use case. Once those anchors are in place, the terminology in this section becomes much easier to reuse accurately.",
    "If this section feels dense, pause and identify the data structure or model first. Most of the APIs here make more sense once you know what is being stored, queried, or transformed.",
    "If this topic is new to you, keep translating it back to three practical ideas: what job it does, when you would reach for it, and which nearby concepts it is easy to confuse with. That lens will make the details in this chapter feel connected instead of memorized.",
    "When a section introduces a boundary between systems, focus on the contract first: what information crosses the boundary, who is allowed to send it, and what the caller can safely assume in return.",
    r'The important beginner shift here is moving from "it works on my machine" to "it behaves predictably in a real environment." Each step matters because it reduces surprises when the software runs elsewhere.',
    "A useful beginner mental model here is to separate the shape of the data from the operations performed on it. Once you know what is being represented and who depends on that representation, the rules become easier to predict.",
    "A helpful beginner shortcut here is to ask why the system is split this way at all. Once the separation of responsibilities is clear, the patterns feel like practical decisions instead of abstract rules.",
]

def clean_cell(source_str):
    """Remove boilerplate phrases from a cell's source text."""
    for phrase in BOILERPLATE_PHRASES:
        # Remove phrase with optional surrounding newlines
        source_str = source_str.replace('\n' + phrase + '\n', '\n')
        source_str = source_str.replace(phrase + '\n', '')
        source_str = source_str.replace('\n' + phrase, '')
        source_str = source_str.replace(phrase, '')
    # Collapse more than 2 consecutive blank lines into 2
    source_str = re.sub(r'\n{3,}', '\n\n', source_str)
    return source_str.strip()

total_changed = 0
total_notebooks = 0

for folder in ['dsa', 'networking']:
    for path in sorted(glob.glob(f'{BASE}/{folder}/**/*.ipynb', recursive=True)):
        nb = json.load(open(path))
        changed = False
        for cell in nb['cells']:
            original = ''.join(cell.get('source', []))
            cleaned = clean_cell(original)
            if cleaned != original:
                # Reconstruct source as list of lines (preserve newlines)
                if cleaned:
                    lines = cleaned.splitlines(keepends=True)
                    cell['source'] = lines
                else:
                    cell['source'] = []
                changed = True
        if changed:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
            total_changed += 1
            rel = path.replace(BASE + '/', '')
            print(f'Cleaned: {rel}')
    total_notebooks += 1

print(f'\nDone: {total_changed} notebooks cleaned.')
