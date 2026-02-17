#!/usr/bin/env python3
import os, json, re, sys

def extract_chapter_number(filename):
    match = re.match(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')


python_folder = sys.argv[1] if len(sys.argv) > 1 else "./python"

all_notebooks = []
for folder_name in sorted(os.listdir(python_folder)):
    folder_path = os.path.join(python_folder, folder_name)
    if not os.path.isdir(folder_path) or not re.match(r'^\d+\.', folder_name):
        continue
    
    for notebook in sorted(os.listdir(folder_path)):
        if notebook.endswith('.ipynb'):
            chapter_num = extract_chapter_number(notebook)
            all_notebooks.append((chapter_num, folder_name, folder_path, notebook))

all_notebooks.sort(key=lambda x: x[0])
print(f"Found {len(all_notebooks)} notebooks\n")

for idx, (ch_num, folder, folder_path, notebook) in enumerate(all_notebooks):
    prev_nb = all_notebooks[idx - 1] if idx > 0 else None
    next_nb = all_notebooks[idx + 1] if idx < len(all_notebooks) - 1 else None
    
    prev_link = ""
    if prev_nb:
        prev_ch, prev_folder, prev_folder_path, prev_notebook = prev_nb
        prev_path = prev_notebook if folder_path == prev_folder_path else f"../{prev_folder}/{prev_notebook}"
        prev_link = f"  <a href='{prev_path}' style='font-weight:bold; font-size:1.05em;'>&larr; Previous</a>\n"
    else:
        prev_link = "  <span style='color:gray; font-size:1.05em;'>Previous</span>\n"
    
    next_link = ""
    if next_nb:
        next_ch, next_folder, next_folder_path, next_notebook = next_nb
        next_path = next_notebook if folder_path == next_folder_path else f"../{next_folder}/{next_notebook}"
        next_link = f"  <a href='{next_path}' style='font-weight:bold; font-size:1.05em;'>Next &rarr;</a>\n"
    else:
        next_link = "  <span style='color:gray; font-size:1.05em;'>Next</span>\n"
    
    html = f"<div style='width:100%; display:flex; justify-content:space-between; align-items:center; margin: 1em 0;'>\n{prev_link}  <a href='../TOC.md' style='font-weight:bold; font-size:1.05em; text-align:center;'>Table of Contents</a>\n{next_link}</div>\n"
    
    nb_path = os.path.join(folder_path, notebook)
    with open(nb_path, 'r') as f:
        content = json.load(f)
    
    if content.get('cells') and 'width:100%' in str(content['cells'][-1].get('source', '')):
        content['cells'].pop()
    
    nav_cell = {"cell_type": "markdown", "metadata": {}, "source": [line + '\n' for line in html.rstrip('\n').split('\n')]}
    content['cells'].append(nav_cell)
    
    with open(nb_path, 'w') as f:
        json.dump(content, f, indent=1)
    
    print(f"✓ Ch {ch_num:2d}: {folder}/{notebook}")
    if prev_nb:
        print(f"           ← Ch {prev_nb[0]}")
    if next_nb:
        print(f"           → Ch {next_nb[0]}")

print(f"\n✓ Updated {len(all_notebooks)} notebooks with cross-folder navigation")
