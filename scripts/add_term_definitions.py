#!/usr/bin/env python3
"""Add term definitions to specific notebooks (Part 2 of handbook improvement)."""
import json
from pathlib import Path

ROOT = Path("/media/ankit/Programming/Projects/Dev-Handbook")


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save(nb, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)


def text_of(cell):
    return "".join(cell["source"])


def set_source(cell, text):
    """Re-split text into lines, each ending with \\n except the last."""
    lines = text.split("\n")
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + "\n")
        else:
            result.append(line)
    cell["source"] = result


# ─────────────────────────────────────────────────────────────────────────────
# 2A: FastAPI Chapter 1 — setting_up_the_development_environment.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_fastapi_ch1():
    path = ROOT / "fastapi/1. foundations_of_fastapi/1. setting_up_the_development_environment.ipynb"
    nb = load(path)

    # Cell 3: Core Concepts — append WSGI vs ASGI, type hints, OpenAPI/Swagger
    cell = nb["cells"][3]
    current = text_of(cell)
    addition = """
### WSGI vs ASGI: why FastAPI requires ASGI

**WSGI** (Web Server Gateway Interface) is the older Python web standard. It handles one request at a time per worker — each request runs synchronously to completion before the next one starts. Traditional frameworks like Django and Flask default to WSGI, and servers like Gunicorn speak it natively.

**ASGI** (Asynchronous Server Gateway Interface) is its modern, async-capable successor. A single ASGI worker can handle multiple concurrent requests, WebSocket connections, and long-polling without blocking. FastAPI is built around Python's `async/await` model and **requires** an ASGI server like Uvicorn.

> ❓ **Can I run FastAPI behind plain Gunicorn?** Only if you use `uvicorn.workers.UvicornWorker`, which makes each Gunicorn worker an ASGI worker. Using Gunicorn's default WSGI workers with FastAPI will produce incorrect behaviour.

### Type hints

**Type hints** are Python's built-in syntax for annotating the expected type of a variable or parameter:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

FastAPI reads type hints on every route parameter and Pydantic model field to parse requests, validate input, and generate documentation — all automatically. When you write `def create_item(item: Item)`, FastAPI already knows the expected JSON shape.

### OpenAPI and interactive docs

**OpenAPI** is a standard format for describing HTTP APIs — their endpoints, parameters, request/response shapes, and authentication. FastAPI generates an OpenAPI specification from your code automatically.

That spec is served as interactive documentation at two URLs:

- `/docs` — Swagger UI (try real requests from the browser)
- `/redoc` — ReDoc (clean reading format)

Your code and your API docs stay in sync without any extra effort."""

    set_source(cell, current + addition)
    save(nb, path)
    print("2A: FastAPI Ch1 — Cell 3 updated (WSGI/ASGI, type hints, OpenAPI)")


# ─────────────────────────────────────────────────────────────────────────────
# 2B: FastAPI Chapter 6 — dependency_injection_system.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_fastapi_ch6():
    path = ROOT / "fastapi/3. core_fastapi_concepts/6. dependency_injection_system.ipynb"
    nb = load(path)

    # Cell 1: intro — add formal DI definition after the first sentence
    cell = nb["cells"][1]
    current = text_of(cell)
    old = (
        "Dependency injection sounds like a scary architecture phrase, "
        "but the beginner version is simple: **instead of every route building "
        "its own tools, FastAPI hands the route the tools it asked for**."
    )
    new = (
        "Dependency injection sounds like a scary architecture phrase, "
        "but the beginner version is simple: **instead of every route building "
        "its own tools, FastAPI hands the route the tools it asked for**.\n\n"
        "**Dependency injection** (DI) is a design pattern where a function or class "
        "declares what it needs (its dependencies), and an external system provides them "
        "— rather than the function building them itself. In FastAPI, that external "
        "system is the framework: you declare `Depends(some_function)`, FastAPI calls "
        "the function, manages its lifetime, and passes the result into your route."
    )
    set_source(cell, current.replace(old, new, 1))
    save(nb, path)
    print("2B: FastAPI Ch6 — Cell 1 updated (formal DI definition)")


