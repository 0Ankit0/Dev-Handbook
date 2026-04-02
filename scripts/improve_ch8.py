import json

NB = '/media/ankit/Programming/Projects/Dev-Handbook/flask/3. application_structure/8. blueprints_and_application_factory.ipynb'

def src(text):
    """Convert multi-line string to Jupyter source list."""
    lines = text.split('\n')
    out = [l + '\n' for l in lines[:-1]]
    if lines[-1]:
        out.append(lines[-1])
    elif out:
        pass  # trailing newline already on last element
    return out

with open(NB) as f:
    nb = json.load(f)

# ── CELL 1 — Intro ─────────────────────────────────────────────────────────
nb['cells'][1]['source'] = src("""# Chapter 8: Blueprints and the Application Factory

**Learning goals:**
- Understand *why* blueprints exist — the "one big file" problem explained
- Create a blueprint, register routes on it, and mount it in a factory
- Use `url_for` correctly with blueprint namespaces (`auth.login`, not `login`)
- Understand the `init_app()` pattern for shared extensions
- Implement the Application Factory (`create_app()`) and understand how it eliminates circular imports
- Use `current_app` as a context proxy when `app` is not available as a global
- Know the recommended directory layout for a medium-sized Flask project

---

## 🚨 The "One Big File" Problem

Every Flask tutorial starts with a single file:

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index(): ...
```

This is fine for learning. But real applications grow fast. Within weeks you have:

```python
# app.py — now 1 200 lines and counting
@app.route('/login')       def login(): ...
@app.route('/logout')      def logout(): ...
@app.route('/register')    def register(): ...
@app.route('/posts')       def posts(): ...
@app.route('/post/<id>')   def post(id): ...
@app.route('/admin/users') def admin_users(): ...
# ... 80 more routes, all in one file
```

Problems with a monolithic `app.py`:

| Problem | Impact |
|---|---|
| 1 000-line file | Impossible to navigate; every change risks breaking unrelated code |
| One global `app` | Cannot create multiple app instances — tests interfere with each other |
| All imports at top | Any model that needs `app` causes a circular import |
| No namespace separation | `url_for('login')` is ambiguous when you have both a web and an API login |
| Everyone edits the same file | Git conflicts on every team PR |

**Blueprints** solve the first problem — modular code.
**The Application Factory** solves the rest — testability, config flexibility, and circular imports.

> ❓ **What is a decorator?** A decorator is a function that wraps another function to add behaviour before or after it runs. `@app.route('/')` is shorthand for `index = app.route('/')(index)` — it registers your view function with Flask's URL map without any explicit call.""")

# ── CELL 2 — Big Picture ───────────────────────────────────────────────────
nb['cells'][2]['source'] = src("""## 🗺️ The Big Picture

You started with one file: **`app.py`**. It worked. But now you have routes for users, posts,
comments, authentication, and admin — all jumbled in one **1 000-line file**.
Blueprints split that file into logical modules. The **Application Factory** creates the app
in a way that makes it **testable, configurable, and free of circular imports**.

```text
Before blueprints          After blueprints
──────────────────         ──────────────────────────────────
app.py (1 000 lines)  →   app/
                              __init__.py  (factory, ~30 lines)
                              auth/
                                  routes.py
                              blog/
                                  routes.py
                              admin/
                                  routes.py
```

Two ideas work together:

| Concept | Role |
|---|---|
| **Blueprint** | A *mini-app* that groups related routes, templates, and static files |
| **Application Factory** | A function (`create_app`) that builds and returns the Flask app |

---

### 🔄 The Circular Import Problem (and how the factory fixes it)

Without the factory pattern you hit a classic Python trap almost immediately:

```python
# app.py  — creates the global app
from flask import Flask
app = Flask(__name__)

# models.py  — needs the app to initialise the DB
from app import app          # ← imports app.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)         # ← binds db at import time

# routes.py  — needs both app AND db
from app import app          # ← imports app.py (again)
from models import db        # ← imports models.py, which imports app.py → CIRCULAR!
```

Python raises `ImportError: cannot import name 'app' from partially initialized module 'app'`.

The **factory pattern** breaks this cycle by deferring extension binding:

```text
Traditional (circular)              Factory (no cycle)
──────────────────────              ──────────────────────────────
app.py    imports models      →    extensions.py: db = SQLAlchemy()   # no app yet
models.py imports app         →    create_app(): db.init_app(app)     # bound here
routes.py imports both        →    blueprints imported INSIDE factory
↑  CIRCULAR IMPORT ↑               ↑  No circular dependency ↑
```

The secret: **extensions are created without an `app` argument**, and wired up to the app
later inside `create_app()`. This is the `init_app()` pattern.""")

