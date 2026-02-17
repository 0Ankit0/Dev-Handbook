# Django Mastery Workbook — Table of Contents (Beginner → Advanced, Industry-Standard)

## Part I — Foundations (Setup, Web Basics, Django Mental Model)

### [1. Web Development Essentials (Crash Course)](1.%20Foundations/1.%20web_dev_essentials.ipynb)
1. HTTP/HTTPS, request–response lifecycle
2. URLs, routing, query strings
3. HTML/CSS/JS basics (what Django renders vs what frontend frameworks do)
4. Cookies, sessions, local storage (what matters for Django)
5. REST basics and when you need APIs
6. Security basics: same-origin policy, CSRF, XSS, SQL injection (high-level)

### [2. Python for Django (Practical)](1.%20Foundations/2.%20python_for_django.ipynb)
1. Virtual environments and dependency management
2. Python packaging basics
3. Data structures and comprehensions
4. Functions, modules, imports
5. Classes, dataclasses, typing (just enough)
6. Exceptions and logging basics
7. File I/O and environment variables

### [3. Developer Tooling and Workflow (Industry Standard)](1.%20Foundations/3.%20developer_tooling_and_workflow.ipynb)
1. Git fundamentals and branching workflow
2. Editor/IDE setup (PyCharm/VS Code)
3. Linting/formatting: Ruff/Flake8, Black, isort (recommended baseline)
4. Pre-commit hooks
5. Debugging: breakpoints, Django Debug Toolbar
6. Docs reading strategy: how to use Django docs effectively

### [4. Installing Django + First Project (The Right Way)](1.%20Foundations/4.%20installing_django_plus_first_project.ipynb)
1. Choosing Django version (LTS vs latest)
2. Creating a project and app (project vs app mental model)
3. Running the dev server and exploring settings
4. Understanding manage.py and django-admin
5. Initial project layout and “what goes where”
6. Workbook Lab: “Hello Django” minimal page + health endpoint

### [5. Django Architecture Overview](1.%20Foundations/5.%20django_architecture_overview.ipynb)
1. MTV pattern (Model–Template–View) and how it maps to MVC
2. Request flow: URLconf → view → template/response
3. Settings, apps, middleware, WSGI/ASGI overview
4. Static vs media files
5. Environments: dev/staging/prod overview

---

## Part II — Core Django (CRUD Web Apps Done Right)

### [6. URL Routing and Views (Function-Based and Class-Based)](2.%20Core_Django/6.%20url_routing_and_views.ipynb)
1. URL patterns, path converters, namespacing
2. Function-based views (FBVs): request, response, shortcuts
3. Class-based views (CBVs): TemplateView, ListView, DetailView, FormView
4. When to choose FBV vs CBV
5. Error views (404/500) and custom handlers
6. Lab: build a small pages app with named routes and templates

### [7. Templates (Django Templating Language)](2.%20Core_Django/7.%20templates.ipynb)
1. Template discovery and loaders
2. Variables, filters, tags, template inheritance
3. Includes and partials
4. Context processors
5. Template best practices and avoiding logic-in-templates
6. Custom template filters and tags
7. Lab: build a reusable base layout + navigation + messages

### [8. Models and Database Basics](2.%20Core_Django/8.%20models_and_database_basics.ipynb)
1. Configuring a database (SQLite vs PostgreSQL)
2. Defining models: fields, options, Meta
3. Migrations: makemigrations, migrate, squashing, data migrations
4. Relationships: OneToOne, ForeignKey, ManyToMany
5. Constraints and validation (unique, check constraints)
6. Model methods and properties
7. Lab: design models for a blog/news app

### [9. Django ORM (Querying Like a Pro)](2.%20Core_Django/9.%20django_orm.ipynb)
1. QuerySets, laziness, evaluation
2. Filtering, ordering, slicing
3. Lookups, Q objects, F expressions
4. Aggregation and annotation
5. select_related vs prefetch_related
6. Transactions and atomicity basics
7. Raw SQL: when/why and safe usage
8. Lab: solve ORM query exercises + performance comparison

### [10. Admin Site (Productivity Power Tool)](2.%20Core_Django/10.%20admin_site.ipynb)
1. Registering models
2. List display, search, filters, ordering
3. Fieldsets, readonly fields, custom forms
4. Inlines for related objects
5. Custom actions
6. Admin security and audit concerns
7. Lab: build a polished admin for content management

### [11. Forms (HTML Forms, Validation, UX)](2.%20Core_Django/11.%20forms.ipynb)
1. Form classes and fields
2. Validation: clean(), clean_field, non-field errors
3. ModelForms
4. Handling file uploads
5. Form rendering strategies and styling
6. Messages framework for UX feedback
7. Lab: create/edit flows for posts with validation + uploads

