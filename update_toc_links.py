#!/usr/bin/env python3
import os
import re
import sys
from urllib.parse import quote

def to_snake_case(s):
    """Convert text to snake_case for file matching"""
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '_', s)
    s = s.lower()
    return s

def remove_parentheses(s):
    """Remove text within parentheses and brackets"""
    return re.sub(r'\s*[\(\[].*?[\)\]]', '', s).strip()

def find_matching_notebook(folder_path, chapter_num, chapter_name):
    """Find the notebook file that matches the chapter number and name"""
    if not os.path.isdir(folder_path):
        return None
    
    chapter_name_clean = remove_parentheses(chapter_name)
    snake_name = to_snake_case(chapter_name_clean)
    
    # Look for numbered folders (e.g., "1. foundations")
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if not os.path.isdir(item_path):
            continue
        
        # Check if this folder might contain our chapter
        for notebook in os.listdir(item_path):
            if not notebook.endswith('.ipynb'):
                continue
            
            # Extract number from notebook name
            match = re.match(r'(\d+)\.', notebook)
            if match and match.group(1) == str(chapter_num):
                # Found matching chapter number - URL encode the path
                notebook_path = os.path.join(item, notebook)
                # URL encode spaces and special characters
                encoded_path = quote(notebook_path, safe='/')
                return encoded_path
    
    return None

def roman_to_int(s):
    """Convert Roman numeral to integer"""
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s.upper()):
        val = roman.get(char, 0)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

def update_toc_file(toc_path):
    """Update a TOC.md file to add links to chapters"""
    folder_path = os.path.dirname(toc_path)
    
    with open(toc_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    current_part = None
    changes_made = 0
    
    for line in lines:
        original_line = line
        line_stripped = line.strip()
        
        # Track current part for context
        if re.match(r'##+ \*?\*?(?:Part|Module) [IVXLCDM]+', line_stripped, re.IGNORECASE):
            current_part = line_stripped
        
        # Pattern 1: ### **Chapter X: Name** (most common in structured TOCs)
        match = re.match(r'^(###+ )\*\*Chapter (\d+): (.+?)\*\*\s*$', line_stripped)
        if not match:
            # Also match if already a link: ### **[Chapter X: Name](...)**
            match = re.match(r'^(###+ )\*\*\[Chapter (\d+): (.+?)\]\(.+?\)\*\*\s*$', line_stripped)
        
        if match:
            prefix, chapter_num, chapter_name = match.groups()
            notebook_path = find_matching_notebook(folder_path, chapter_num, chapter_name)
            if notebook_path:
                new_line = f"{prefix}**[Chapter {chapter_num}: {chapter_name}]({notebook_path})**\n"
                if new_line != original_line:
                    line = new_line
                    changes_made += 1
            updated_lines.append(line)
            continue
        
        # Pattern 2: ### Chapter X: Name (without bold)
        match = re.match(r'^(###+ )Chapter (\d+): (.+?)\s*$', line_stripped)
        if not match:
            # Also match if already a link: ### [Chapter X: Name](...)
            match = re.match(r'^(###+ )\[Chapter (\d+): (.+?)\]\(.+?\)\s*$', line_stripped)
        
        if match:
            prefix, chapter_num, chapter_name = match.groups()
            notebook_path = find_matching_notebook(folder_path, chapter_num, chapter_name)
            if notebook_path:
                new_line = f"{prefix}[Chapter {chapter_num}: {chapter_name}]({notebook_path})\n"
                if new_line != original_line:
                    line = new_line
                    changes_made += 1
            updated_lines.append(line)
            continue
        
        # Pattern 3: ### X. Name (numbered list style)
        match = re.match(r'^(###+ )(\d+)\. (.+?)\s*$', line_stripped)
        if not match:
            # Also match if already a link: ### [X. Name](...)
            match = re.match(r'^(###+ )\[(\d+)\. (.+?)\]\(.+?\)\s*$', line_stripped)
        
        if match:
            prefix, chapter_num, chapter_name = match.groups()
            # Remove any existing markdown links
            chapter_name_clean = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', chapter_name)
            notebook_path = find_matching_notebook(folder_path, chapter_num, chapter_name_clean)
            if notebook_path:
                new_line = f"{prefix}[{chapter_num}. {chapter_name_clean}]({notebook_path})\n"
                if new_line != original_line:
                    line = new_line
                    changes_made += 1
            updated_lines.append(line)
            continue
        
        # Pattern 4: **Chapter X: Name** (bold without heading)
        match = re.match(r'^\*\*Chapter (\d+): (.+?)\*\*\s*$', line_stripped)
        if not match:
            # Also match if already a link: **[Chapter X: Name](...)**
            match = re.match(r'^\*\*\[Chapter (\d+): (.+?)\]\(.+?\)\*\*\s*$', line_stripped)
        
        if match:
            chapter_num, chapter_name = match.groups()
            notebook_path = find_matching_notebook(folder_path, chapter_num, chapter_name)
            if notebook_path:
                new_line = f"**[Chapter {chapter_num}: {chapter_name}]({notebook_path})**\n"
                if new_line != original_line:
                    line = new_line
                    changes_made += 1
            updated_lines.append(line)
            continue
        
        # Keep line as-is if no pattern matched
        updated_lines.append(line)
    
    if changes_made > 0:
        with open(toc_path, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
        print(f"✓ Updated {changes_made} chapter links in {os.path.basename(folder_path)}/TOC.md")
    else:
        print(f"- No changes needed in {os.path.basename(folder_path)}/TOC.md")
    
    return changes_made

def main():
    if len(sys.argv) > 1:
        # Process specific folder
        folder_path = sys.argv[1]
        toc_path = os.path.join(folder_path, 'TOC.md')
        if os.path.exists(toc_path):
            update_toc_file(toc_path)
        else:
            print(f"Error: TOC.md not found in {folder_path}")
    else:
        # Process all TOC.md files in subdirectories
        root_dir = '.'
        total_changes = 0
        processed = 0
        
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                toc_path = os.path.join(item_path, 'TOC.md')
                if os.path.exists(toc_path):
                    changes = update_toc_file(toc_path)
                    total_changes += changes
                    processed += 1
        
        print(f"\n✓ Processed {processed} TOC files with {total_changes} total changes")

if __name__ == "__main__":
    main()
