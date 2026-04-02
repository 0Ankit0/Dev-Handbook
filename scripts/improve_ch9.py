import json

NB = '/media/ankit/Programming/Projects/Dev-Handbook/flask/3. application_structure/9. configuration_management.ipynb'

def src(text):
    lines = text.split('\n')
    out = [l + '\n' for l in lines[:-1]]
    if lines[-1]:
        out.append(lines[-1])
    return out

with open(NB) as f:
    nb = json.load(f)

C = nb["cells"]

C[1]["source"] = src("""# Chapter 9: Configuration Management -- Controlling Your App's Behaviour

> **"Your app should behave differently depending on where it runs -- without you changing a single line of code."**

Configuration management is the discipline of keeping environment-specific settings *outside* your application logic.
This chapter shows you three approaches -- from quick hacks to production-grade patterns -- and explains exactly why each step up the ladder matters.

**What you'll learn:**
- Why hardcoding settings is dangerous (and how it ends careers)
- Three approaches to Flask configuration (direct assignment -- from_pyfile -- config classes)
- All important built-in Flask config keys and what each one controls
- How to use environment variables and `python-dotenv` for the 12-Factor App pattern
- The fail-fast pattern for required production secrets
- How to access config safely inside blueprints with `current_app.config`
- The `instance/` folder: secrets outside version control
- Logging configuration per environment

---

### The 12-Factor App Principle

The [12-Factor App](https://12factor.net/config) methodology (the foundation of modern cloud-native development) states:

> **Factor III: Store config in the environment.**

This means: separate configuration from code entirely. An app should be deployable to
development, staging, and production *without any code changes* -- only the environment changes.

This is why experienced developers never hardcode credentials or environment-specific values
in Python files that get committed to version control.""")

C[2]["source"] = src("""## Big Picture: One App, Three Environments

Your development database should be different from your production database.
Debug mode must be off in production. Email credentials can't be hardcoded in source code.
**Configuration management is how you control these settings without touching your application code.**

| Setting | Development | Testing | Production |
|---|---|---|---|
| `DEBUG` | `True` | `False` | `False` |
| `TESTING` | `False` | `True` | `False` |
| `DATABASE_URL` | `sqlite:///dev.db` | `sqlite:///:memory:` | `postgresql://prod-host/mydb` |
| `SECRET_KEY` | `"dev-only-key"` | `"test-key"` | *from environment variable -- never in code* |
| `MAIL_SERVER` | `localhost` | `None` | `smtp.sendgrid.net` |
| `LOG_LEVEL` | `DEBUG` | `WARNING` | `ERROR` |

> **Rule of thumb:** anything that changes between environments belongs in config, not in code.

---

### Why This Matters

Without proper config management you end up with anti-patterns like these:

```python
# Anti-pattern 1: Hardcoded credentials
app.config['SECRET_KEY'] = 'my-secret-key-123'    # leaked on GitHub -- game over

# Anti-pattern 2: Commented-out environment switches
# app.config['DATABASE_URL'] = 'sqlite:///dev.db'     # dev
app.config['DATABASE_URL'] = 'postgresql://prod/db'  # prod (remember to uncomment!)

# Anti-pattern 3: if/else based on hostname
import socket
if socket.gethostname() == 'my-laptop':
    app.config['DEBUG'] = True   # breaks on any new machine
```

All three are fragile, error-prone, and put secrets in version control.
The solution is **config classes loaded via environment variables**.""")

