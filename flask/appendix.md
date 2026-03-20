# Appendices

## Appendix A: Flask Cheat Sheet

### Application Setup
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

### Routing
```python
@app.route('/user/<int:id>', methods=['GET', 'POST'])
def user(id):
    return url_for('user', id=id)  # URL building
```

### Templates
```python
return render_template('index.html', title='Home', items=my_list)
```

### Request Object
```python
from flask import request
data = request.form['field']    # Form data
param = request.args.get('q')  # Query string
body = request.get_json()       # JSON body
file = request.files['upload']  # File upload
```

### SQLAlchemy Quick Reference
```python
# Create
obj = Model(field=value)
db.session.add(obj); db.session.commit()
# Read
Model.query.all()
Model.query.filter_by(name='Alice').first()
Model.query.get_or_404(id)
# Update
obj.field = new_value; db.session.commit()
# Delete
db.session.delete(obj); db.session.commit()
```

### Flask-Login
```python
@login_required          # Protect a route
current_user             # The logged-in user object
login_user(user)         # Log in
logout_user()            # Log out
```

### JWT (Flask-JWT-Extended)
```python
create_access_token(identity=user_id)
@jwt_required()
get_jwt_identity()
```

---

## Appendix B: Flask Extension Directory

| Extension | Purpose | Install |
|---|---|---|
| Flask-SQLAlchemy | ORM integration | `pip install flask-sqlalchemy` |
| Flask-Migrate | DB migrations (Alembic) | `pip install flask-migrate` |
| Flask-WTF | Forms + CSRF protection | `pip install flask-wtf` |
| Flask-Login | User session management | `pip install flask-login` |
| Flask-JWT-Extended | JWT authentication | `pip install flask-jwt-extended` |
| Flask-RESTX | REST APIs + Swagger | `pip install flask-restx` |
| Flask-Caching | Response & function caching | `pip install flask-caching` |
| Flask-Limiter | Rate limiting | `pip install flask-limiter` |
| Flask-CORS | Cross-origin resource sharing | `pip install flask-cors` |
| Flask-Mail | Email sending | `pip install flask-mail` |
| Flask-Admin | Admin interface | `pip install flask-admin` |
| Flask-Talisman | Security headers (HTTPS) | `pip install flask-talisman` |
| Gunicorn | Production WSGI server | `pip install gunicorn` |

---

## Appendix C: Glossary

**WSGI** (Web Server Gateway Interface) — The Python standard for how web servers communicate with web applications. Flask is a WSGI application.

**ORM** (Object-Relational Mapper) — A library that translates between Python objects and database rows. Flask-SQLAlchemy is an ORM wrapper around SQLAlchemy.

**CSRF** (Cross-Site Request Forgery) — An attack where a malicious site tricks a user's browser into making unwanted requests. Flask-WTF prevents this with hidden tokens.

**XSS** (Cross-Site Scripting) — An attack where malicious scripts are injected into web pages. Jinja2's autoescaping prevents this by default.

**JWT** (JSON Web Token) — A compact, URL-safe token format for transmitting claims between parties. Used for stateless API authentication.

**Blueprint** — A Flask object for organising a set of related routes, templates, and static files. Used to structure large applications.

**Application Factory** — A function (`create_app()`) that creates and configures a Flask application. Enables multiple configurations and easier testing.

**Jinja2** — Flask's default templating engine. Processes HTML files with special syntax for variables, loops, and inheritance.

**Werkzeug** — The WSGI utility library that Flask is built on. Handles routing, requests, responses, and development server.

**Migration** — A versioned script that modifies a database schema. Flask-Migrate uses Alembic to auto-generate and apply migrations.

**Gunicorn** — A Python WSGI HTTP server for running Flask in production. More stable and performant than Flask's built-in dev server.

**Reverse Proxy** — A server (like Nginx) that sits in front of your application, handling SSL, load balancing, and static file serving.

**Rate Limiting** — Restricting the number of requests a client can make in a given time window, protecting APIs from abuse.

**Eager Loading** — Loading related database objects in a single query to avoid the N+1 query problem.

---

## Appendix D: Recommended Resources

### Official Documentation
- [Flask Documentation](https://flask.palletsprojects.com/) — The definitive reference. Read the quickstart and tutorial first.
- [Jinja2 Documentation](https://jinja.palletsprojects.com/) — Complete template syntax reference.
- [Werkzeug Documentation](https://werkzeug.palletsprojects.com/) — Understanding what's under Flask's hood.
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) — Deep ORM and Core reference.

### Books
- *Flask Web Development* by Miguel Grinberg — The bible of Flask development. Comprehensive and practical.
- *The Flask Mega-Tutorial* (free online) by Miguel Grinberg — 23-part tutorial building a real blogging app.

### Courses and Tutorials
- Miguel Grinberg's Flask Mega-Tutorial (blog.miguelgrinberg.com) — Free, comprehensive, regularly updated.
- TestDriven.io Flask courses — Test-driven development approach.

### Communities
- [Flask Discord](https://discord.gg/pallets) — Official Pallets project Discord.
- [r/flask](https://www.reddit.com/r/flask/) — Active subreddit for Flask questions.
- [Stack Overflow `[flask]` tag](https://stackoverflow.com/questions/tagged/flask) — Huge archive of answered questions.

### What to Learn Next After This Handbook
1. **Advanced Flask** — Celery for background tasks, WebSockets with Flask-SocketIO.
2. **FastAPI** — If you need async or high-performance APIs, check the FastAPI handbook.
3. **Django** — If you need a batteries-included framework with built-in admin and auth.
4. **System Design** — How to architect scalable Flask applications.
5. **Cloud & DevOps** — AWS/GCP deployment, Kubernetes, and infrastructure as code.
