#!/usr/bin/env python3
"""Fix multiple issues across 19 Flask Jupyter notebooks."""

import json
import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))

NOTEBOOKS = [
    "1. flask_foundations/1. getting_started.ipynb",
    "1. flask_foundations/2. routing_and_url_building.ipynb",
    "1. flask_foundations/3. templates_with_jinja2.ipynb",
    "2. working_with_data/4. handling_forms_and_user_input.ipynb",
    "2. working_with_data/5. sessions_and_cookies.ipynb",
    "2. working_with_data/6. databases_with_flask_sqlalchemy.ipynb",
    "2. working_with_data/7. database_migrations_with_flask_migrate.ipynb",
    "3. application_structure/8. blueprints_and_application_factory.ipynb",
    "3. application_structure/9. configuration_management.ipynb",
    "4. authentication_and_security/10. user_authentication_with_flask_login.ipynb",
    "4. authentication_and_security/11. security_best_practices.ipynb",
    "5. building_apis/12. building_rest_apis.ipynb",
    "5. building_apis/13. api_authentication_with_jwt.ipynb",
    "6. advanced_features/14. file_uploads_and_static_assets.ipynb",
    "6. advanced_features/15. error_handling_and_logging.ipynb",
    "6. advanced_features/16. testing_flask_applications.ipynb",
    "7. deployment_and_production/17. caching_and_performance.ipynb",
    "7. deployment_and_production/18. deployment.ipynb",
    "8. capstone_project/19. building_a_fullstack_flask_blog.ipynb",
]

BOILERPLATE = [
    "A first read goes better when you connect every new idea to a concrete responsibility and a concrete use case. Once those anchors are in place, the terminology in this section becomes much easier to reuse accurately.",
    "If this section feels dense, pause and identify the data structure or model first. Most of the APIs here make more sense once you know what is being stored, queried, or transformed.",
    "Architecture material sounds bigger than it is if you read it only as terminology. Start by identifying the responsibility of each part and the reason those responsibilities are separated; the structure usually becomes much clearer from there.",
    "Whenever a process has several stages, beginners benefit from tracing the handoff between them. Follow the order carefully and notice what information each step receives, transforms, and passes on.",
    "Sections like this become clearer when you separate capabilities from tradeoffs. As you read, ask what each option is optimized for and what complexity you accept in exchange.",
    "Debugging-oriented sections are easiest to learn when you keep cause and evidence connected. Notice what symptom shows up first, what tool exposes it, and what the result tells you about the next step.",
    "A beginner-friendly way to approach this section is to pair each risk with the mechanism meant to reduce it. That keeps the advice grounded and helps you see why the defaults matter.",
    "A useful beginner mental model here is to separate the shape of the data from the operations performed on it. Once you know what is being represented and who depends on that representation, the rules become easier to predict.",
    "Setup steps are easier to remember when you know what each one unlocks. Read this section as a map from each command, option, or file to the problem it solves, so later errors are easier to diagnose instead of feeling random.",
    "The hard part here is usually not the syntax but the boundary between similar ideas. ",  # trailing space
    "Security topics become much easier to follow when you separate the threat from the defense. As you read, keep asking what can go wrong, what protection addresses it, and what assumption that protection depends on.",
]


def remove_boilerplate(text):
    """Remove all boilerplate phrases from text and clean up blank lines."""
    for bp in BOILERPLATE:
        text = text.replace(bp, "")
    # Collapse 3+ consecutive blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Strip trailing whitespace from each line
    lines = text.split("\n")
    lines = [l.rstrip() for l in lines]
    text = "\n".join(lines)
    # Remove trailing blank lines but keep one trailing newline if original had it
    text = text.rstrip("\n")
    return text


def get_source(cell):
    return "".join(cell["source"])


def set_source(cell, text):
    cell["source"] = text


def is_heading_only(text):
    """Return True if after stripping, text is a single heading line."""
    stripped = text.strip()
    lines = [l for l in stripped.split("\n") if l.strip()]
    return len(lines) == 1 and lines[0].startswith("#")


# ─── Task 1: Remove boilerplate from all notebooks ─────────────────────────

def task1_remove_boilerplate(nb):
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            src = get_source(cell)
            cleaned = remove_boilerplate(src)
            if cleaned != src:
                set_source(cell, cleaned)
    return nb


# ─── Task 2: Fix specific cells ────────────────────────────────────────────