C[3]["source"] = src("""## Core Concepts: The Why

### `app.config` is a Control Panel

Think of `app.config` as a **control panel for your Flask application**.
It is just a special dictionary that Flask -- and every extension -- reads at startup:

```text
+------------------------------------------------------+
|                  app.config  (dict)                  |
|  +----------------+   +----------------------------+ |
|  |  SECRET_KEY    |   |  SQLALCHEMY_DATABASE_URI   | |
|  |  DEBUG         |   |  MAIL_SERVER               | |
|  |  TESTING       |   |  SQLALCHEMY_TRACK_MODS     | |
|  +----------------+   +----------------------------+ |
|        ^ Flask reads these          ^ Extensions read |
+------------------------------------------------------+
```

You can read any key like a dict: `app.config['SECRET_KEY']`
Set one: `app.config['DEBUG'] = True`
Access inside blueprints: `current_app.config['SECRET_KEY']`

---

### Key Flask Config Variables You Must Know

| Key | Default | What it controls |
|---|---|---|
| `SECRET_KEY` | `None` (warning!) | Signs session cookies and CSRF tokens -- **must be a strong random value** |
| `DEBUG` | `False` | Enables hot reloader, detailed error pages, interactive Werkzeug debugger |
| `TESTING` | `False` | Test mode -- exceptions propagate to tests, no error-catch pages |
| `SESSION_COOKIE_SECURE` | `False` | `True` = cookie only sent over HTTPS (set this in production!) |
| `SESSION_COOKIE_HTTPONLY` | `True` | `True` = JavaScript cannot access the cookie (prevents XSS theft) |
| `SESSION_COOKIE_SAMESITE` | `'Lax'` | CSRF cookie protection -- `'Strict'` is safer where compatible |
| `PERMANENT_SESSION_LIFETIME` | 31 days | `timedelta` for how long "remember me" sessions last |
| `MAX_CONTENT_LENGTH` | `None` | Reject request bodies larger than N bytes (file-upload limit) |
| `SERVER_NAME` | `None` | Hostname and port for URL generation outside a request context |
| `SQLALCHEMY_DATABASE_URI` | *(extension)* | SQLAlchemy database connection string |
| `SQLALCHEMY_TRACK_MODIFICATIONS` | `False` | Disable to silence SQLAlchemy deprecation warnings |
| `MAIL_SERVER` | *(extension)* | SMTP server hostname for Flask-Mail |
| `REMEMBER_COOKIE_DURATION` | *(extension)* | Flask-Login "Remember Me" cookie lifetime |

> **`SECRET_KEY` is the single most important setting.** It signs your session cookies.
> If it is `None`, Flask falls back to an empty string and your sessions are insecure.
> If it is leaked, attackers can forge session cookies -- giving them access to any account.
> Generate it with: `python -c "import secrets; print(secrets.token_hex(32))"`

---

### The 3-Environment Problem

Every real project runs in (at least) three environments:

| Environment | Who uses it | Needs |
|---|---|---|
| **Development** | You, locally | SQLite, debug reloader, verbose errors |
| **Testing** | CI/CD pipeline | In-memory DB, no side effects, fast startup |
| **Production** | Real users | PostgreSQL, secrets from env vars, no debug output |

One config file cannot serve all three -- you need a **config class hierarchy**.

---

### Logging Configuration Per Environment

Logging is often overlooked in configuration management but is critically important in production.
Flask uses Python's standard `logging` module. Configure it per environment:

```python
import logging
from logging.handlers import RotatingFileHandler

class DevelopmentConfig(Config):
    LOG_LEVEL = logging.DEBUG    # see every request and query in development

class ProductionConfig(Config):
    LOG_LEVEL = logging.ERROR    # only errors in production -- less noise, less PII leakage

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    logging.basicConfig(level=app.config['LOG_LEVEL'])
    if not app.debug:
        handler = RotatingFileHandler('logs/app.log', maxBytes=10_000_000, backupCount=3)
        handler.setLevel(app.config['LOG_LEVEL'])
        app.logger.addHandler(handler)
    return app
```

> **Never log passwords, session tokens, or PII.** Even in development, avoid
> `app.logger.debug(f"User password: {password}")`. Logs are often shared for debugging
> and may be stored for months -- treat them as semi-public documents.

> **Why automate builds and tests?** Manual steps get skipped under pressure. A CI pipeline
> runs tests on every commit, catches regressions before they reach production, and gives the
> whole team a shared signal -- green means good, red means broken.""")