# ─────────────────────────────────────────────────────────────────────────────
# 2C: FastAPI Chapter 11 — security_fundamentals.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_fastapi_ch11():
    path = ROOT / "fastapi/5. security_and_authentication/11. security_fundamentals.ipynb"
    nb = load(path)

    # Cell 3: Core Concepts — add brief Middleware definition at the end
    cell = nb["cells"][3]
    current = text_of(cell)
    addition = """
### Middleware (brief introduction)

**Middleware** is code that runs before and/or after every request, regardless of which route handles it. A middleware layer can inspect or modify the incoming request before your route sees it, and can inspect or modify the outgoing response before it reaches the client.

FastAPI's CORS support, GZip compression, and HTTPS-redirect helpers all work as middleware. Full coverage is in the middleware chapter — for now, just know that security often involves adding middleware layers."""

    set_source(cell, current + addition)
    save(nb, path)
    print("2C: FastAPI Ch11 — Cell 3 updated (Middleware brief definition)")


# ─────────────────────────────────────────────────────────────────────────────
# 2D: FastAPI Chapter 12 — oauth2_and_jwt.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_fastapi_ch12():
    path = ROOT / "fastapi/5. security_and_authentication/12. oauth2_and_jwt.ipynb"
    nb = load(path)

    # Cell 3: Core Concepts — add OAuth2 as authorization protocol clarification
    cell3 = nb["cells"][3]
    current3 = text_of(cell3)
    old3 = "### OAuth2 password flow\n\nThe password flow is a login pattern where:"
    new3 = (
        "### OAuth2 password flow\n\n"
        "**OAuth2** is an **authorization protocol** — not an authentication system "
        "itself. Its primary role in the wider ecosystem is to delegate access between "
        "services (\"Login with Google,\" \"Connect with GitHub\"), but the **password "
        "flow** used in this chapter is a simplified form intended for first-party apps "
        "where you own both the client and the server. It uses the same token "
        "infrastructure as broader OAuth2, making the patterns transferable.\n\n"
        "The password flow is a login pattern where:"
    )
    set_source(cell3, current3.replace(old3, new3, 1))

    # Cell 4: Syntax & First Usage — add Bearer token definition
    cell4 = nb["cells"][4]
    current4 = text_of(cell4)
    old4 = (
        "Then you use `Depends(oauth2_scheme)` to read the token string from the "
        "`Authorization: Bearer ...` header."
    )
    new4 = (
        "Then you use `Depends(oauth2_scheme)` to read the token string from the "
        "`Authorization: Bearer ...` header.\n\n"
        "> 🔑 **What does \"Bearer\" mean?** A **Bearer token** grants access to whoever "
        "holds (bears) it — any client presenting a valid token is granted the request. "
        "Unlike a credential tied to a specific user agent, the token itself is the "
        "proof of access. This is why bearer tokens must be transmitted only over "
        "HTTPS and must never be logged or stored carelessly."
    )
    set_source(cell4, current4.replace(old4, new4, 1))

    # Cell 7: JWT deep dive — strengthen the Base64url / no-encryption note
    cell7 = nb["cells"][7]
    current7 = text_of(cell7)
    old7 = (
        "Important beginner note: the payload is usually **encoded**, not magically "
        "hidden from the world. Do not put sensitive secrets inside a JWT just because "
        "it looks scrambled."
    )
    new7 = (
        "Important beginner note: the payload is **Base64url-encoded**, not encrypted. "
        "Anyone who intercepts the token string can decode and read the payload with a "
        "single command — no key required. The signature verifies that the token was "
        "issued by your server and has not been tampered with, but it provides "
        "**no confidentiality**. Never put passwords, API secrets, or sensitive personal "
        "data in the JWT payload."
    )
    set_source(cell7, current7.replace(old7, new7, 1))

    save(nb, path)
    print("2D: FastAPI Ch12 — Cells 3, 4, 7 updated (OAuth2 protocol, Bearer token, Base64url)")