SESSIONS_REPLACEMENTS = {
    # Cell 6: heading "### The `session` Object Behaves Like a Python Dict"
    6: "### The `session` Object Behaves Like a Python Dict\n\nFlask's `session` works exactly like a Python dict — get, set, delete with the same syntax you already know. The key difference: Flask tracks modifications automatically and re-serializes the updated session into the cookie on every response.",
    # Cell 11: heading "### Session Lifetime and Permanence — The 'Remember Me' Pattern"
    11: "### Session Lifetime and Permanence — The 'Remember Me' Pattern\n\nBy default a session lasts as long as the browser window is open (a *browser session cookie* — no expiry date). Setting `session.permanent = True` tells Flask to set an explicit expiry date on the cookie, controlled by `PERMANENT_SESSION_LIFETIME`. This is the server-side half of the \"Remember Me\" feature.",
    # Cell 13: heading "### Raw Cookies — The Lower-Level Mechanism"
    13: "### Raw Cookies — The Lower-Level Mechanism\n\nFlask's `session` is the right choice for auth state. But for simple, non-sensitive preferences — theme, language, items-per-page — you can skip the overhead of signed sessions and write a raw cookie directly with `response.set_cookie()`. Raw cookies are plain text in the browser, so never put sensitive data in them.",
    # Cell 15: heading "### ⚖️ Sessions vs Raw Cookies vs Server-Side Sessions"
    15: "### ⚖️ Sessions vs Raw Cookies vs Server-Side Sessions\n\nWhich storage mechanism is right for your use case? The table below compares the three options on the dimensions that matter most:",
    # Cell 17: heading "### Complete Login/Logout Flow with Sessions"
    17: "### Complete Login/Logout Flow with Sessions\n\nThe full login flow passes through several steps. Follow the data — the user ID — as it travels from login form → session cookie → each subsequent request → logout:",
    # Cell 30: heading "### Session-Based Flash Messages Deep Dive"
    30: "### Session-Based Flash Messages Deep Dive\n\nFlash messages are a one-time-read pattern built on top of the session: Flask stores messages in the session, and `get_flashed_messages()` reads and **removes** them in a single call. This means a flash message is shown exactly once, then gone — perfect for \"Post saved!\" or \"Login successful\" feedback.",
}


def task2_fix_sessions(nb):
    for idx, new_text in SESSIONS_REPLACEMENTS.items():
        cell = nb["cells"][idx]
        assert cell["cell_type"] == "markdown", f"Cell {idx} is not markdown"
        set_source(cell, new_text)
    return nb


# Introductions for handling_forms heading-only cells after boilerplate removal
FORMS_INTROS = {
    6: "### Safe vs Unsafe Field Access — A Critical Distinction\n\n`request.form['key']` raises a `KeyError` if the field is missing; `request.form.get('key')` returns `None`. Choosing the wrong accessor is one of the most common sources of 400 errors in Flask form handling.",
    14: "### ⚖️ Manual vs Flask-WTF — Side-by-Side Comparison\n\nManual forms require less setup but put validation and CSRF protection entirely on you. Flask-WTF adds a thin layer of boilerplate in exchange for automatic CSRF tokens, clean field definitions, and reusable validators.",
    16: "### All WTForms Field Types and Validators at a Glance\n\nWTForms ships with field types for every common HTML input and a library of validators you can chain together. The table below is your quick reference for picking the right field and validator combination.",
    18: "### Flash Messages — One-Time Feedback That Survives Redirects\n\nAfter a form submission you typically redirect rather than render directly (Post/Redirect/Get pattern). Flash messages let you carry a one-time status string — \"Saved!\", \"Invalid password\" — across that redirect so the user sees feedback on the next page.",
    22: "### What If 2: The CSRF Token is Missing or Invalid?\n\nFlask-WTF rejects any POST without a valid CSRF token with a 400 error. This usually means the hidden `{{ form.hidden_tag() }}` is absent from your template, the form was submitted from a different origin, or the session expired.",
    27: "## 📋 Chapter Summary & Cheat Sheet\n\nThe key patterns from this chapter — manual form parsing, Flask-WTF validation, CSRF protection, and flash messages — are summarised below for quick reference.",
    29: "### SelectField and Multi-Choice Fields\n\n`SelectField` renders an HTML `<select>` and validates that the submitted value is one of the allowed choices. `SelectMultipleField` works the same way but accepts a list of selected values.",
    31: "### File Upload Handling\n\nFile uploads require `enctype=\"multipart/form-data\"` on the HTML form and `request.files` (not `request.form`) on the server. Always validate the filename with `secure_filename()` and check the extension before saving.",
    35: "### Form Customization: HTML Attributes and Macros\n\nWTForms fields accept `render_kw` to inject arbitrary HTML attributes (`class`, `placeholder`, `id`). For consistent styling across many forms, a Jinja2 macro lets you render any field with your design system's markup in a single call.",
}


def task2_fix_forms(nb):
    for idx, new_text in FORMS_INTROS.items():
        cell = nb["cells"][idx]
        assert cell["cell_type"] == "markdown", f"Cell {idx} is not markdown"
        current = get_source(cell).strip()
        # Only set if the cell is heading-only (or blank) after boilerplate removal
        if is_heading_only(current) or not current:
            set_source(cell, new_text)
    return nb