C[6]["source"] = src("""## Approach 3: Config Classes -- The Professional Way

Config classes use **Python inheritance** to share common settings while letting each
environment override exactly what it needs.

```text
         Config  (base -- shared defaults)
        /       \\          \\
DevelopmentConfig  TestingConfig  ProductionConfig
```

- **`Config`** holds everything every environment shares
- Subclasses **only override what differs** -- no repetition
- `create_app(config_name)` picks the right class at startup
- Secrets always come from **`os.environ.get()`** -- never hardcoded

---

### Three Ways to Load Config into `app.config`

Flask provides multiple `from_*` methods. You can stack them -- later calls override earlier ones.
This layering is the key to flexible, environment-aware configuration.

#### 1. `app.config.from_object(obj)` -- Load from a Python class or module path

```python
# Pass a class directly:
app.config.from_object(ProductionConfig)

# Or pass an import path string:
app.config.from_object('config.ProductionConfig')
```

All **uppercase** attributes on the class are loaded as config keys.
Lowercase attributes are silently ignored -- useful for adding Python helper methods.

#### 2. `app.config.from_pyfile(filename)` -- Load from a `.py` file

```python
# Load from the instance folder:
app.config.from_pyfile('instance/config.py')

# silent=True: no error if the file is missing (safe for optional local overrides):
app.config.from_pyfile('production.cfg', silent=True)
```

Useful for **machine-specific settings** in the `instance/` folder that should not be in git.
Think of it as a local override layer on top of your committed config class.

#### 3. `app.config.from_envvar(variable_name)` -- Load from env var pointing to a config file

```python
# export MYAPP_SETTINGS=/etc/myapp/production.cfg
app.config.from_envvar('MYAPP_SETTINGS')    # reads the file path from the env var
```

Useful for ops teams who manage config files at the deployment level, outside the codebase.

---

### Stacking All Three (Production Pattern)

```python
def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)

    # 1. Load base config from a class (committed to git, no secrets)
    app.config.from_object(config_map[config_name])

    # 2. Override with machine-specific instance config (NOT in git)
    app.config.from_pyfile('config.py', silent=True)

    # 3. Override with ops-managed config file pointed to by env var (optional)
    app.config.from_envvar('MYAPP_SETTINGS', silent=True)

    return app
```

**Later calls win.** So instance config overrides class config, and env-pointed config
overrides everything. The chain is: defaults -> class -> instance folder -> env var file.""")

C[9]["source"] = src("""## Environment Variables: The Right Way to Store Secrets

An **environment variable** is a key-value pair set in the operating system shell --
completely outside your Python code and git repository.

```bash
# Set in shell (Linux/macOS)
export SECRET_KEY="super-secret-production-key-abc123"
export DATABASE_URL="postgresql://user:pass@db-host:5432/mydb"

# Set in shell (Windows PowerShell)
$env:SECRET_KEY = "super-secret-production-key-abc123"
```

Python reads them with `os.environ`:

```python
import os
secret = os.environ.get('SECRET_KEY')    # None if not set -- safe, no exception
secret = os.environ['SECRET_KEY']        # KeyError if not set -- strict, use for required values
```

### Why environment variables?

| Concern | Hardcoded | Environment Variable |
|---|---|---|
| Stored in git history | Yes (dangerous) | Never |
| Needs code change to rotate | Yes | No -- just update the var |
| Works in Docker/Kubernetes | Awkward | Native `-e` flag / Secrets |
| Works in CI/CD secrets vault | No | Native |
| Auditable access | Anyone with repo | Ops team only |

---

### The Instance Folder -- Secrets Outside Version Control

Flask supports an `instance/` folder at the project root for machine-specific config that
should never be committed to git. Enable it with `instance_relative_config=True`:

```python
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)  # loads instance/config.py if it exists
```

```text
my_flask_app/
+-- config.py           <- committed to git (no secrets)
+-- instance/           <- NOT committed to git
|   +-- config.py       <- SECRET_KEY, DATABASE_URL, API keys go here
+-- app/
    +-- __init__.py
```

**`instance/config.py`** (add `instance/` to `.gitignore`):
```python
SECRET_KEY = 'my-local-dev-key-never-pushed'
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/mydev'
```

This is ideal for local development secrets. In production, use actual environment variables
(Docker env, Heroku config vars, AWS Secrets Manager, etc.) instead of the instance folder.

> What problem does Docker solve? "It works on my machine." Docker packages your app
> and its exact environment (OS libraries, Python version, config) into a container image
> that runs identically on any machine or cloud provider.""")

C[15]["source"] = src("""## Hardcoded vs Environment Variables: Side-by-Side

| | Hardcoded in source | Environment variable |
|---|---|---|
| **Visible in git?** | Yes -- forever, even after deletion | No |
| **Rotate without deploy?** | No -- requires code change + deploy | Yes -- update var, restart |
| **Works in Docker?** | Awkward | Native `-e SECRET_KEY=...` flag |
| **Works in Heroku/Railway?** | Poor | Dashboard config vars |
| **Auditable access?** | Anyone with repo access | Ops team only |
| **Accidental leak risk?** | HIGH | LOW |

### Real-world consequences of hardcoded secrets

- A leaked `SECRET_KEY` lets attackers **forge session cookies** -- full account takeover for all users
- A leaked `DATABASE_URL` with credentials exposes **all your user data**
- GitHub's secret scanning notifies the service when tokens appear in pushes -- but by then the
  token is already in git history and the damage often precedes the notification
- Cloud providers bill you for compute resources spun up by attackers who found your API keys

> **Golden rule:** If it's a secret, it lives in an environment variable. No exceptions.

### How to generate a safe SECRET_KEY

```python
# Run once -- paste the output into your .env file or server environment
import secrets
print(secrets.token_hex(32))
# e.g.: 'a3f8d92c1e4b0f7a6d2e9c8b5a1f3d0e7c4b2a9f6e3d0c7a4b1e8f5c2a9d6b3'
```

Never use short strings, your name, "secret", or any guessable value.
The key should be at least 32 bytes of cryptographically random data.""")