### [12. Authentication and Authorization (Django Auth System)](2.%20Core_Django/12.%20authentication_and_authorization.ipynb)
1. Users, passwords, authentication backends
2. Login/logout, password reset flow
3. Permissions and groups
4. User model options: custom user model (best practice timing)
5. Session authentication basics
6. Lab: implement auth screens + permissioned views

### [13. Middleware, Sessions, Messages, and Cookies](2.%20Core_Django/13.%20middleware_sessions_messages_and_cookies.ipynb)
1. What middleware is and how it works
2. Built-in middleware overview
3. Sessions: storage backends and security
4. Messages framework in depth
5. Writing custom middleware (logging, timing, headers)
6. Lab: request timing middleware + per-user preferences

### [14. Static Files and Media Files](2.%20Core_Django/14.%20static_files_and_media_files.ipynb)
1. Static files setup and conventions
2. collectstatic and deployment implications
3. Media uploads: storage backends and security
4. Image handling basics (validation, size limits)
5. Lab: user avatar upload + serving media in dev

### [15. Email and Notifications](2.%20Core_Django/15.%20email_and_notifications.ipynb)
1. Email backend configuration (dev vs prod)
2. Transactional emails: password reset, verification
3. Templates for emails (text + HTML)
4. Deliverability basics and provider integration
5. Lab: verification email + notification preferences

---

## Part III — Building Real Projects (From Small to Production-Ready)

### [16. Project 1 (Beginner): Blog/Content Site](3.%20Building_real_projects/16.%20blog_site.ipynb)
1. Requirements and user stories
2. Data model and migration plan
3. Public views and templates
4. Admin management
5. Comments, tags, pagination
6. Basic SEO: sitemaps, robots, meta tags
7. Final checklist and review questions

### [17. Project 2 (Intermediate): Multi-User App (Tasks/CRM/Inventory)](3.%20Building_real_projects/17.%20team_tasks.ipynb)
1. Roles and permissions
2. CRUD with ownership rules
3. Search and filtering UI
4. Audit fields (created_by, updated_by), history basics
5. Exporting data (CSV)
6. Final checklist and review questions

---

## Part IV — Professional Django (Testing, Security, Performance, Maintainability)

### 18. Testing (Unit, Integration, E2E)
1. Django test runner and structure
2. Model tests, form tests, view tests
3. Client, RequestFactory, reverse()
4. Fixtures vs factories (factory_boy)
5. Mocking external services
6. Coverage goals and test pyramid
7. Lab: write a complete test suite for one app

### [19. Security (OWASP-Aligned)](4.%20Professional_Django/19.%20security.ipynb)
1. SECRET_KEY and environment config
2. Debug mode risks
3. CSRF protection (how it works)
4. XSS prevention in templates
5. SQL injection and ORM safety
6. Authentication hardening (password policy, 2FA concepts)
7. Security headers (CSP, HSTS, X-Frame-Options)
8. Secure file uploads
9. Dependency security and patching
10. Lab: security review checklist + fixes

### [20. Performance and Scaling Fundamentals](4.%20Professional_Django/20.%20performance_and_scaling_fundamentals.ipynb)
1. Measuring performance: profiling basics
2. ORM optimization patterns and anti-patterns
3. N+1 queries and how to prevent them
4. Indexing basics (PostgreSQL focus)
5. Caching: per-view, template fragment, low-level cache
6. Pagination strategies
7. Lab: optimize slow pages + add caching safely

### [21. Logging, Monitoring, and Observability](4.%20Professional_Django/21.%20logging_monitoring_scaling_foundations.ipynb)
1. Python logging configuration best practices
2. Structured logging
3. Error tracking (e.g., Sentry concepts)
4. Metrics and health checks
5. Tracing basics
6. Lab: add production-grade logging + error reporting hooks

### [22. Architecture and Code Organization](4.%20Professional_Django/22.%20architecture_and_code_organization.ipynb)
1. App boundaries and modular design
2. Service layer vs “fat models” vs “fat views”
3. Reusable apps, internal packages
4. Settings management (split settings, env vars)
5. Dependency inversion and testability
6. Lab: refactor a feature into a maintainable architecture

---

## Part V — APIs with Django (Django REST Framework + Beyond)

### [23. API Fundamentals](5.%20Apis_with_Django/23.%20api_fundamentals.ipynb)
1. REST principles, resources, representation
2. Authentication methods (session, token, JWT concepts)
3. Pagination, filtering, ordering
4. Versioning and backwards compatibility
5. API documentation basics (OpenAPI)