# ─────────────────────────────────────────────────────────────────────────────
# 2E: Django Chapter 5 — django_architecture_overview.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_django_ch5():
    path = ROOT / "django/1. Foundations/5. django_architecture_overview.ipynb"
    nb = load(path)

    # Cell 0: Add WSGI vs ASGI section after the MTV section
    cell = nb["cells"][0]
    current = text_of(cell)
    # The MTV section ends just before "**Model** (later chapters, preview only):"
    old = "### 5.2.1 A minimal MTV example (with clear mapping)\n\n**Model** (later chapters, preview only):"
    new = (
        "### 5.2.1 A minimal MTV example (with clear mapping)\n\n"
        "**Model** (later chapters, preview only):"
    )
    # Add WSGI vs ASGI section right after the MTV explanation, before 5.2.1
    wsgi_asgi = (
        "\n### WSGI vs ASGI: Django's Two Deployment Standards\n\n"
        "Django supports two standards for connecting a Python web app to a server.\n\n"
        "**WSGI** (Web Server Gateway Interface) is the older, synchronous standard. "
        "Each request is handled by one worker process to completion before the next "
        "request starts. This works well for typical HTML apps and standard JSON APIs. "
        "Gunicorn and uWSGI are common WSGI servers.\n\n"
        "**ASGI** (Asynchronous Server Gateway Interface) is the modern standard. It "
        "supports async views, WebSocket connections, long-polling, and handling many "
        "concurrent connections within a single process. ASGI is required for Django "
        "Channels (WebSockets) and for async views. Uvicorn and Daphne are common "
        "ASGI servers.\n\n"
        "For most classic Django projects, WSGI is perfectly adequate. "
        "Choose ASGI when you need real-time features or heavily async request handling.\n\n"
    )
    insertion_point = "### 5.2.1 A minimal MTV example"
    set_source(cell, current.replace(insertion_point, wsgi_asgi + insertion_point, 1))

    save(nb, path)
    print("2E: Django Ch5 — Cell 0 updated (WSGI vs ASGI, MTV already well defined)")


