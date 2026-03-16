# Appendices

## Appendix A: Python Type Hints Cheat Sheet
- Built-in types, generics, unions, literals, typed dicts.
- FastAPI-specific typing patterns for params, bodies, and dependencies.
- Common pitfalls (`Optional`, mutable defaults, forward references).

## Appendix B: Migration Guide: Flask/Django to FastAPI
- Incremental migration plan (strangler pattern).
- Mapping request lifecycle and middleware concepts.
- Porting validation layer to Pydantic with contract parity checks.
- Rollout strategy with dual-run and compatibility tests.

## Appendix C: FastAPI CLI Reference
- Development server startup variants and production worker patterns.
- OpenAPI generation/export workflow.
- Typical tooling commands for lint, test, type check, and packaging.

## Appendix D: Common Pitfalls and FAQ
- Async/sync mixing and blocking I/O in event loop.
- Dependency injection scope confusion and resource leaks.
- Inconsistent error shapes and status code misuse.
- CORS/auth misconfiguration and security hardening reminders.

## Glossary
- ASGI, coroutine, path operation, dependency injection, OpenAPI, JSON Schema.