# ── CELL 3 — Core Concepts ─────────────────────────────────────────────────
nb['cells'][3]['source'] = src("""## 💡 Core Concepts — The Why

### Blueprint analogy

Think of a large company:

- **HR department** (auth blueprint) → hiring / firing / payroll procedures
- **Finance department** (blog blueprint) → invoice / budget procedures
- **IT department** (admin blueprint) → server / access procedures

Each department runs independently with its own rulebook.
On day one everyone registers with **company HQ** (the Flask app).
No department needs to know what the others are doing.

A **Blueprint** is exactly that departmental instruction manual:
it defines routes, error handlers, template filters — completely self-contained.
The `create_app` factory is **company HQ**: it hires every department at startup.

---

### Blueprint URL Prefixes and Name Prefixes

When you register a blueprint you give it two kinds of namespacing:

**1. URL prefix** — prepended to every route URL in the blueprint:

```python
# Every route inside auth_bp is now under /auth/
app.register_blueprint(auth_bp, url_prefix='/auth')
# /login  inside auth_bp  →  /auth/login  in the browser
# /register inside auth_bp  →  /auth/register  in the browser
```

**2. Endpoint name prefix** — automatically namespaces every `url_for()` call:

```python
# auth/routes.py
auth_bp = Blueprint('auth', __name__)   # 'auth' is the blueprint name

@auth_bp.route('/login')
def login(): ...                         # endpoint is 'auth.login'

# ── Anywhere in the app ──
url_for('auth.login')    # ✅ correct  — blueprint_name.function_name
url_for('login')         # ❌ BuildError — there is no global 'login' endpoint anymore
```

This is not optional — it's enforced. Two blueprints can both define a `login` view without
conflict because they are `auth.login` and `api.login`. This is the **endpoint namespace**.

> ⚠️ **Most common beginner mistake:** Writing `url_for('login')` in a template after moving
> the view into a blueprint. Flask raises `BuildError: Could not build url for endpoint 'login'`.
> **Fix:** always use `blueprint_name.function_name` — e.g., `url_for('auth.login')`.

---

### The `init_app()` Pattern

This pattern appears in every major Flask extension (SQLAlchemy, Migrate, Login, Mail…).
Understanding it is essential for working with any non-trivial Flask project.

**The problem it solves:** Extensions need the `app` object to configure themselves, but in the
factory pattern `app` doesn't exist yet when you first import the extension at module level.

```python
# extensions.py — create extensions WITHOUT an app argument
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db           = SQLAlchemy()    # no app — just creates the extension object
login_manager = LoginManager()
mail          = Mail()

# app/__init__.py — bind extensions to the app INSIDE the factory
from .extensions import db, login_manager, mail

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)            # ← binds db to THIS specific app instance
    login_manager.init_app(app)
    mail.init_app(app)

    return app
```

Why is `init_app()` better than `db = SQLAlchemy(app)`?

| | `SQLAlchemy(app)` at module level | `init_app()` inside factory |
|---|---|---|
| Works with factory pattern | ❌ No (`app` not yet created) | ✅ Yes |
| Supports multiple app instances | ❌ No | ✅ Yes |
| Tests with different config | ❌ Hard | ✅ Easy — call `create_app('testing')` |
| Circular import risk | ✅ High | ❌ None |

---

### Application Factory — `create_app()` Annotated

```python
# app/__init__.py
from flask import Flask
from .extensions import db, login_manager
from .auth.routes  import auth_bp
from .blog.routes  import blog_bp

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=True)  # (1)

    # ── Load config ─────────────────────────────────────────────
    if config_object is None:
        config_object = 'config.ProductionConfig'
    app.config.from_object(config_object)            # (2)
    app.config.from_pyfile('config.py', silent=True) # (3) instance/ overrides

    # ── Initialise extensions ────────────────────────────────────
    db.init_app(app)                                 # (4)
    login_manager.init_app(app)                      # (5)

    # ── Register blueprints ──────────────────────────────────────
    app.register_blueprint(auth_bp, url_prefix='/auth')  # (6)
    app.register_blueprint(blog_bp, url_prefix='/blog')  # (7)

    return app                                       # (8)
```

| Line | What it does |
|---|---|
| (1) | `instance_relative_config=True` enables the `instance/` folder for machine-local secrets |
| (2) | Loads config from a Python class (`DevelopmentConfig`, `ProductionConfig`…) |
| (3) | Optional local override from `instance/config.py` — not committed to git |
| (4–5) | Binds extensions to *this* app instance via `init_app()` |
| (6–7) | Registers blueprints; each route inside gets the specified URL prefix |
| (8) | Returns the fully configured app — the caller decides what to do with it |

---

### `current_app` — The Application Context Proxy

Inside a factory-built app you cannot do this:

```python
# auth/routes.py
from app import app          # ← ImportError, or imports the wrong instance

@bp.route('/settings')
def settings():
    return app.config['SOME_KEY']   # fragile — circular import
```

Instead, Flask provides `current_app` — a **context-local proxy** that always points to
the active application for the current request:

```python
from flask import current_app

@bp.route('/settings')
def settings():
    key   = current_app.config['SOME_KEY']   # ✅ correct app, always
    debug = current_app.debug                 # ✅ works anywhere
    return str(key)
```

**How it works:** When a request arrives, Flask pushes an *application context* onto a
thread-local stack. `current_app` reads the top of that stack. When the request ends,
Flask pops it. This means `current_app` is only valid *inside a request or application context*.

```python
# ❌ Wrong — module level, no context active
print(current_app.config['DEBUG'])    # RuntimeError: Working outside of application context

# ✅ Correct — inside a request handler
@bp.route('/')
def index():
    print(current_app.config['DEBUG'])   # fine

# ✅ Correct — push context manually (e.g., CLI scripts, background tasks)
with app.app_context():
    print(current_app.config['DEBUG'])   # fine
```

---

### Blueprint Templates — `template_folder` and Lookup Order

Each blueprint can carry its own `templates/` folder:

```python
auth_bp = Blueprint('auth', __name__, template_folder='templates')
```

Directory layout:

```text
app/
├── templates/                  ← app-level templates (checked FIRST)
│   └── auth/
│       └── login.html          ← overrides blueprint's version if present
└── auth/
    ├── routes.py
    └── templates/              ← blueprint templates (checked SECOND)
        └── auth/
            └── login.html
```

**Lookup order:** Flask always checks the **app-level** `templates/` folder first.
If the file isn't found, it checks each registered blueprint's `templates/` in registration order.

This lets you **override** a third-party blueprint's templates by placing the same-named file
in the app-level `templates/` folder — a powerful customisation pattern.

> ⚠️ **Convention:** Always nest blueprint templates in a subdirectory named after the blueprint
> (`auth/login.html`, not just `login.html`) to avoid name collisions across blueprints.""")