def task2_fix_user_auth(nb):
    """Fix cell 17 of user_authentication_with_flask_login.ipynb."""
    cell = nb["cells"][17]
    assert cell["cell_type"] == "markdown"
    src = get_source(cell)
    # Remove both occurrences of the boilerplate phrase (with trailing space)
    bp = "The hard part here is usually not the syntax but the boundary between similar ideas. "
    src = src.replace(bp, "")
    # Clean up any extra blank lines that result
    src = re.sub(r"\n{3,}", "\n\n", src)
    set_source(cell, src)
    return nb


# ─── Task 3: Fix code fence language in templates_with_jinja2.ipynb ────────

def task3_fix_code_fences(nb):
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            src = get_source(cell)
            # Cell 1: json fence with ASCII diagram
            if "Python data  ──►  Jinja2 engine" in src:
                src = src.replace("```json\nPython data", "```text\nPython data")
                set_source(cell, src)
            # Cell 7: json fence with Jinja2 filter examples
            if "{{ name | upper }}" in src and "```json" in src:
                # Replace the first ```json that precedes the filter examples
                src = src.replace("```json\n{{ name | upper }}", "```text\n{{ name | upper }}")
                set_source(cell, src)
    return nb


# ─── Task 4: Content improvements in getting_started.ipynb ─────────────────

def task4_fix_getting_started(nb):
    cells = nb["cells"]

    # Cell 3: Replace installation section text
    cell3 = cells[3]
    src3 = get_source(cell3)
    old_install_text = "Flask lives on PyPI. Install it (ideally inside a virtual environment) with:"
    new_install_intro = (
        "A **virtual environment** is an isolated Python installation for your project — "
        "it keeps your project's packages separate from your system Python and from other projects. "
        "Without one, every project would share the same global packages, leading to version conflicts. "
        "Always create one before installing project dependencies.\n\n"
        "Flask lives on PyPI. Install it inside a virtual environment:"
    )
    if old_install_text in src3:
        src3 = src3.replace(old_install_text, new_install_intro)
        set_source(cell3, src3)

    # Cell 5: Insert decorator tip after the numbered list
    cell5 = cells[5]
    src5 = get_source(cell5)
    # The numbered list ends after "4. **Return** a response string from that function"
    # We need to insert the tip after the list but before any code block or next heading
    decorator_tip = (
        "\n> 💡 **What is a decorator?** A decorator is Python syntax using `@` that wraps a function "
        "with extra behavior — without changing the function itself. `@app.route('/')` tells Flask: "
        "*\"Register the function below for the URL `/`.*\" You'll see decorators constantly in Flask code."
    )
    target = "4. **Return** a response string from that function"
    if target in src5 and "What is a decorator?" not in src5:
        # Find the end of the numbered list item
        insert_pos = src5.index(target) + len(target)
        src5 = src5[:insert_pos] + decorator_tip + src5[insert_pos:]
        set_source(cell5, src5)

    # Cell 19: Add context intro before the table
    cell19 = cells[19]
    src19 = get_source(cell19)
    context_intro = (
        "Flask uses two **context** types to make objects available to your code without passing them as arguments:\n\n"
        "- **Application context** — active whenever Flask is processing anything (startup, requests, CLI commands). "
        "Provides access to the app configuration and `g` (per-request scratch space).\n"
        "- **Request context** — pushed on top of the app context for every incoming HTTP request. "
        "Provides `request` (the current HTTP request) and `session` (the user's signed cookie data).\n\n"
    )
    # Insert before the table (which starts with "| Object |")
    table_marker = "| Object | Context | What it holds |"
    if table_marker in src19 and "Application context" not in src19:
        src19 = src19.replace(table_marker, context_intro + table_marker)
        set_source(cell19, src19)

    return nb


# ─── Main ───────────────────────────────────────────────────────────────────

def load_nb(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_nb(nb, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
        f.write("\n")


def process_notebook(rel_path):
    path = os.path.join(BASE, rel_path)
    nb = load_nb(path)

    # Task 1: Remove boilerplate from all notebooks
    nb = task1_remove_boilerplate(nb)

    # Task 2: File-specific fixes
    fname = os.path.basename(rel_path)
    if fname == "5. sessions_and_cookies.ipynb":
        nb = task2_fix_sessions(nb)
    elif fname == "4. handling_forms_and_user_input.ipynb":
        nb = task2_fix_forms(nb)
    elif fname == "10. user_authentication_with_flask_login.ipynb":
        nb = task2_fix_user_auth(nb)

    # Task 3: Fix code fence languages
    if fname == "3. templates_with_jinja2.ipynb":
        nb = task3_fix_code_fences(nb)

    # Task 4: Content improvements
    if fname == "1. getting_started.ipynb":
        nb = task4_fix_getting_started(nb)

    save_nb(nb, path)
    print(f"  ✓ {rel_path}")


if __name__ == "__main__":
    print("Processing notebooks...")
    for nb_path in NOTEBOOKS:
        process_notebook(nb_path)
    print("\nDone.")
