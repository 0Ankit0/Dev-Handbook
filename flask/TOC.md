# The Complete Flask Developer's Handbook: From Zero to Production

## Preface
* **Introduction to the Handbook**: How to use this book effectively.
* **Why Flask?**: Flask's philosophy — micro, extensible, and unopinionated. When to choose Flask over Django or FastAPI.
* **What You'll Build**: An overview of the capstone project and the mini-projects threaded throughout.
* **Prerequisites**: Basic Python knowledge (variables, functions, classes). If you're new to Python, start with the [Python Handbook](../python/TOC.md).

---

## Part I: Flask Foundations

### [Chapter 1: Getting Started with Flask](1.%20flask_foundations/1.%20getting_started.ipynb)
* **1.1 What is Flask?**: The micro-framework philosophy, Werkzeug, Jinja2, and the Flask ecosystem.
* **1.2 Installation & Setup**: `pip install flask`, virtual environments, and project structure.
* **1.3 Your First Flask App**: The minimal app — `Flask(__name__)`, routes, and the dev server.
* **1.4 The Application Context**: Understanding `app`, `current_app`, `g`, and the request context.

### [Chapter 2: Routing and URL Building](1.%20flask_foundations/2.%20routing_and_url_building.ipynb)
* **2.1 Defining Routes**: The `@app.route()` decorator and URL patterns.
* **2.2 URL Variables**: Dynamic URL segments with type converters (`<int:id>`, `<string:name>`).
* **2.3 HTTP Methods**: Handling GET, POST, PUT, DELETE in a single route.
* **2.4 URL Building**: The `url_for()` function — never hardcode URLs again.
* **2.5 Redirects and `abort()`**: Redirecting users and returning HTTP errors cleanly.

### [Chapter 3: Templates with Jinja2](1.%20flask_foundations/3.%20templates_with_jinja2.ipynb)
* **3.1 Rendering Templates**: `render_template()`, the `templates/` folder, and passing data.
* **3.2 Jinja2 Syntax**: Variables `{{ }}`, statements `{% %}`, comments `{# #}`.
* **3.3 Control Flow in Templates**: `if`, `for`, `with`, and `set` blocks.
* **3.4 Template Filters**: Built-in filters (`upper`, `length`, `default`) and custom filters.
* **3.5 Template Inheritance**: `base.html`, `{% block %}`, and `{% extends %}` — the DRY template.
* **3.6 Macros**: Reusable template components with `{% macro %}`.

---

## Part II: Working with Data

### [Chapter 4: Forms and User Input](2.%20working_with_data/4.%20handling_forms_and_user_input.ipynb)
* **4.1 The `request` Object**: `request.form`, `request.args`, `request.json`, and `request.files`.
* **4.2 HTML Forms**: Building forms manually and handling POST submissions.
* **4.3 Flask-WTF & WTForms**: Form classes, field types, validators, and CSRF protection.
* **4.4 Flash Messages**: Communicating feedback to users across redirects.
* **4.5 Form Validation Patterns**: Server-side validation, custom validators, and error display.

### [Chapter 5: Sessions and Cookies](2.%20working_with_data/5.%20sessions_and_cookies.ipynb)
* **5.1 The Session Object**: How Flask sessions work (client-side, signed cookies).
* **5.2 Working with Cookies**: Setting, reading, and deleting cookies manually.
* **5.3 The Secret Key**: Why it matters and how to generate a secure one.
* **5.4 Session vs. Cookie**: When to use each, size limits, and security trade-offs.

### [Chapter 6: Databases with Flask-SQLAlchemy](2.%20working_with_data/6.%20databases_with_flask_sqlalchemy.ipynb)
* **6.1 Flask-SQLAlchemy Setup**: Installation, `db = SQLAlchemy(app)`, configuration.
* **6.2 Defining Models**: `db.Model`, column types, primary keys, constraints.
* **6.3 CRUD Operations**: `db.session.add()`, `db.session.commit()`, `.query`, `.filter_by()`.
* **6.4 Relationships**: One-to-many, many-to-many, `db.relationship()`, and `backref`.
* **6.5 Querying**: Filtering, ordering, paginating, and aggregating data.

