# Appendices

## Appendix A: Django Commands and Project Skeleton Reference
- Project bootstrap (`startproject`, `startapp`) and app layout conventions.
- Migration lifecycle commands and safe deployment sequence.
- Static/media collection and environment-specific startup commands.
- Management command patterns for operational tasks.

## Appendix B: Settings Reference (Dev/Staging/Prod) Template
- Base settings plus environment overlays and secret injection.
- Database/cache/email/storage configuration matrix.
- Security toggles per environment (HSTS, SSL redirect, cookie flags).
- Logging, observability, and feature-flag configuration.

## Appendix C: Security Checklist (OWASP-inspired)
- Authentication/session hardening and brute-force protections.
- CSRF/XSS/clickjacking protections and template hygiene.
- File upload safety (type checks, storage isolation, scanning).
- Dependency and vulnerability management workflow.

## Appendix D: ORM Optimization Cheat Sheet
- `select_related`/`prefetch_related` decision guide.
- Query plan inspection and index alignment strategy.
- Bulk operations and transaction boundaries.
- Avoiding N+1 queries in templates and APIs.

## Appendix E: Testing Checklist + Sample Patterns
- Unit, integration, and end-to-end boundary definitions.
- Fixture/factory strategy and deterministic test data.
- Permission and security regression tests.
- Performance and smoke tests for critical endpoints.

## Appendix F: Deployment Checklist (Nginx/Gunicorn/Uvicorn/ASGI)
- Build artifact, migration, and static collection order.
- Health checks, readiness, and rollback gating.
- Reverse-proxy headers, timeouts, and TLS configuration.
- Post-deploy verification and canary validation.

## Appendix G: Common Errors and Debugging Playbook
- Migration conflicts, import cycles, and settings misconfiguration.
- Database deadlocks/timeouts and remediation patterns.
- Static/media serving issues and cache invalidation steps.
- Incident triage flow with owner escalation path.

## Appendix H: Glossary (Django + Web + DevOps terms)
- Framework, HTTP, deployment, and observability terms.
- Security and scaling terminology for production operations.

## Appendix I: Recommended Reading (Official Docs + Key Topics)
- Official Django documentation map by competency level.
- Curated references for ORM, security, async, and deployment.