# ── CELL 13 — Comparison ───────────────────────────────────────────────────
nb['cells'][13]['source'] = src("""## ⚖️ Comparison: Single-file vs Blueprints

The table below summarises when each approach makes sense.

| Criterion | Single file | Blueprints + Factory |
|---|---|---|
| Project size | Small (< ~200 lines) | Medium → Large |
| Team size | Solo | 2+ developers |
| Testability | Hard (global `app`) | Easy (`create_app("testing")`) |
| Config flexibility | One config at startup | Multiple configs, chosen at runtime |
| Route namespacing | Flat (`url_for('login')`) | Namespaced (`url_for('auth.login')`) |
| Template organisation | One flat folder | Per-blueprint folders, overridable |
| Circular import risk | Medium to High | None — factory defers imports |
| Extension management | `db = SQLAlchemy(app)` | `db.init_app(app)` via factory |
| Learning curve | Low | Slightly higher upfront, pays off fast |

---

### When to choose each

**Stick with a single file when:**
- You are prototyping, learning, or building a throwaway demo
- The app is under ~200 lines and unlikely to grow significantly
- You are building a quick internal tool or CLI-adjacent micro-service

**Move to Blueprints + Factory when:**
- The app has more than 2–3 distinct feature areas (auth, blog, admin…)
- You need different configs for testing vs. production
- More than one developer is working on the codebase at the same time
- You start hitting circular import errors (the factory is the cure)
- You want to write proper unit tests using `app.test_client()`""")