### [24. Django REST Framework (DRF) Core](5.%20Apis_with_Django/24.%20django_rest_framework.ipynb)
1. Setting up DRF in a Django project
2. Serializers: ModelSerializer vs custom
3. Views: APIView, GenericAPIView, ViewSets
4. Routers and URL configuration
5. Permissions and throttling
6. Validation and error responses
7. Lab: build CRUD API for your project models

### [25. DRF Advanced Patterns](5.%20Apis_with_Django/25.%20drf_advanced_patterns.ipynb)
1. Nested relationships and writable nested serializers
2. Performance: select_related/prefetch_related with DRF
3. Custom permissions and object-level authorization
4. File uploads in APIs
5. Background tasks for long-running API work
6. Testing DRF APIs (APITestCase, APIClient)
7. Lab: production-grade API endpoint set + tests

### [26. API Security and Production Concerns](5.%20Apis_with_Django/26.%20api_security_and_production_concerns.ipynb)
1. Rate limiting strategies
2. CORS configuration
3. Security headers for APIs
4. Secrets management and key rotation
5. Lab: harden your API + add documentation

---

## Part VI — Async, Realtime, and Background Work

### [27. ASGI, Async Views, and Django’s Async Capabilities](6.%20Async_realtime_and_background_work/27.%20asgi_async_views_and_async_capabilities.ipynb)
1. WSGI vs ASGI
2. Async views: when they help, when they don’t
3. Async ORM status and practical patterns
4. Streaming responses basics
5. Lab: add an async endpoint safely

### [28. Realtime with WebSockets (Django Channels)](6.%20Async_realtime_and_background_work/28.%20realtime_with_websocets.ipynb)
1. Channels concepts: consumers, routing, channel layer
2. Presence, chat, notifications
3. Scaling channels with Redis
4. Lab: realtime notifications for your app

### [29. Background Tasks (Celery/RQ Concepts)](6.%20Async_realtime_and_background_work/29.%20background_tasks.ipynb)
1. When to use background jobs
2. Celery architecture: broker, workers, result backend
3. Retries, idempotency, task timeouts
4. Scheduling periodic tasks
5. Lab: email sending + report generation in background

---

## Part VII — Data, Integrations, and Advanced ORM

### [30. PostgreSQL for Django (Practical Database Mastery)](7.%20Data_integrations_and_advanced_orm/30.%20postgres_for_django.ipynb)
1. Choosing PostgreSQL and configuring properly
2. Index types and query planning basics
3. Transactions, isolation levels, locking
4. Constraints and data integrity
5. Full-text search basics (PostgreSQL)
6. Lab: add indexes + measure query improvements

### [31. Advanced Migrations and Data Management](7.%20Data_integrations_and_advanced_orm/31.%20advanced_migrations_and_data_management.ipynb)
1. Safe migrations in production
2. Data migrations patterns
3. Backfilling and large table strategies
4. Rollbacks and “zero downtime” considerations
5. Lab: perform a safe schema change with backfill

### [32. Advanced Model Patterns](7.%20Data_integrations_and_advanced_orm/32.%20advanced_model_patterns.ipynb)
1. Abstract base classes, proxy models
2. Generic relations (ContentTypes)
3. Multi-table inheritance pitfalls
4. Soft deletes and audit logging
5. Lab: implement audit trail + soft delete safely

### [33. Search, Files, and External Services](7.%20Data_integrations_and_advanced_orm/33.%20search_files_and_external_services.ipynb)
1. Integrating external APIs (requests, timeouts, retries)
2. Webhooks: verification, signatures, replay protection
3. File storage: S3-like backends and security
4. Lab: webhook receiver + file storage integration

---

## Part VIII — Frontend Integration (Modern Django in Real Teams)

### [34. Django + HTMX (Server-Rendered Interactivity)](8.%20Frontend_integration/34.%20django_plus_htmx.ipynb)
1. Where HTMX fits
2. Partial rendering patterns
3. Form submissions and validation UX
4. Lab: convert a CRUD page to HTMX interactions

### [35. Django + SPA/Frontend Frameworks (React/Vue/Next)](8.%20Frontend_integration/35.%20django_plus_frontend_frameworks.ipynb)
1. Architecture options (monolith, split frontend/backend)
2. Auth patterns (cookies vs tokens)
3. CORS, CSRF, and secure deployment patterns
4. Lab: integrate a small frontend with a DRF backend

---

## Part IX — Deployment and Production Operations (Real-World Standard)

### [36. Production Readiness Checklist](9.%20Deployment_and_production_operations/36.%20production_readiness_checklist.ipynb)
1. Settings hardening
2. Allowed hosts, CSRF trusted origins
3. Static/media strategy
4. Database backups and migrations plan
5. Lab: create your production readiness document