### [Chapter 7: Database Migrations with Flask-Migrate](2.%20working_with_data/7.%20database_migrations_with_flask_migrate.ipynb)
* **7.1 Why Migrations?**: The problem with dropping and recreating tables in production.
* **7.2 Flask-Migrate Setup**: Integrating Alembic via Flask-Migrate.
* **7.3 The Migration Workflow**: `flask db init`, `flask db migrate`, `flask db upgrade`.
* **7.4 Writing Migration Scripts**: Auto-generated vs. manual migrations.
* **7.5 Rolling Back**: `flask db downgrade` and safe schema evolution.

---

## Part III: Application Structure

### [Chapter 8: Blueprints and the Application Factory](3.%20application_structure/8.%20blueprints_and_application_factory.ipynb)
* **8.1 The Problem with One Big File**: Why small apps grow into unmaintainable monsters.
* **8.2 Blueprints**: Registering, prefixing, and organizing routes into modules.
* **8.3 The Application Factory Pattern**: `create_app()`, `app.config`, and `init_app()`.
* **8.4 Professional Project Layout**: The structure used in real Flask production apps.

### [Chapter 9: Configuration Management](3.%20application_structure/9.%20configuration_management.ipynb)
* **9.1 Flask Configuration**: `app.config`, built-in keys, and accessing config values.
* **9.2 Config Classes**: `DevelopmentConfig`, `ProductionConfig`, `TestingConfig`.
* **9.3 Environment Variables**: `python-dotenv`, `.env` files, and `os.environ`.
* **9.4 Instance Folders**: Keeping secrets out of version control.

---

## Part IV: Authentication and Security

### [Chapter 10: User Authentication with Flask-Login](4.%20authentication_and_security/10.%20user_authentication_with_flask_login.ipynb)
* **10.1 Authentication Concepts**: Sessions, identity, and the login flow.
* **10.2 Flask-Login Setup**: `LoginManager`, `UserMixin`, `@login_required`.
* **10.3 Password Hashing**: `werkzeug.security` — `generate_password_hash` and `check_password_hash`.
* **10.4 The Login Flow**: Register → Login → Protect Routes → Logout.
* **10.5 Remember Me**: Persistent sessions and `remember=True`.

### [Chapter 11: Security Best Practices](4.%20authentication_and_security/11.%20security_best_practices.ipynb)
* **11.1 CSRF Protection**: How cross-site request forgery works and how Flask-WTF stops it.
* **11.2 XSS Prevention**: Jinja2 autoescaping and why you should never use `| safe` carelessly.
* **11.3 SQL Injection**: Why ORMs protect you (and when raw SQL is dangerous).
* **11.4 Secure Headers**: `Flask-Talisman`, HTTPS, HSTS, and CSP.
* **11.5 Input Validation**: Never trust user data — validate everything server-side.

---

## Part V: Building APIs

### [Chapter 12: Building REST APIs with Flask](5.%20building_apis/12.%20building_rest_apis.ipynb)
* **12.1 REST Principles**: Resources, statelessness, uniform interface, and JSON.
* **12.2 `jsonify()` and Status Codes**: Returning proper JSON responses.
* **12.3 Request Parsing**: Reading JSON bodies, query params, and headers.
* **12.4 Flask-RESTX**: Resource classes, namespaces, Swagger docs, and request parsing.
* **12.5 CORS**: `Flask-CORS` and allowing cross-origin requests.

### [Chapter 13: API Authentication with JWT](5.%20building_apis/13.%20api_authentication_with_jwt.ipynb)
* **13.1 Why JWT for APIs?**: Stateless auth vs. session-based auth.
* **13.2 Flask-JWT-Extended Setup**: `JWTManager`, creating tokens, and verifying them.
* **13.3 Access and Refresh Tokens**: Short-lived access tokens + long-lived refresh tokens.
* **13.4 Protected Endpoints**: `@jwt_required()`, `get_jwt_identity()`.
* **13.5 Token Revocation**: Blocklisting tokens for logout.

---

## Part VI: Advanced Features

