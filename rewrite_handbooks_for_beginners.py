#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


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

DISALLOWED_HEADINGS = {
    "questions",
    "faq",
    "q&a",
    "common questions",
    "frequently asked questions",
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
TOC_LINK_RE = re.compile(r"\(([^)]+\.ipynb)\)")
LEADING_NUMBER_RE = re.compile(r"^\s*\d+[\.\)]?\s*")
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
FENCED_CODE_RE = re.compile(r"(?ms)^```([^\n`]*)\n(.*?)^```[ \t]*\n?")


INTRO_TEMPLATES = [
    "If this topic is new to you, keep translating it back to three practical ideas: what job it does, when you would reach for it, and which nearby concepts it is easy to confuse with. That lens will make the details in this chapter feel connected instead of memorized.",
    "A first-time learner usually gets the most value from this chapter by asking what problem this topic solves, what changes when you apply it correctly, and what breaks when you misunderstand it. The sections below are much easier to follow once that thread is visible.",
    "You do not need to memorize every term on first read. Focus on the responsibility this topic carries, the situations where it becomes useful, and the small signals that tell you you are using it well. The rest of the chapter fills in the supporting detail around that core idea.",
]

SECTION_TEMPLATES = {
    "concept": [
        "The easiest way to read this section is to keep one plain-language question in view: what is {concept} actually responsible for? Once that job is clear, the terminology stops feeling arbitrary and the details start to line up.",
        "If the wording here feels abstract at first, anchor it to the concrete job {concept} performs in a real system. That mental model makes the definitions easier to retain and easier to use later.",
    ],
    "setup": [
        "Setup steps are easier to remember when you know what each one unlocks. Read this section as a map from each command, option, or file to the problem it solves, so later errors are easier to diagnose instead of feeling random.",
        "A beginner usually learns this material faster by connecting each setup step to its purpose rather than treating it as a checklist. Keep asking what each piece enables and what would fail if you skipped it.",
    ],
    "comparison": [
        "The hard part here is usually not the syntax but the boundary between similar ideas. Keep comparing the job each option does best, the tradeoff it introduces, and the clues that tell you which one fits the situation in front of you.",
        "Sections like this become clearer when you separate capabilities from tradeoffs. As you read, ask what each option is optimized for and what complexity you accept in exchange.",
    ],
    "workflow": [
        "The key to this section is sequence. If you can explain what happens first, what happens next, and where control moves after that, the moving parts here become much easier to reason about.",
        "Whenever a process has several stages, beginners benefit from tracing the handoff between them. Follow the order carefully and notice what information each step receives, transforms, and passes on.",
    ],
    "data": [
        "A useful beginner mental model here is to separate the shape of the data from the operations performed on it. Once you know what is being represented and who depends on that representation, the rules become easier to predict.",
        "If this section feels dense, pause and identify the data structure or model first. Most of the APIs here make more sense once you know what is being stored, queried, or transformed.",
    ],
    "security": [
        "Security topics become much easier to follow when you separate the threat from the defense. As you read, keep asking what can go wrong, what protection addresses it, and what assumption that protection depends on.",
        "A beginner-friendly way to approach this section is to pair each risk with the mechanism meant to reduce it. That keeps the advice grounded and helps you see why the defaults matter.",
    ],
    "testing": [
        "Treat this section as a feedback loop: define an expectation, exercise the behavior, compare the result, and use the difference to learn. That framing keeps testing ideas concrete instead of procedural.",
        "Testing concepts stick better when you remember the purpose behind each step: create evidence that the behavior you care about still works, and learn quickly when it stops working.",
    ],
    "performance": [
        "This topic is easier to understand if you split it into two questions: how do you notice a problem, and which lever changes it? Measurement comes first, optimization second, and mixing those steps usually creates confusion.",
        "Performance advice only becomes useful once you tie each technique to the bottleneck it addresses. Keep asking what is slow, how you can prove it, and what side effect each optimization introduces.",
    ],
    "deployment": [
        "The important beginner shift here is moving from “it works on my machine” to “it behaves predictably in a real environment.” Each step matters because it reduces surprises when the software runs elsewhere.",
        "Production-oriented material makes more sense when you see it as reliability work. The tools and steps here exist to make behavior repeatable, observable, and safer to change.",
    ],
    "api": [
        "When a section introduces a boundary between systems, focus on the contract first: what information crosses the boundary, who is allowed to send it, and what the caller can safely assume in return.",
        "API and integration material becomes easier when you treat it as agreement design rather than just endpoint syntax. Watch the shape of the data, the guarantees around it, and the failure cases.",
    ],
    "architecture": [
        "Architecture material sounds bigger than it is if you read it only as terminology. Start by identifying the responsibility of each part and the reason those responsibilities are separated; the structure usually becomes much clearer from there.",
        "A helpful beginner shortcut here is to ask why the system is split this way at all. Once the separation of responsibilities is clear, the patterns feel like practical decisions instead of abstract rules.",
    ],
    "debugging": [
        "Debugging-oriented sections are easiest to learn when you keep cause and evidence connected. Notice what symptom shows up first, what tool exposes it, and what the result tells you about the next step.",
        "When a topic involves troubleshooting, focus on the signals before the fixes. The more clearly you can read the evidence, the less likely you are to cargo-cult a solution.",
    ],
    "default": [
        "If this topic is new, keep translating each new term into a simple question: what job does it do, when would you reach for it, and what would you confuse it with if you were moving too quickly? That habit makes the section easier to retain.",
        "A first read goes better when you connect every new idea to a concrete responsibility and a concrete use case. Once those anchors are in place, the terminology in this section becomes much easier to reuse accurately.",
    ],
}


@dataclass(frozen=True)
class NotebookEntry:
    handbook: str
    path: Path
    relative_path: str
    chapter_number: int


@dataclass
class RewriteSummary:
    path: str
    changed: bool
    question_count: int
    intro_added: bool
    section_leads_added: int
    code_cells_created: int


def numeric_prefix(value: str) -> int:
    match = re.match(r"^\s*(\d+)", value)
    return int(match.group(1)) if match else sys.maxsize


def slugify(value: str) -> str:
    value = value.lower()
    value = NON_ALNUM_RE.sub("-", value)
    return value.strip("-")


def clean_heading_text(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = LEADING_NUMBER_RE.sub("", text)
    text = re.sub(r"[#*_>\[\]\(\)]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -:|")
    return text


def is_handbook_dir(path: Path) -> bool:
    return path.is_dir() and (path / "TOC.md").exists()


def ordered_handbooks(root: Path) -> list[str]:
    available = {path.name for path in root.iterdir() if is_handbook_dir(path)}
    ordered = [name for name in HANDBOOK_ORDER if name in available]
    ordered.extend(sorted(available - set(ordered)))
    return ordered


def discover_notebooks(root: Path, handbook: str) -> list[NotebookEntry]:
    handbook_dir = root / handbook
    entries: list[NotebookEntry] = []
    for path in handbook_dir.rglob("*.ipynb"):
        if not path.is_file():
            continue
        if ".ipynb_checkpoints" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        entries.append(
            NotebookEntry(
                handbook=handbook,
                path=path,
                relative_path=relative,
                chapter_number=numeric_prefix(path.name),
            )
        )
    entries.sort(key=lambda item: (item.chapter_number, item.relative_path))
    return entries


def run_git_show(root: Path, relative_path: str) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"HEAD:{relative_path}"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def load_json_from_text(text: str, label: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid notebook JSON in {label}: {exc}") from exc


def notebook_to_text(notebook: dict) -> str:
    return json.dumps(notebook, indent=1) + "\n"


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


def is_two_cell_nav_notebook(notebook: dict) -> bool:
    cells = notebook.get("cells", [])
    return (
        len(cells) == 2
        and all(cell.get("cell_type") == "markdown" for cell in cells)
        and is_nav_cell(cells[-1])
    )


def extract_headings(markdown: str) -> list[tuple[int, str]]:
    return [(len(match.group(1)), clean_heading_text(match.group(2))) for match in HEADING_RE.finditer(markdown)]


def choose_template(options: list[str], key: str) -> str:
    if not options:
        return ""
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    index = int(digest[:8], 16) % len(options)
    return options[index]


def classify_heading(heading: str) -> str:
    lowered = heading.lower()
    if any(token in lowered for token in ("install", "setup", "getting started", "configuration", "environment", "tooling")):
        return "setup"
    if any(token in lowered for token in ("what is", "introduction", "overview", "foundations", "fundamentals", "basics", "core concepts", "mental model")):
        return "concept"
    if any(token in lowered for token in (" vs ", "versus", "comparison", "choose", "tradeoff", "differences")):
        return "comparison"
    if any(token in lowered for token in ("lifecycle", "flow", "pipeline", "workflow", "routing", "request", "execution", "how it works")):
        return "workflow"
    if any(token in lowered for token in ("data", "database", "model", "schema", "orm", "query", "storage", "state", "cache")):
        return "data"
    if any(token in lowered for token in ("security", "auth", "authorization", "authentication", "permission", "csrf", "xss", "threat", "oauth", "jwt")):
        return "security"
    if any(token in lowered for token in ("test", "quality", "validation", "assert", "mock", "debug", "troubleshoot", "error handling")):
        return "testing" if "debug" not in lowered and "troubleshoot" not in lowered else "debugging"
    if any(token in lowered for token in ("performance", "scal", "optimiz", "profil", "observability", "monitoring", "latency", "throughput")):
        return "performance"
    if any(token in lowered for token in ("deployment", "production", "release", "operations", "ci", "cd", "container", "hosting", "day 2")):
        return "deployment"
    if any(token in lowered for token in ("api", "rest", "graphql", "websocket", "integration", "service", "messaging", "endpoint")):
        return "api"
    if any(token in lowered for token in ("architecture", "design", "pattern", "components", "module", "layer", "domain-driven")):
        return "architecture"
    return "default"


def build_question_inventory(topic: str, headings: list[tuple[int, str]]) -> list[str]:
    topic_name = topic or "this topic"
    questions = [
        f"What problem does {topic_name} solve?",
        f"Why does {topic_name} matter in real projects instead of only in examples?",
        f"When would I reach for {topic_name}, and when is it the wrong tool?",
        f"What is the smallest mental model I need before copying the examples in {topic_name}?",
        f"What mistakes or confusions usually trip beginners up in {topic_name}?",
    ]
    seen = {slugify(question) for question in questions}
    for _, heading in headings:
        if not heading:
            continue
        cleaned = heading.rstrip("?")
        candidates = [
            f"What does {cleaned} actually do?",
            f"How does {cleaned} fit into {topic_name}?",
            f"What would break if I misunderstood {cleaned}?",
        ]
        for question in candidates:
            key = slugify(question)
            if key and key not in seen:
                questions.append(question)
                seen.add(key)
            if len(questions) >= 12:
                return questions
    return questions[:12]


def preamble_has_intro(text: str) -> bool:
    sanitized_lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("<"):
            continue
        if stripped.startswith("---"):
            continue
        sanitized_lines.append(stripped)
    combined = " ".join(sanitized_lines)
    return len(combined) >= 120


def first_body_block(body: str) -> tuple[str, str]:
    text = body.lstrip("\n")
    if not text:
        return "empty", ""
    lines = text.splitlines()
    first = lines[0].strip()
    if first.startswith("```"):
        return "code", first
    if first.startswith(">"):
        return "quote", first
    if re.match(r"^[-*+]\s+", first) or re.match(r"^\d+\.\s+", first):
        return "list", first
    if first.startswith("|"):
        return "table", first
    if first.startswith("<"):
        return "html", first
    paragraph_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            break
        if stripped.startswith("```"):
            break
        if stripped.startswith("|") or stripped.startswith(">"):
            break
        if re.match(r"^[-*+]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            break
        paragraph_lines.append(stripped)
    paragraph = " ".join(paragraph_lines)
    return "paragraph", paragraph


def paragraph_is_dense(paragraph: str) -> bool:
    if len(paragraph) >= 430:
        return True
    if paragraph.count("`") >= 4:
        return True
    if paragraph.count("(") >= 4:
        return True
    acronyms = re.findall(r"\b[A-Z]{2,}\b", paragraph)
    if len(acronyms) >= 4:
        return True
    return False


def section_needs_lead(body: str) -> bool:
    block_type, payload = first_body_block(body)
    if block_type in {"empty", "code", "list", "table", "html"}:
        return True
    if block_type == "quote":
        return True
    if block_type == "paragraph":
        lowered = payload.lower()
        if lowered.startswith(
            (
                "before ",
                "this ",
                "these ",
                "in this ",
                "understanding ",
                "treat ",
                "think of ",
                "we ",
                "the goal ",
                "unlike ",
                "once ",
            )
        ):
            return False
        if len(payload) < 35:
            return True
        return paragraph_is_dense(payload)
    return False


def make_chapter_intro(topic: str) -> str:
    topic_key = slugify(topic) or "chapter"
    return choose_template(INTRO_TEMPLATES, topic_key)


def concept_from_heading(heading: str, chapter_topic: str) -> str:
    cleaned = clean_heading_text(heading) or chapter_topic or "this concept"
    if ":" in cleaned:
        left, right = [part.strip() for part in cleaned.split(":", 1)]
        left_slug = slugify(left)
        if right and left_slug in {"core-concepts", "chapter", "part", "section"}:
            cleaned = right
    lowered = cleaned.lower().rstrip("?")
    for pattern in (
        r"^what is\s+(.+)$",
        r"^why\s+(.+)$",
        r"^how\s+does\s+(.+?)\s+work$",
        r"^understanding\s+(.+)$",
        r"^introduction to\s+(.+)$",
        r"^overview of\s+(.+)$",
    ):
        match = re.match(pattern, lowered)
        if match:
            extracted = match.group(1).strip(" -:")
            if extracted:
                return extracted
    return cleaned


def make_section_lead(heading: str, chapter_topic: str) -> str:
    category = classify_heading(heading)
    concept = concept_from_heading(heading, chapter_topic)
    template = choose_template(SECTION_TEMPLATES.get(category, SECTION_TEMPLATES["default"]), f"{category}:{concept}")
    return template.format(concept=concept, topic=chapter_topic or "this topic")


def inject_chapter_intro(markdown: str, topic: str) -> tuple[str, bool]:
    matches = list(HEADING_RE.finditer(markdown))
    if not matches:
        return markdown, False
    title_match = matches[0]
    next_heading = matches[1] if len(matches) > 1 else None
    title_block_end = next_heading.start() if next_heading else len(markdown)
    title_block = markdown[title_match.end() : title_block_end]
    if preamble_has_intro(title_block):
        return markdown, False
    structural_offset = 0
    for line in title_block.splitlines(keepends=True):
        stripped = line.strip()
        if not stripped or stripped.startswith("<") or stripped.startswith("---"):
            structural_offset += len(line)
            continue
        break
    intro = make_chapter_intro(topic)
    insert_at = title_match.end() + structural_offset
    rebuilt = markdown[:insert_at].rstrip() + "\n\n" + intro + "\n\n" + markdown[insert_at:].lstrip("\n")
    return rebuilt, True


def rewrite_sections(markdown: str, chapter_topic: str) -> tuple[str, int]:
    matches = list(HEADING_RE.finditer(markdown))
    if not matches:
        return markdown, 0
    pieces: list[str] = []
    cursor = 0
    inserted = 0
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        section = markdown[start:end]
        if start > cursor:
            pieces.append(markdown[cursor:start])
        level = len(match.group(1))
        heading = clean_heading_text(match.group(2))
        if level < 2:
            pieces.append(section)
            cursor = end
            continue
        if any(token in heading.lower() for token in ("next up", "summary", "review", "conclusion", "takeaway")):
            pieces.append(section)
            cursor = end
            continue
        section_lines = section.splitlines()
        heading_line = section_lines[0]
        body = "\n".join(section_lines[1:])
        if section_needs_lead(body):
            lead = make_section_lead(heading, chapter_topic)
            rebuilt = heading_line.rstrip() + "\n\n" + lead + "\n\n"
            stripped_body = body.lstrip("\n")
            if stripped_body:
                rebuilt += stripped_body
                if section.endswith("\n") and not rebuilt.endswith("\n"):
                    rebuilt += "\n"
            pieces.append(rebuilt)
            inserted += 1
        else:
            pieces.append(section)
        cursor = end
    if cursor < len(markdown):
        pieces.append(markdown[cursor:])
    return "".join(pieces), inserted


def rewrite_markdown(markdown: str, chapter_path: str, *, allow_chapter_intro: bool) -> tuple[str, list[str], bool, int]:
    headings = extract_headings(markdown)
    title = next((text for level, text in headings if level == 1), clean_heading_text(Path(chapter_path).stem.replace("_", " ")))
    questions = build_question_inventory(title, headings)
    rewritten = markdown
    intro_added = False
    if allow_chapter_intro:
        rewritten, intro_added = inject_chapter_intro(markdown, title)
    rewritten, section_leads_added = rewrite_sections(rewritten, title)
    return rewritten, questions, intro_added, section_leads_added


def should_promote_code_block(info_string: str, code: str) -> bool:
    language = info_string.strip().split()[0].lower() if info_string.strip() else ""
    if language in {"text", "plaintext", "plain", "mermaid"}:
        return False
    if language:
        return True
    stripped = code.strip()
    if not stripped:
        return False
    return any(
        token in stripped
        for token in (
            "import ",
            "from ",
            "def ",
            "class ",
            "SELECT ",
            "INSERT ",
            "UPDATE ",
            "DELETE ",
            "{",
            "}",
            "=>",
            "console.",
            "pip ",
            "npm ",
            "docker ",
            "kubectl ",
            "python ",
            "$ ",
        )
    )


def make_markdown_cell(text: str) -> dict | None:
    normalized = text.strip("\n")
    if not normalized.strip():
        return None
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text_to_source(normalized + "\n"),
    }


def make_code_cell(code: str) -> dict:
    normalized = code
    if normalized and not normalized.endswith("\n"):
        normalized += "\n"
    return {
        "cell_type": "code",
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": text_to_source(normalized),
    }


def split_markdown_into_cells(markdown: str) -> tuple[list[dict], int]:
    cells: list[dict] = []
    buffer: list[str] = []
    created_code_cells = 0
    position = 0
    for match in FENCED_CODE_RE.finditer(markdown):
        buffer.append(markdown[position : match.start()])
        info_string = match.group(1).strip()
        code = match.group(2)
        full_block = match.group(0)
        if should_promote_code_block(info_string, code):
            markdown_cell = make_markdown_cell("".join(buffer))
            if markdown_cell is not None:
                cells.append(markdown_cell)
            buffer = []
            cells.append(make_code_cell(code))
            created_code_cells += 1
        else:
            buffer.append(full_block)
        position = match.end()
    buffer.append(markdown[position:])
    markdown_cell = make_markdown_cell("".join(buffer))
    if markdown_cell is not None:
        cells.append(markdown_cell)
    return cells, created_code_cells


def compare_notebooks(original: dict, current: dict, path: str) -> list[str]:
    problems: list[str] = []
    original_cells = original.get("cells", [])
    current_cells = current.get("cells", [])
    if original.get("metadata") != current.get("metadata"):
        problems.append(f"{path}: notebook metadata changed")
    if is_two_cell_nav_notebook(original):
        if not current_cells:
            problems.append(f"{path}: notebook has no cells after rewrite")
            return problems
        if not is_nav_cell(current_cells[-1]):
            problems.append(f"{path}: trailing nav cell missing after rewrite")
        else:
            if source_to_text(original_cells[-1].get("source")) != source_to_text(current_cells[-1].get("source")):
                problems.append(f"{path}: trailing nav cell content changed")
        for index, cell in enumerate(current_cells[:-1]):
            if cell.get("cell_type") not in {"markdown", "code"}:
                problems.append(f"{path}: cell {index} has unexpected type {cell.get('cell_type')}")
                continue
            if cell.get("cell_type") == "code":
                if cell.get("outputs") != []:
                    problems.append(f"{path}: generated code cell {index} has outputs")
                if cell.get("execution_count") is not None:
                    problems.append(f"{path}: generated code cell {index} has execution_count")
        disallowed = find_disallowed_headings(current)
        if disallowed:
            problems.append(f"{path}: disallowed heading(s) introduced: {', '.join(disallowed)}")
        return problems
    if len(original_cells) != len(current_cells):
        problems.append(f"{path}: cell count changed ({len(original_cells)} -> {len(current_cells)})")
        return problems
    original_nav = is_nav_cell(original_cells[-1]) if original_cells else False
    current_nav = is_nav_cell(current_cells[-1]) if current_cells else False
    if original_nav != current_nav:
        problems.append(f"{path}: trailing nav cell presence changed")
    if original_nav and current_nav:
        if source_to_text(original_cells[-1].get("source")) != source_to_text(current_cells[-1].get("source")):
            problems.append(f"{path}: trailing nav cell content changed")
    for index, (before, after) in enumerate(zip(original_cells, current_cells)):
        if before.get("cell_type") != after.get("cell_type"):
            problems.append(f"{path}: cell {index} type changed")
            continue
        if before.get("cell_type") == "code":
            if before.get("source") != after.get("source"):
                problems.append(f"{path}: code cell {index} source changed")
            if before.get("outputs") != after.get("outputs"):
                problems.append(f"{path}: code cell {index} outputs changed")
            if before.get("execution_count") != after.get("execution_count"):
                problems.append(f"{path}: code cell {index} execution_count changed")
            if before.get("metadata") != after.get("metadata"):
                problems.append(f"{path}: code cell {index} metadata changed")
    disallowed = find_disallowed_headings(current)
    if disallowed:
        problems.append(f"{path}: disallowed heading(s) introduced: {', '.join(disallowed)}")
    return problems


def find_disallowed_headings(notebook: dict) -> list[str]:
    matches: list[str] = []
    seen = set()
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        text = source_to_text(cell.get("source"))
        for heading_match in HEADING_RE.finditer(text):
            heading = clean_heading_text(heading_match.group(2)).lower()
            if heading in DISALLOWED_HEADINGS and heading not in seen:
                seen.add(heading)
                matches.append(heading)
    return matches


def rewrite_notebook(root: Path, entry: NotebookEntry) -> RewriteSummary:
    baseline_text = run_git_show(root, entry.relative_path)
    current_text = entry.path.read_text(encoding="utf-8")
    source_text = baseline_text or current_text
    notebook = load_json_from_text(source_text, entry.relative_path)
    original = load_json_from_text(source_text, entry.relative_path)
    cells = notebook.get("cells", [])
    if not cells:
        return RewriteSummary(entry.relative_path, False, 0, False, 0, 0)
    if is_two_cell_nav_notebook(notebook):
        main_text = source_to_text(cells[0].get("source"))
        rewritten, questions, intro_added, section_leads_added = rewrite_markdown(
            main_text,
            entry.relative_path,
            allow_chapter_intro=True,
        )
        rebuilt_cells, code_cells_created = split_markdown_into_cells(rewritten)
        if not rebuilt_cells:
            rebuilt_cells = [cells[0]]
        notebook["cells"] = rebuilt_cells + [cells[-1]]
        problems = compare_notebooks(original, notebook, entry.relative_path)
        if problems:
            raise ValueError("\n".join(problems))
        new_text = notebook_to_text(notebook)
        if new_text != current_text:
            entry.path.write_text(new_text, encoding="utf-8")
            return RewriteSummary(
                entry.relative_path,
                True,
                len(questions),
                intro_added,
                section_leads_added,
                code_cells_created,
            )
        return RewriteSummary(
            entry.relative_path,
            False,
            len(questions),
            intro_added,
            section_leads_added,
            code_cells_created,
        )
    rewritten_any = False
    intro_added = False
    section_leads_added = 0
    question_count = 0
    code_cells_created = 0
    first_markdown_index = next(
        (
            index
            for index, cell in enumerate(cells)
            if cell.get("cell_type") == "markdown" and not (index == len(cells) - 1 and is_nav_cell(cell))
        ),
        None,
    )
    for index, cell in enumerate(cells):
        if cell.get("cell_type") != "markdown":
            continue
        if index == len(cells) - 1 and is_nav_cell(cell):
            continue
        text = source_to_text(cell.get("source"))
        rewritten, questions, cell_intro_added, cell_section_leads = rewrite_markdown(
            text,
            entry.relative_path,
            allow_chapter_intro=index == first_markdown_index,
        )
        question_count = max(question_count, len(questions))
        intro_added = intro_added or cell_intro_added
        section_leads_added += cell_section_leads
        if rewritten != text:
            cell["source"] = text_to_source(rewritten)
            rewritten_any = True
    if not rewritten_any:
        return RewriteSummary(entry.relative_path, False, question_count, intro_added, section_leads_added, code_cells_created)
    problems = compare_notebooks(original, notebook, entry.relative_path)
    if problems:
        raise ValueError("\n".join(problems))
    new_text = notebook_to_text(notebook)
    if new_text != current_text:
        entry.path.write_text(new_text, encoding="utf-8")
        return RewriteSummary(entry.relative_path, True, question_count, intro_added, section_leads_added, code_cells_created)
    return RewriteSummary(entry.relative_path, False, question_count, intro_added, section_leads_added, code_cells_created)


def extract_toc_paths(root: Path, handbook: str) -> list[str]:
    toc_path = root / handbook / "TOC.md"
    if not toc_path.exists():
        return []
    links = TOC_LINK_RE.findall(toc_path.read_text(encoding="utf-8"))
    return [f"{handbook}/{link.replace('%20', ' ')}" for link in links]


def inventory_command(root: Path) -> int:
    print("handbook\tchapters\tmixed\tlong_markdown\ttoc_links\torder_mismatch")
    for handbook in ordered_handbooks(root):
        notebooks = discover_notebooks(root, handbook)
        mixed = 0
        long_markdown = 0
        for entry in notebooks:
            notebook = load_json_from_text(entry.path.read_text(encoding="utf-8"), entry.relative_path)
            cells = notebook.get("cells", [])
            if any(cell.get("cell_type") == "code" for cell in cells):
                mixed += 1
            if len(cells) == 2 and all(cell.get("cell_type") == "markdown" for cell in cells):
                body = source_to_text(cells[0].get("source"))
                if len(body) >= 20000:
                    long_markdown += 1
        toc_paths = extract_toc_paths(root, handbook)
        notebook_paths = [entry.relative_path for entry in notebooks]
        order_mismatch = toc_paths and toc_paths != notebook_paths[: len(toc_paths)]
        print(
            f"{handbook}\t{len(notebooks)}\t{mixed}\t{long_markdown}\t{len(toc_paths)}\t"
            f"{'yes' if order_mismatch else 'no'}"
        )
    return 0


def rewrite_command(root: Path, handbook: str) -> int:
    notebooks = discover_notebooks(root, handbook)
    if not notebooks:
        print(f"No notebooks found for handbook '{handbook}'.", file=sys.stderr)
        return 1
    summaries = [rewrite_notebook(root, entry) for entry in notebooks]
    changed = [item for item in summaries if item.changed]
    print(
        f"{handbook}: rewritten {len(changed)}/{len(summaries)} notebooks; "
        f"chapter intros added in {sum(1 for item in summaries if item.intro_added)}; "
        f"section leads added={sum(item.section_leads_added for item in summaries)}; "
        f"code cells created={sum(item.code_cells_created for item in summaries)}"
    )
    samples = choose_representative_entries(notebooks)
    if samples:
        print("spot-check sample notebooks:")
        for sample in samples:
            print(f"  - {sample.relative_path}")
    return 0


def choose_representative_entries(notebooks: list[NotebookEntry]) -> list[NotebookEntry]:
    if not notebooks:
        return []
    indices = {0, len(notebooks) // 2, len(notebooks) - 1}
    mixed_index = None
    for index, entry in enumerate(notebooks):
        notebook = load_json_from_text(entry.path.read_text(encoding="utf-8"), entry.relative_path)
        if any(cell.get("cell_type") == "code" for cell in notebook.get("cells", [])):
            mixed_index = index
            break
    if mixed_index is not None:
        indices.add(mixed_index)
    return [notebooks[index] for index in sorted(indices)]


def validate_notebook(root: Path, entry: NotebookEntry) -> list[str]:
    baseline_text = run_git_show(root, entry.relative_path)
    if baseline_text is None:
        return [f"{entry.relative_path}: missing git baseline; cannot validate against HEAD"]
    current_text = entry.path.read_text(encoding="utf-8")
    original = load_json_from_text(baseline_text, f"HEAD:{entry.relative_path}")
    current = load_json_from_text(current_text, entry.relative_path)
    return compare_notebooks(original, current, entry.relative_path)


def validate_command(root: Path, handbook: str) -> int:
    notebooks = discover_notebooks(root, handbook)
    if not notebooks:
        print(f"No notebooks found for handbook '{handbook}'.", file=sys.stderr)
        return 1
    problems = []
    for entry in notebooks:
        problems.extend(validate_notebook(root, entry))
    if problems:
        print(f"{handbook}: validation failed")
        for problem in problems[:50]:
            print(f"  - {problem}")
        if len(problems) > 50:
            print(f"  ... and {len(problems) - 50} more")
        return 1
    samples = choose_representative_entries(notebooks)
    print(f"{handbook}: validation passed for {len(notebooks)} notebooks")
    if samples:
        print("validated sample notebooks:")
        for sample in samples:
            print(f"  - {sample.relative_path}")
    return 0


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rewrite handbook notebooks for first-time learners.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("inventory", help="List handbook inventory and notebook shape information.")

    rewrite_parser = subparsers.add_parser("rewrite", help="Rewrite one handbook's notebooks in-place.")
    rewrite_parser.add_argument("--handbook", required=True, help="Handbook directory name.")

    validate_parser = subparsers.add_parser("validate", help="Validate rewritten notebooks against git HEAD.")
    validate_parser.add_argument("--handbook", required=True, help="Handbook directory name.")

    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    root = Path.cwd()
    if not (root / "README.md").exists():
        print("Run this utility from the repository root.", file=sys.stderr)
        return 1
    if args.command == "inventory":
        return inventory_command(root)
    if args.command == "rewrite":
        return rewrite_command(root, args.handbook)
    if args.command == "validate":
        return validate_command(root, args.handbook)
    print(f"Unknown command: {args.command}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
