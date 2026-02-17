import os
import re
import json
import argparse

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s.upper()):
        val = roman[char]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

def to_snake_case(s):
    s = re.sub(r'[^\w\s-]', '', s)  # remove punctuation
    s = re.sub(r'[\s_-]+', '_', s)  # replace spaces and dashes with _
    s = s.lower()
    return s

def remove_parentheses(s):
    """Remove text within parentheses and brackets"""
    return re.sub(r'\s*[\(\[].*?[\)\]]', '', s).strip()

def main():
    parser = argparse.ArgumentParser(description="Create folder structure from TOC.md")
    parser.add_argument('folder_path', help='Path to the folder containing TOC.md and where to create the structure')
    args = parser.parse_args()
    
    toc_file = os.path.join(args.folder_path, 'TOC.md')
    if not os.path.exists(toc_file):
        print(f"TOC.md not found in {args.folder_path}.")
        return

    with open(toc_file, 'r') as f:
        lines = f.readlines()

    current_part = None
    for line in lines:
        line_stripped = line.strip()
        
        # Match patterns like: ## **Part I: Name** or ## Part I — Name or ## Part I: Name or ### Part I: Name
        if re.match(r'## \*\*(?:Part|Module) [IVXLCDM]+:', line_stripped, re.IGNORECASE) or \
           re.match(r'## Part [IVXLCDM]+ [—-]', line_stripped) or \
           re.match(r'## Part [IVXLCDM]+:', line_stripped) or \
           re.match(r'### Part [IVXLCDM]+:', line_stripped):
            # Pattern 1: ## **Part I: Name**
            match = re.match(r'## \*\*(?:Part|Module) ([IVXLCDM]+): (.+)\*\*', line_stripped, re.IGNORECASE)
            if not match:
                # Pattern 2: ## Part I — Name or ## Part I - Name
                match = re.match(r'## Part ([IVXLCDM]+) [—-] (.+)', line_stripped, re.IGNORECASE)
            if not match:
                # Pattern 3: ## Part I: Name
                match = re.match(r'## Part ([IVXLCDM]+): (.+)', line_stripped, re.IGNORECASE)
            if not match:
                # Pattern 4: ### Part I: Name
                match = re.match(r'### Part ([IVXLCDM]+): (.+)', line_stripped, re.IGNORECASE)
            
            if match:
                roman_num = match.group(1)
                part_name_raw = match.group(2)
                part_name_clean = remove_parentheses(part_name_raw)
                part_name = to_snake_case(part_name_clean)
                part_num = roman_to_int(roman_num)
                folder_name = f"{part_num}. {part_name}"
                part_path = os.path.join(args.folder_path, folder_name)
                if not os.path.exists(part_path):
                    os.makedirs(part_path, exist_ok=True)
                    print(f"Created part folder: {folder_name}")
                else:
                    print(f"Part folder already exists: {folder_name}")
                current_part = part_path
        
        # Match patterns like: ### **Chapter 1: Name** or ### Chapter 1: Name or **Chapter 1: Name**
        elif current_part:
            # Pattern 1: ### **Chapter 1: Name**
            match = re.match(r'### \*\*Chapter (\d+): (.+)\*\*', line_stripped)
            if not match:
                # Pattern 2: ### Chapter 1: Name
                match = re.match(r'### Chapter (\d+): (.+)', line_stripped)
            if not match:
                # Pattern 3: **Chapter 1: Name**
                match = re.match(r'\*\*Chapter (\d+): (.+)\*\*', line_stripped)
            
            if match:
                chap_num = match.group(1)
                chap_name = match.group(2)
                chap_name_clean = remove_parentheses(chap_name)
                snake_name = to_snake_case(chap_name_clean)
                notebook_name = f"{chap_num}. {snake_name}.ipynb"
                notebook_path = os.path.join(current_part, notebook_name)
                
                if not os.path.exists(notebook_path):
                    # Create basic notebook content
                    notebook_content = {
                        "cells": [
                            {
                                "cell_type": "markdown",
                                "metadata": {},
                                "source": [f"# Chapter {chap_num}: {chap_name_clean}\n"]
                            }
                        ],
                        "metadata": {},
                        "nbformat": 4,
                        "nbformat_minor": 2
                    }
                    
                    with open(notebook_path, 'w') as f:
                        json.dump(notebook_content, f, indent=1)
                    
                    print(f"Created notebook: {notebook_name}")
                else:
                    print(f"Notebook already exists: {notebook_name}")

if __name__ == "__main__":
    main()