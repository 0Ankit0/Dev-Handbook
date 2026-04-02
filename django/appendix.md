# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: Django CLI Quick Reference

### Project and App Setup

```bash
# Create a new project (creates manage.py and project package)
django-admin startproject myproject

# Create a new app inside the project
cd myproject
python manage.py startapp myapp
```

### Development Server

```bash
python manage.py runserver              # Start on port 8000
python manage.py runserver 0.0.0.0:8080 # Custom host:port
```

### Database Migrations

```bash
# Generate migration files from model changes
python manage.py makemigrations

# Apply pending migrations to the database
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Preview the SQL a migration will run
python manage.py sqlmigrate myapp 0001

# Roll back to a specific migration (by name)
python manage.py migrate myapp 0002
```

### Shell and Data

```bash
# Interactive Python shell with Django context
python manage.py shell

# Flush all data from the database (destructive!)
python manage.py flush

# Load fixture data
python manage.py loaddata fixtures/initial_data.json

# Dump data to fixture
python manage.py dumpdata myapp.MyModel --indent=2 > fixtures/my_model.json
```

### Users and Auth

```bash
python manage.py createsuperuser
python manage.py changepassword username
```

### Static Files

```bash
python manage.py collectstatic      # Collect static files to STATIC_ROOT
python manage.py findstatic logo.png  # Find where a static file comes from
```

### Checks and Inspection

```bash
python manage.py check              # System check for common issues
python manage.py check --deploy     # Extra checks for production settings
python manage.py inspectdb          # Generate models from existing database
python manage.py diffsettings       # Show settings that differ from defaults
python manage.py dbshell            # Open a database shell (psql, sqlite3, etc.)
```

### Running Tests

```bash
python manage.py test                     # Run all tests
python manage.py test myapp               # Run tests for a single app
python manage.py test myapp.tests.MyTest  # Run a single test class
python manage.py test --keepdb            # Reuse test database (faster)
python manage.py test --verbosity=2       # Verbose output
```

---

## Appendix B: Settings Reference

### Core Settings Structure

```python
# settings/base.py — shared settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-do-not-use-in-production')

DEBUG = False  # Always False in base; override in dev

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your apps:
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'
```

### Database Configuration

```python
# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'mydb'),
        'USER': os.environ.get('DB_USER', 'myuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'CONN_MAX_AGE': 60,   # persistent connections
    }
}

# SQLite (development default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Cache Configuration

```python
# Redis (production)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://localhost:6379/1'),
    }
}

# LocMem (development / testing)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

### Production Security Settings

```python
# Production security settings (settings/production.py)
DEBUG = False

ALLOWED_HOSTS = ['mysite.com', 'www.mysite.com']

# HTTPS enforcement
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000        # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookie security
SESSION_COOKIE_SECURE = True          # Only send session cookie over HTTPS
CSRF_COOKIE_SECURE = True             # Only send CSRF cookie over HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Click-jacking protection
X_FRAME_OPTIONS = 'DENY'

# Content-type sniffing protection
SECURE_CONTENT_TYPE_NOSNIFF = True
```

---

## Appendix C: ORM Quick Reference

### Basic Queries

```python
# Create
user = User.objects.create(username='alice', email='alice@example.com')

# Retrieve
user = User.objects.get(id=1)        # Raises DoesNotExist if not found
user = User.objects.get(pk=1)        # pk is alias for primary key

# Filter (returns QuerySet, not single object)
users = User.objects.filter(is_active=True)
users = User.objects.exclude(is_active=False)

# Chaining filters (AND)
users = User.objects.filter(is_active=True).filter(role='admin')

# OR filter using Q objects
from django.db.models import Q
users = User.objects.filter(Q(role='admin') | Q(is_superuser=True))

# First / last
user = User.objects.filter(is_active=True).first()
user = User.objects.order_by('-created_at').first()

# Count
total = User.objects.count()
active = User.objects.filter(is_active=True).count()

# Exists (more efficient than count > 0)
if User.objects.filter(email='alice@example.com').exists():
    ...

# Update
User.objects.filter(is_active=False).update(is_active=True)

# Delete
User.objects.filter(created_at__lt=cutoff_date).delete()
```

### Field Lookups

```python
# Exact match (default)
User.objects.filter(username='alice')        # username = 'alice'
User.objects.filter(username__exact='alice') # same

# Contains (case-sensitive)
User.objects.filter(email__contains='@gmail')

# icontains (case-insensitive)
User.objects.filter(name__icontains='smith')

# Starts/ends with
User.objects.filter(username__startswith='admin')

# Greater/less than
User.objects.filter(age__gte=18)       # age >= 18
User.objects.filter(created_at__lt=date)

# In list
User.objects.filter(id__in=[1, 2, 3])

# Range
User.objects.filter(created_at__date__range=(start, end))

# Is null
User.objects.filter(deleted_at__isnull=True)

# Related field lookup (double underscore crosses ForeignKey)
Order.objects.filter(user__email='alice@example.com')
```