# ─────────────────────────────────────────────────────────────────────────────
# 2F: Django Chapter 8 — models_and_database_basics.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_django_ch8():
    path = ROOT / "django/2. Core_Django/8. models_and_database_basics.ipynb"
    nb = load(path)

    # Cell 0: Expand section 8.3 to include ORM definition
    cell = nb["cells"][0]
    current = text_of(cell)
    old = (
        "## 8.3 What a Django Model Is (and what it contains)\n\n"
        "A Django model is a Python class that:\n"
        "- defines fields (schema)\n"
        "- provides query API via the ORM\n"
        "- can include behavior (methods)\n"
        "- participates in validation and constraints\n\n"
        "**Key mental model:**\n"
        "- Models are not just schema; they are your *domain objects* + persistence mapping."
    )
    new = (
        "## 8.3 What a Django Model Is (and what it contains)\n\n"
        "A Django model is a Python class that:\n"
        "- defines fields (schema)\n"
        "- provides query API via the ORM\n"
        "- can include behavior (methods)\n"
        "- participates in validation and constraints\n\n"
        "#### What is the ORM?\n\n"
        "**ORM** stands for **Object Relational Mapper**. It is a tool that lets you "
        "interact with a relational database using Python objects and methods instead "
        "of writing raw SQL. Django's ORM translates Python code like "
        "`Article.objects.filter(status='published')` into SQL queries behind the scenes.\n\n"
        "This means you can build most database operations without writing SQL, and "
        "your code stays largely database-agnostic — switching from SQLite to PostgreSQL "
        "rarely requires rewriting your queries.\n\n"
        "**Key mental model:**\n"
        "- Models are not just schema; they are your *domain objects* + persistence mapping."
    )
    set_source(cell, current.replace(old, new, 1))

    # Cell 4: Migrations section — add crisp migration definition at the start of 8.6
    cell4 = nb["cells"][4]
    current4 = text_of(cell4)
    old4 = (
        "## 8.6 Migrations (How Django Changes the Database Safely)\n\n"
        "A useful beginner mental model here is to separate the shape of the data from the operations performed on it. Once you know what is being represented and who depends on that representation, the rules become easier to predict.\n\n"
        "### 8.6.1 What a migration is\n"
        "A migration is a versioned, replayable set of operations:"
    )
    new4 = (
        "## 8.6 Migrations (How Django Changes the Database Safely)\n\n"
        "### 8.6.1 What a migration is\n\n"
        "A **migration** is a version-controlled change to your database schema. "
        "Each `makemigrations` run creates a Python file in your app's `migrations/` "
        "folder describing the schema changes; `migrate` applies those files to the "
        "actual database. This keeps your database schema in sync with your models "
        "across all environments (local, staging, production).\n\n"
        "Migrations are tracked in your codebase and applied to databases in order. "
        "**Industry reality:** migrations are as important as code — "
        "they are part of your deployment process.\n\n"
        "A migration file records a versioned, replayable set of operations:"
    )
    # Only replace if the exact old string is found
    if old4 in current4:
        set_source(cell4, current4.replace(old4, new4, 1))
    else:
        # Try without the boilerplate line (already removed by part 1)
        old4b = (
            "## 8.6 Migrations (How Django Changes the Database Safely)\n\n"
            "### 8.6.1 What a migration is\n"
            "A migration is a versioned, replayable set of operations:"
        )
        new4b = (
            "## 8.6 Migrations (How Django Changes the Database Safely)\n\n"
            "### 8.6.1 What a migration is\n\n"
            "A **migration** is a version-controlled change to your database schema. "
            "Each `makemigrations` run creates a Python file in your app's `migrations/` "
            "folder describing the schema changes; `migrate` applies those files to the "
            "actual database. This keeps your database schema in sync with your models "
            "across all environments (local, staging, production).\n\n"
            "**Industry reality:** migrations are as important as code — "
            "they are part of your deployment process.\n\n"
            "A migration file records a versioned, replayable set of operations:"
        )
        set_source(cell4, current4.replace(old4b, new4b, 1))

    save(nb, path)
    print("2F: Django Ch8 — Cells 0, 4 updated (ORM definition, Migration definition)")


# ─────────────────────────────────────────────────────────────────────────────
# 2G: Django Chapter 9 — django_orm.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_django_ch9():
    path = ROOT / "django/2. Core_Django/9. django_orm.ipynb"
    nb = load(path)

    # Cell 0: Add QuerySet definition before section 9.1
    cell = nb["cells"][0]
    current = text_of(cell)
    old = "## 9.1 ORM Mental Model: QuerySets Are **Lazy Programs**, Not Results\n\n### 9.1.1 QuerySet = \"a query description\""
    new = (
        "## 9.1 ORM Mental Model: QuerySets Are **Lazy Programs**, Not Results\n\n"
        "### What is a QuerySet?\n\n"
        "A **QuerySet** is a lazy, composable database query. Creating a QuerySet — "
        "for example, `Article.objects.filter(status='published')` — does **not** hit "
        "the database. It builds a query description. The database is only queried when "
        "you evaluate the QuerySet: iterating over it, calling `.count()`, slicing it, "
        "or converting it to a list.\n\n"
        "This laziness lets you progressively compose queries in clean, readable steps "
        "before any SQL is executed — a core design principle of Django's ORM.\n\n"
        "### 9.1.1 QuerySet = \"a query description\""
    )
    set_source(cell, current.replace(old, new, 1))
    save(nb, path)
    print("2G: Django Ch9 — Cell 0 updated (QuerySet definition)")