C[20]["source"] = src("""## Real-World Project Structure

Here's how configuration integrates with a full Flask project:

```text
myapp/
+-- config.py               <- Config class hierarchy (committed, no secrets)
+-- .env                    <- Local dev secrets (in .gitignore!)
+-- .env.example            <- Template with empty values (committed to git)
+-- .gitignore              <- Must include: .env, instance/
+-- app/
|   +-- __init__.py         <- create_app() factory
|   +-- auth/
|   |   +-- __init__.py     <- Blueprint (uses current_app.config)
|   +-- models.py
+-- instance/
    +-- config.py           <- Machine-specific overrides (in .gitignore)
```

**`config.py`** (committed, no secrets):
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-fallback-not-for-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = 'WARNING'

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', 'sqlite:///dev.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SESSION_COOKIE_SECURE   = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'

    @classmethod
    def init_app(cls, app):
        """Fail fast -- catch missing secrets at startup, not mid-request."""
        required = ['SECRET_KEY', 'DATABASE_URL']
        missing = [k for k in required if not app.config.get(k)]
        if missing:
            raise RuntimeError(f"Missing required config keys: {missing}")

config = {
    'development': DevelopmentConfig,
    'testing':     TestingConfig,
    'production':  ProductionConfig,
    'default':     DevelopmentConfig,
}
```

**`app/__init__.py`**:
```python
from flask import Flask
from config import config

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])          # class-level settings
    app.config.from_pyfile('config.py', silent=True)     # instance/ overrides
    config[config_name].init_app(app)                    # fail-fast validation
    return app
```

**`.env.example`** (committed -- so team members know which env vars are needed):
```
SECRET_KEY=
DATABASE_URL=
MAIL_PASSWORD=
STRIPE_SECRET_KEY=
```

**`.env`** (never committed -- each developer fills in their own values locally):
```
SECRET_KEY=my-local-dev-key-abc123
DATABASE_URL=sqlite:///dev.db
```""")

C[22]["source"] = src("""## Practice Prompts

Try these exercises to solidify your understanding:

1. **Three-environment setup**
   Create a `config.py` with `Config`, `DevelopmentConfig`, `TestingConfig`, and `ProductionConfig` classes.
   Add `ITEMS_PER_PAGE = 10` to the base class and override it to `5` in `TestingConfig`.
   Verify with `create_app('testing').config['ITEMS_PER_PAGE']`.

2. **Secret Key from environment**
   Remove any hardcoded `SECRET_KEY` from your config classes.
   Set it only via an environment variable. Write a test that asserts the app raises `RuntimeError`
   on startup (via `init_app` validation) when `SECRET_KEY` is missing.

3. **Fail-fast validator**
   Add an `init_app()` classmethod to `ProductionConfig` that checks for `SECRET_KEY`,
   `DATABASE_URL`, and `MAIL_PASSWORD`. Demonstrate it raises `RuntimeError` with a clear
   message when any key is missing.

4. **Blueprint config access**
   Create a blueprint with a `/debug-info` route that returns a JSON response containing
   `DEBUG`, `TESTING`, and `SQLALCHEMY_DATABASE_URI` from `current_app.config`.
   Protect it with `@login_required`.

5. **`python-dotenv` loading**
   Create a `.env` file with `SECRET_KEY=my-test-secret`.
   Load it with `load_dotenv()` in your factory and verify `os.environ.get('SECRET_KEY')`
   returns your value.

6. **Instance folder override**
   Create `instance/config.py` with `ITEMS_PER_PAGE = 50`.
   Confirm it overrides the class-level value when loaded with
   `app.config.from_pyfile('config.py', silent=True)`.

7. **Logging exercise**
   Add a `LOG_LEVEL` config key to each environment. Configure `RotatingFileHandler`
   in `create_app()` and verify that setting `LOG_LEVEL = logging.ERROR` in production config
   suppresses `DEBUG` and `INFO` messages in the log file.""")

with open(NB, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Ch9 saved.")
