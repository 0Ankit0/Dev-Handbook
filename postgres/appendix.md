# Appendices

## Appendix A: `psql` Command Cheat Sheet
- Connection/session controls and authentication flags.
- Schema exploration commands (`\dt`, `\d+`, `\dn`, `\df`).
- Query execution helpers, formatting, and export patterns.

## Appendix B: SQL Style Guide (Recommended Conventions)
- Naming conventions for schemas/tables/columns/indexes.
- Query formatting, aliasing, and CTE usage standards.
- DDL migration writing conventions for safe rollouts.

## Appendix C: Index Selection Cheat Sheet
- B-tree/GIN/GiST/BRIN decision matrix by query shape.
- Composite and partial index design rules.
- Write amplification and maintenance cost trade-offs.

## Appendix D: EXPLAIN Plan Reading Patterns
- Node types, costs, buffers, and actual-vs-estimated diagnostics.
- Detecting seq scans, bad joins, and cardinality misestimates.
- Optimization loop: hypothesize, index/query change, re-measure.

## Appendix E: Lock Types and Common Symptoms
- Lock mode quick reference and blocking behavior.
- Typical contention scenarios and remediation steps.
- Monitoring blocked sessions and deadlock triage commands.

## Appendix F: Backup/Restore Runbook Templates
- Logical/physical backup workflows and retention policy.
- PITR prerequisites and restore validation checklist.
- Recovery communication and ownership model.

## Appendix G: Migration Patterns Catalog (Zero-Downtime)
- Expand-contract migrations and dual-write/read strategies.
- Backfill orchestration and cutover sequencing.
- Rollback-safe migration design.

## Appendix H: Common Postgres Error Messages and Meanings
- Constraint violations, transaction errors, connection failures.
- Diagnosis checklist and first-response playbook.

## Appendix I: Glossary
- Storage engine, planner, MVCC, vacuum, WAL, replication terminology.

## Appendix J: Recommended Reading / Official Docs Map
- Core docs by operations, performance, replication, security, extensions.