# ─────────────────────────────────────────────────────────────────────────────
# 2H: Django Chapter 13 — middleware_sessions_messages_and_cookies.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_django_ch13():
    path = ROOT / "django/2. Core_Django/13. middleware_sessions_messages_and_cookies.ipynb"
    nb = load(path)

    # Cell 0: Add formal Middleware definition at the start of section 13.1
    cell0 = nb["cells"][0]
    current0 = text_of(cell0)
    old0 = "### 13.1.1 What middleware actually is (concrete mental model)\n\nMiddleware forms a chain like onion layers."
    new0 = (
        "### 13.1.1 What middleware actually is (concrete mental model)\n\n"
        "**Middleware** is a pluggable layer that wraps every request and response. "
        "Each middleware component can read or modify the request before it reaches "
        "your view, and read or modify the response before it is sent to the client. "
        "Middleware runs in order on the way in, and in **reverse order** on the way out.\n\n"
        "Middleware forms a chain like onion layers."
    )
    set_source(cell0, current0.replace(old0, new0, 1))

    # Cell 2: CsrfViewMiddleware section — add CSRF definition
    cell2 = nb["cells"][2]
    current2 = text_of(cell2)
    old2 = "### 13.2.4 `CsrfViewMiddleware`"
    new2 = (
        "### 13.2.4 `CsrfViewMiddleware`\n\n"
        "**CSRF** (Cross-Site Request Forgery) is an attack where a malicious website "
        "tricks a logged-in user's browser into making a state-changing request "
        "(POST/PUT/DELETE) to your site without the user's knowledge — because the "
        "browser automatically sends cookies (including session cookies) with "
        "cross-origin requests.\n\n"
        "Django's CSRF middleware prevents this by requiring a secret token in all "
        "state-changing requests. The token is tied to the user's session and cannot "
        "be guessed by a third-party site. The `{% csrf_token %}` tag in templates "
        "injects this token into forms automatically."
    )
    # Find the section and replace, being careful not to replace the wrong part
    if old2 in current2:
        # We need to keep the original content after the header
        idx = current2.index(old2)
        # Find what comes after the header
        after_header_start = idx + len(old2)
        # Check what's immediately after
        rest = current2[after_header_start:]
        # Insert the new definition, then the original content
        set_source(cell2, current2[:idx] + new2 + "\n" + rest.lstrip("\n"))

    save(nb, path)
    print("2H: Django Ch13 — Cells 0, 2 updated (Middleware formal def, CSRF definition)")


# ─────────────────────────────────────────────────────────────────────────────
# 2I: Django Chapter 24 — django_rest_framework.ipynb
# ─────────────────────────────────────────────────────────────────────────────
def patch_django_ch24():
    path = ROOT / "django/5. Apis_with_Django/24. django_rest_framework.ipynb"
    nb = load(path)

    # Cell 0: Add DRF and Serializer definitions right after the intro title
    cell = nb["cells"][0]
    current = text_of(cell)
    old = (
        "This chapter rebuilds your \"plain Django JSON API\" into a **proper, scalable API**\n"
        "using **Django REST Framework** (DRF) the way it's done in real teams.\n\n"
        "You'll learn DRF's core building blocks deeply:"
    )
    new = (
        "This chapter rebuilds your \"plain Django JSON API\" into a **proper, scalable API**\n"
        "using **Django REST Framework** (DRF) the way it's done in real teams.\n\n"
        "**Django REST Framework (DRF)** is a powerful third-party library for building "
        "REST APIs with Django. It provides serializers, viewsets, routers, "
        "authentication, permissions, and browsable API views out of the box — "
        "turning the manual work of parsing JSON, validating fields, and building "
        "consistent error responses into a declarative, reusable system.\n\n"
        "**Serializer**: a component that converts complex Python objects (like Django "
        "model instances) to and from simple Python data types (dicts, lists) that can "
        "be rendered as JSON/XML. Serializers also handle input validation — they are "
        "the DRF equivalent of Django's Form classes, but designed for APIs.\n\n"
        "You'll learn DRF's core building blocks deeply:"
    )
    set_source(cell, current.replace(old, new, 1))
    save(nb, path)
    print("2I: Django Ch24 — Cell 0 updated (DRF definition, Serializer definition)")


# ─────────────────────────────────────────────────────────────────────────────
# Run all patches
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    patch_fastapi_ch1()
    patch_fastapi_ch6()
    patch_fastapi_ch11()
    patch_fastapi_ch12()
    patch_django_ch5()
    patch_django_ch8()
    patch_django_ch9()
    patch_django_ch13()
    patch_django_ch24()
    print("\nAll term definitions applied.")