# ── CELL 19 — Real-World Layout ────────────────────────────────────────────
nb['cells'][19]['source'] = src("""## 🌍 Real-World Project Layout

The pattern you just learned is used in virtually every production Flask app.

Here are canonical open-source examples to study:

| Project | What to look at |
|---|---|
| [flask-bone](https://github.com/imwilsonxu/fbone) | Classic blueprint + factory layout |
| [cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask) | Modern scaffold with all extensions wired |
| Official [Flask tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/) | Step-by-step factory + blueprint from scratch |

**Recommended layout for a medium-sized Flask app:**

```text
my_flask_app/
├── wsgi.py                      ← Entry point: app = create_app()
├── config.py                    ← Config class hierarchy (no secrets here)
├── .env                         ← Local secrets (in .gitignore!)
├── .env.example                 ← Template with placeholder values — committed to git
├── requirements.txt
│
├── app/
│   ├── __init__.py              ← def create_app(config=None): ...
│   ├── extensions.py            ← db = SQLAlchemy(); login_manager = LoginManager()
│   │
│   ├── auth/                    ← Auth blueprint
│   │   ├── __init__.py          ← auth_bp = Blueprint('auth', __name__, ...)
│   │   ├── routes.py            ← @auth_bp.route('/login'), /logout, /register
│   │   ├── forms.py             ← LoginForm, RegistrationForm (WTForms)
│   │   └── templates/
│   │       └── auth/
│   │           ├── login.html
│   │           └── register.html
│   │
│   ├── blog/                    ← Blog blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py            ← Post, Comment (or shared in app/models.py)
│   │   └── templates/
│   │       └── blog/
│   │           └── index.html
│   │
│   ├── models.py                ← Shared models (User, etc.)
│   └── templates/
│       └── base.html            ← App-level base template
│
├── instance/                    ← NOT in git — machine-local secrets
│   └── config.py
│
└── tests/
    ├── conftest.py              ← @pytest.fixture: return create_app('testing')
    ├── test_auth.py
    └── test_blog.py
```

**The factory makes testing trivial:**

```python
# tests/conftest.py
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app('testing')   # in-memory DB, TESTING=True, no side-effects
    yield app

@pytest.fixture
def client(app):
    return app.test_client()      # test HTTP requests without a real server

# tests/test_auth.py
def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200
```

> ❓ **Why use an ORM instead of raw SQL?** An ORM (Object-Relational Mapper) lets you work
> with database rows as Python objects. It prevents SQL injection by default, handles
> connection pooling, and makes switching databases (SQLite → PostgreSQL) straightforward.""")

# ── CELL 21 — Practice Prompts ─────────────────────────────────────────────
nb['cells'][21]['source'] = src("""## 🏋️ Practice Prompts

Work through these to solidify your understanding:

1. **Refactor** — Take a 200-line single-file Flask app and split it into at least two blueprints
   (`auth` and `main`). Verify nothing breaks by running any existing tests.

2. **Factory configs** — Add a `TestingConfig` class in `config.py` and write a `pytest` fixture
   that calls `create_app(TestingConfig)`. Run a route test using the fixture's `client`.

3. **Blueprint templates** — Give the `blog` blueprint its own `templates/blog/` folder. Render
   `blog/index.html` from a blueprint route. Then place a same-named file in the app-level
   `templates/blog/` folder and confirm it takes priority.

4. **`url_for` audit** — Search an existing project for all `url_for(` calls. Verify every one
   uses the `blueprint.view` format (`auth.login`, not `login`). Fix any that don't.

5. **Error handlers** — Register a `404` error handler on a blueprint using
   `@bp.app_errorhandler(404)`. Confirm it fires for any 404 in the whole app, not just that
   blueprint's routes.

6. **`extensions.py`** — Add `Flask-Mail` to a project using the `extensions.py` pattern.
   Create `mail = Mail()` there, call `mail.init_app(app)` in the factory, and send a test
   email from a blueprint route using `current_app.extensions['mail']`.

7. **`current_app` exercise** — Outside any blueprint, write a small CLI script that uses
   `with app.app_context():` to access `current_app.config`. Then try accessing it
   *without* the context block and observe the `RuntimeError`.

8. **Circular import reproduction** — Create a toy app that intentionally triggers a circular
   import (models importing app, routes importing models). Then refactor it to use the factory
   pattern and confirm the error disappears.

---
*Tip: the official Flask docs [Application Factories](https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/)
and [Blueprints](https://flask.palletsprojects.com/en/3.0.x/blueprints/) pages are excellent companions to this chapter.*""")

with open(NB, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Ch8 saved.")