### Optimization

```python
# select_related — reduces queries for ForeignKey (single query with JOIN)
orders = Order.objects.select_related('user', 'product').all()

# prefetch_related — reduces queries for ManyToMany / reverse FK (2 queries)
users = User.objects.prefetch_related('orders').all()

# values() — return dicts instead of model instances (lighter)
emails = User.objects.values('email', 'name')

# values_list() — return tuples
ids = User.objects.values_list('id', flat=True)

# only() — fetch only specified fields
users = User.objects.only('id', 'email')

# defer() — exclude fields from initial query
users = User.objects.defer('bio', 'avatar')

# Annotate with aggregation
from django.db.models import Count, Avg
users = User.objects.annotate(order_count=Count('orders'))

# Bulk operations (avoid N queries in a loop)
User.objects.bulk_create([User(email=e) for e in email_list])
User.objects.bulk_update(users, ['is_active'])
```

---

## Appendix D: Testing Patterns

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfileViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_profile_requires_login(self):
        url = reverse('user-profile')
        response = self.client.get(url)
        self.assertRedirects(response, f'/login/?next={url}')

    def test_authenticated_user_can_view_profile(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_update_profile(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('user-profile-edit'),
            {'email': 'new@example.com'},
        )
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'new@example.com')
```

```python
# Factory Boy — for creating test objects cleanly
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass')

# Usage
user = UserFactory()
user = UserFactory(email='custom@example.com')
```

---

## Appendix E: Common Errors and Solutions

| Error | Likely Cause | Solution |
|-------|-------------|----------|
| `No module named 'myapp'` | App not in INSTALLED_APPS | Add `'myapp'` to INSTALLED_APPS |
| `django.core.exceptions.ImproperlyConfigured` | Missing required setting | Check for missing `SECRET_KEY`, `DATABASES`, etc. |
| `OperationalError: no such table` | Migration not applied | Run `python manage.py migrate` |
| `RelatedObjectDoesNotExist` | Accessing a OneToOne relation that doesn't exist | Check with `hasattr(user, 'profile')` or use `try/except` |
| `CSRF verification failed` | Missing CSRF token in POST form | Add `{% csrf_token %}` to form; or use `@csrf_exempt` for APIs |
| `django.db.utils.IntegrityError` | Violating a unique or not-null constraint | Check model constraints and input validation |
| `SuspiciousOperation: Invalid HTTP_HOST header` | Request from a host not in ALLOWED_HOSTS | Add the host to `ALLOWED_HOSTS` in settings |
| `DisallowedHost` | Same as above | Same fix |
| Migration conflicts | Two developers created migrations at the same number | Run `python manage.py makemigrations --merge` |

---

## Appendix F: Glossary

**ORM (Object-Relational Mapper)**
Django's database abstraction layer. Lets you define database tables as Python classes (`Model`) and query them with Python methods instead of raw SQL. Handles SQL generation, connection management, and type conversion.

**QuerySet**
The result of an ORM query. It's lazy — the database query is not executed until you iterate, call `.list()`, slice it, or call `.count()`. Supports chaining (`.filter().order_by().values()`).

**Migration**
A Python file generated by `makemigrations` that describes a schema change (create table, add column, etc.). Migrations are tracked in the `django_migrations` database table, making them reproducible and version-controlled.

**WSGI / ASGI**
WSGI (Web Server Gateway Interface) is the traditional interface between Django and a web server (Gunicorn). ASGI (Asynchronous Server Gateway Interface) is the async-capable version, required for WebSockets and async views.

**Middleware**
Classes that process every request before it reaches a view and every response before it's sent to the client. Used for security headers, session loading, authentication checking, and logging.

**Signals**
A Django mechanism for decoupled notifications. One part of the code sends a signal (e.g., `post_save`), and any number of receivers can respond. Useful but can make code harder to trace — use sparingly.

**Template Context**
The dictionary of variables passed to a template from a view. Templates render by substituting `{{ variable }}` expressions with their values from the context.

---

## Appendix G: Resources

- [Django Docs](https://docs.djangoproject.com/) — the official, comprehensive reference
- [Django ORM Cookbook](https://books.agiliq.com/projects/django-orm-cookbook/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x) — best practices book
- [Django REST Framework Docs](https://www.django-rest-framework.org/) — for building APIs