### [Chapter 14: File Uploads and Static Assets](6.%20advanced_features/14.%20file_uploads_and_static_assets.ipynb)
* **14.1 Handling File Uploads**: `request.files`, `FileStorage`, and `secure_filename()`.
* **14.2 Validating Uploads**: File type, size limits, and MIME type checking.
* **14.3 Storing Files**: Local storage, organised directory structure, and cloud storage intro.
* **14.4 Serving Static Files**: `url_for('static', filename=...)`, Flask-Static-Digest.

### [Chapter 15: Error Handling and Logging](6.%20advanced_features/15.%20error_handling_and_logging.ipynb)
* **15.1 Custom Error Pages**: `@app.errorhandler(404)`, `@app.errorhandler(500)`.
* **15.2 Aborting Requests**: `abort()` and custom HTTP exceptions.
* **15.3 The Logging Module**: Setting up structured logging in Flask.
* **15.4 Debug Mode vs. Production**: `app.debug`, the Werkzeug debugger, and why to turn it off in prod.
* **15.5 Error Monitoring**: Introduction to Sentry for production error tracking.

### [Chapter 16: Testing Flask Applications](6.%20advanced_features/16.%20testing_flask_applications.ipynb)
* **16.1 Why Test?**: Confidence, regression prevention, and the Flask test client.
* **16.2 The Flask Test Client**: `app.test_client()` — simulating real requests without a server.
* **16.3 pytest Fixtures**: Setting up a test app, test database, and authenticated client.
* **16.4 Testing Routes and Views**: GET/POST requests, status codes, and response content.
* **16.5 Testing with a Database**: In-memory SQLite, rollbacks, and test isolation.
* **16.6 Coverage**: `pytest-cov` and identifying untested code paths.

---

## Part VII: Deployment and Production

### [Chapter 17: Caching and Performance](7.%20deployment_and_production/17.%20caching_and_performance.ipynb)
* **17.1 Why Caching?**: The performance impact of repeated DB queries and computations.
* **17.2 Flask-Caching**: In-memory cache, Redis backend, `@cache.cached()`, `@cache.memoize()`.
* **17.3 Rate Limiting**: `Flask-Limiter` — protecting APIs from abuse.
* **17.4 Query Optimisation**: N+1 problem, eager loading, and database indexes.
* **17.5 Profiling Flask Apps**: Finding bottlenecks with `flask-profiler` and `cProfile`.

### [Chapter 18: Deployment](7.%20deployment_and_production/18.%20deployment.ipynb)
* **18.1 The Production Stack**: Why you don't use Flask's dev server in production.
* **18.2 Gunicorn**: The WSGI server — workers, threads, and configuration.
* **18.3 Nginx as Reverse Proxy**: Serving static files, SSL termination, and load balancing.
* **18.4 Dockerising Flask**: `Dockerfile`, `docker-compose.yml` with Flask + PostgreSQL.
* **18.5 Cloud Deployment**: Deploying to Railway, Render, or AWS.
* **18.6 CI/CD with GitHub Actions**: Automated testing and deployment pipelines.

---

## Part VIII: Capstone Project

### [Chapter 19: Building a Full-Stack Flask Blog](8.%20capstone_project/19.%20building_a_fullstack_flask_blog.ipynb)
* **19.1 Project Overview**: Features, architecture, and what concepts from each chapter are used.
* **19.2 Project Setup**: Poetry, project structure, config, and database.
* **19.3 Models**: User, Post, Comment, Tag — relationships and schema.
* **19.4 Authentication**: Registration, login, profile, and role-based access.
* **19.5 Blog Features**: CRUD posts, rich text, pagination, search, and tagging.
* **19.6 REST API Layer**: Public API endpoints for the blog content.
* **19.7 Admin Panel**: Flask-Admin for content management.
* **19.8 Testing**: Full test suite with pytest.
* **19.9 Deployment**: Docker + GitHub Actions + cloud deploy.
* **19.10 What's Next?**: Extending the blog and your Flask learning path.

---

## Appendices
* **Appendix A**: Flask Cheat Sheet — quick reference for routes, templates, DB, auth.
* **Appendix B**: Flask Extension Directory — the best extensions and when to use them.
* **Appendix C**: Glossary — WSGI, ORM, CSRF, JWT, and other key terms defined.
* **Appendix D**: Recommended Resources — books, docs, courses, and communities.