### [37. Deployment Options (Concepts + Practical Paths)](9.%20Deployment_and_production_operations/37.%20deployment_options.ipynb)
1. Traditional VPS: Nginx + Gunicorn/Uvicorn
2. Platform-as-a-Service: Render/Heroku-like concepts
3. Containers: Docker fundamentals for Django
4. Lab: deploy a project to one chosen platform

### [38. CI/CD (Automation that Professionals Expect)](9.%20Deployment_and_production_operations/38.%20ci_cd.ipynb)
1. Tests in CI
2. Linting/formatting gates
3. Build artifacts, migrations, deployment steps
4. Secrets in CI
5. Lab: build a CI pipeline for your repo

### [39. Caching, CDN, and Performance in Production](9.%20Deployment_and_production_operations/39.%20caching_cdn_and_performance_in_production.ipynb)
1. Redis caching patterns
2. CDN for static assets
3. Compression, ETags, cache headers
4. Lab: production caching + CDN checklist

### [40. Operations: Backups, Rollbacks, Incident Response](9.%20Deployment_and_production_operations/40.%20operations.ipynb)
1. Backup strategy (DB + media)
2. Restore drills
3. Rollback patterns
4. Incident response basics and runbooks
5. Lab: write a rollback + restore runbook

---

## Part X — Advanced Topics (What Separates “Good” from “Expert”)

### [41. Multi-Tenancy Patterns (SaaS Architectures)](10.%20Advanced_topics/41.%20multi-tenancy_patterns.ipynb)
1. Tenant isolation approaches: DB-per-tenant, schema-per-tenant, shared DB
2. Data access boundaries and security
3. Tenant-aware middleware and routing
4. Lab: implement a basic tenant model + tenant scoping

### [42. Advanced Authorization (Policy-Based Access)](10.%20Advanced_topics/42.%20advanced_authorization.ipynb)
1. Object-level permissions patterns
2. Role-based vs attribute-based access control
3. Audit and compliance considerations
4. Lab: implement policy checks and tests

### [43. Internationalization (i18n) and Localization (l10n)](10.%20Advanced_topics/43.%20internationalization_and_localization.ipynb)
1. Translation workflow
2. Locale formatting and time zones
3. Lab: multilingual pages + translated admin

### [44. Accessibility and UX Quality (Professional Baseline)](10.%20Advanced_topics/44.%20accessibility_and_ux_quality.ipynb)
1. Forms accessibility basics
2. Error messaging and focus management
3. Lab: accessibility audit checklist on your templates

### [45. Advanced Admin and Internal Tools](10.%20Advanced_topics/45.advanced_admin_and_internal_tools.ipynb)
1. Admin customization patterns
2. Admin performance optimization
3. Custom admin views and dashboards
4. Lab: build an internal reporting dashboard

### [46. Advanced Testing and Quality Engineering](10.%20Advanced_topics/46.%20advanced_testing_and_quality_engineering.ipynb)
1. Property-based testing concepts
2. Contract testing for APIs
3. Load testing basics
4. Lab: load test one endpoint and interpret results

### [47. Managing Large Codebases](10.%20Advanced_topics/47.%20managing_large_codebases.ipynb)
1. Monolith modularization strategies
2. Dependency boundaries and app APIs
3. Tech debt management
4. Lab: define architecture rules and enforce them

---

## Capstone — End-to-End Professional Project (Choose One Track)

### [48. Capstone A: Content Platform (Publishing + Membership)](11.%20Projects/48.%20content_platform.ipynb)
1. Membership tiers, payments integration (concepts)
2. Protected content, rate limiting
3. Editorial workflows
4. Deployment + monitoring + security review

### [49. Capstone B: SaaS CRUD Platform (Multi-Tenant + API)](11.%20Projects/49.%20saas_crud_platform.ipynb)
1. Multi-tenant architecture
2. DRF API + docs + versioning
3. Background jobs + email notifications
4. CI/CD + production runbooks

### [50. Capstone C: Realtime App (Notifications/Chat)](11.%20Projects/50.%20realtime_app.ipynb)
1. Channels + Redis
2. Realtime authorization
3. Scaling considerations
4. Observability and incident readiness

---

## Appendices (Reference + Checklists)
A. Django Commands and Project Skeleton Reference  
B. Settings Reference (Dev/Staging/Prod) Template  
C. Security Checklist (OWASP-inspired)  
D. ORM Optimization Cheat Sheet  
E. Testing Checklist + Sample Patterns  
F. Deployment Checklist (Nginx/Gunicorn/Uvicorn/ASGI)  
G. Common Errors and Debugging Playbook  
H. Glossary (Django + Web + DevOps terms)  
I. Recommended Reading (Official Docs + Key Topics)

---
