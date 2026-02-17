## PostgreSQL Developer Handbook — Table of Contents (Simple → Advanced)

### Front Matter
- Foreword
- Who This Book Is For (Developers, Data Engineers, DBAs, SREs)
- What You’ll Be Able to Do After Finishing
- How to Use This Book (progressive path, labs, reference sections)
- Conventions Used (SQL style, psql, OS notes, diagrams)
- Companion Repo / Sample Dataset Overview

---

## Part I — Foundations (Getting Oriented)

### [1. What PostgreSQL Is (and Isn’t)](1.%20Foundations/1.%20Introduction.ipynb)
- PostgreSQL philosophy and strengths
- Relational model refresher (tables, keys, constraints)
- ACID properties in practical terms
- When to use Postgres vs alternatives
- Postgres ecosystem and extensions overview

### [2. Installing PostgreSQL (Local + Team Standards)](1.%20Foundations/2.%20installing_postgres.ipynb)
- Installation options (package manager, installer, Docker, cloud)
- Choosing a Postgres version (LTS mindset, upgrade cadence)
- Directory layout and key files
- Environment setup checklist (dev vs prod parity)

### [3. First Steps with `psql` (Your Primary Interface)](1.%20Foundations/3.%20first_steps_with_psql.ipynb)
- Connecting, roles, databases, schemas
- `psql` essentials (meta-commands, variables, scripting)
- Running SQL files and repeatable workflows
- Output formatting, timing, error handling

### [4. Core Concepts You Must Get Right Early](1.%20Foundations/4.%20core_concepts_to_get_right_early.ipynb)
- Cluster vs database vs schema
- Tables vs views vs materialized views
- Rows, pages, heap, TOAST (high-level)
- System catalogs basics (`pg_catalog`, `information_schema`)
- Naming conventions and SQL style guide

---

## Part II — SQL Essentials (Correctness First)

### [5. Data Types Done Right](2.%20SQL_essentials/5.%20data_types_done_right.ipynb)
- Numeric types, precision, money pitfalls
- Text types, collations, case-sensitivity considerations
- Dates/times, time zones, intervals
- UUID, JSON/JSONB, arrays, ranges, enums
- Choosing types for correctness and performance

### [6. Creating Tables and Constraints](2.%20SQL_essentials/6.%20creating_tables_and_constraints.ipynb)
- `CREATE TABLE` patterns
- `PRIMARY KEY`, `UNIQUE`, `CHECK`, `FOREIGN KEY`
- `NOT NULL` and domain constraints
- Generated columns (where appropriate)
- Common modeling mistakes and fixes

### [7. CRUD and Filtering](2.%20SQL_essentials/7.%20crud_and_filtering.ipynb)
- `INSERT`, `UPDATE`, `DELETE`, `RETURNING`
- `WHERE` logic, `NULL` semantics, three-valued logic
- Sorting and pagination (including keyset pagination)
- Working safely with parameters (SQL injection prevention)

### [8. Joins, Aggregation, and Set Logic](2.%20SQL_essentials/8.%20joins_aggregation_and_set_logic.ipynb)
- Inner/outer joins and join pitfalls
- Grouping, `HAVING`, aggregates
- `UNION`, `INTERSECT`, `EXCEPT`
- Window functions (intro → practical patterns)

### [9. Functions, Expressions, and Common Patterns](2.%20SQL_essentials/9.%20functions_expressions_and_common_patterns.ipynb)
- String/date/JSON functions
- `CASE`, `COALESCE`, `NULLIF`
- CTEs (`WITH`) and recursive CTEs (intro)
- LATERAL joins (when and why)

---

## Part III — Schema Design for Real Applications

### [10. Data Modeling for OLTP Systems](3.%20Schema_design_for_real_applications/10.%20data_modeling_for_oltp_systems.ipynb)
- Normalization vs pragmatic denormalization
- Natural vs surrogate keys
- Many-to-many tables and association metadata
- Soft deletes, audit fields, and temporal considerations

### [11. Working with Schemas (Namespaces)](3.%20Schema_design_for_real_applications/11.%20working_with_schemas.ipynb)
- Multi-schema patterns (tenancy, bounded contexts)
- Search path and safety
- Schema ownership and permissions

### [12. Views and Materialized Views](3.%20Schema_design_for_real_applications/12.%20views_and_materialized_views.ipynb)
- When a view is appropriate
- Security barrier views (conceptual)
- Materialized view refresh strategies
- Indexing materialized views

### [13. Partitioning (Declarative)](3.%20Schema_design_for_real_applications/13.%20partitioning_declarative.ipynb)
- When partitioning helps (and when it doesn’t)
- Range/list/hash partitioning
- Partition keys and pruning
- Managing partitions over time (rolling windows)
- Partition-wise joins/aggregates (conceptual + practical)

---

## Part IV — Indexing and Query Performance (The Practical Core)

### [14. How PostgreSQL Executes Queries](4.%20Indexing_and_query_performance/14.%20how_postgres_executes_queries.ipynb)
- Planner vs executor
- Statistics, selectivity, and cost model basics
- Common scan types (seq, index, bitmap)
- Join strategies (nested loop, hash join, merge join)

### [15. Index Fundamentals](4.%20Indexing_and_query_performance/15.%20index_fundamentals.ipynb)
- B-tree indexes: the default workhorse
- Multi-column index ordering and prefix rules
- Covering indexes (`INCLUDE`)
- When indexes hurt (write amplification, bloat)

### [16. Advanced Index Types (When You Need Them)](4.%20Indexing_and_query_performance/16.%20advanced_index_types.ipynb)
- Hash indexes (use cases)
- GIN / GiST (arrays, JSONB, full text, ranges)
- BRIN (large tables, naturally ordered data)
- Partial indexes
- Expression indexes
- Index-only scans and visibility map implications

### [17. EXPLAIN Like You Mean It](4.%20Indexing_and_query_performance/17.%20explain_like_you_mean_it.ipynb)
- `EXPLAIN` vs `EXPLAIN ANALYZE`
- Reading plans reliably
- Common anti-patterns: functions in predicates, mismatched types
- Parameter sniffing-like issues and plan stability
- Measuring improvements correctly

### [18. Performance Tuning Playbook (Developer-Focused)](4.%20Indexing_and_query_performance/18.%20performance_tuning_playbook.ipynb)
- Query refactoring patterns
- Index selection workflow
- Batch operations and minimizing round trips
- Avoiding N+1 queries at the SQL layer
- Practical checklist for slow endpoints

---

## Part V — Transactions, Concurrency, and Correctness Under Load

### [19. Transactions and MVCC](5.%20Transactions_concurrency_and_correctness_under_load/19.%20transactions_and_mvcc.ipynb)
- What MVCC means in practice
- Autocommit vs explicit transactions
- Transaction boundaries in application code
- Write skew and anomaly intuition

### [20. Isolation Levels and Locking](5.%20Transactions_concurrency_and_correctness_under_load/20.%20isolation_levels_and_locking.ipynb)
- `READ COMMITTED` vs `REPEATABLE READ` vs `SERIALIZABLE`
- Row locks, table locks, advisory locks
- Deadlocks: causes, detection, prevention
- `SELECT ... FOR UPDATE` patterns (and pitfalls)

### [21. Sequences and ID Generation](5.%20Transactions_concurrency_and_correctness_under_load/21.%20sequences_and_id_generation.ipynb)
- `SERIAL` vs `IDENTITY`
- Sequence caching and gaps
- UUID strategies and index implications
- Distributed systems considerations

---

## Part VI — Programmability (Database Logic Done Safely)

### [22. SQL Functions and Procedures](6.%20Programmability/22.%20sql_functions_and_procedures.ipynb)
- Creating stable, immutable, volatile functions
- Procedures vs functions (transactions and side effects)
- Error handling patterns
- Security definer functions (safe usage)

### [23. PL/pgSQL Essentials](6.%20Programmability/23.%20plpgsql_essentials.ipynb)
- Variables, control flow, records
- Cursors (when needed)
- Performance considerations in procedural code

### [24. Triggers (Use Sparingly, Use Well)](6.%20Programmability/24.%20triggers.ipynb)
- Trigger types and timing
- Auditing, denormalized cache updates
- Avoiding hidden complexity
- Testing trigger behavior

### [25. Extensions and Ecosystem](6.%20Programmability/25.%20extensions_and_ecosystem.ipynb)
- What extensions are and how to manage them
- Commonly used extensions (e.g., `pgcrypto`, `uuid-ossp`, `citext`)
- Versioning and migration implications
- Policy for adopting extensions in teams

---

## Part VII — Security and Access Control (Industry Baselines)

### [26. Roles, Privileges, and Ownership](7.%20security_and_access_control_industry_baselines/26.%20roles_privileges_and_ownership.ipynb)
- Role design (app role, readonly role, migration role)
- GRANT/REVOKE and default privileges
- Object ownership and schema hygiene
- Least privilege checklist

### [27. Authentication, `pg_hba.conf`, and TLS](7.%20security_and_access_control_industry_baselines/27.%20authentication_pg_hbaconf_and_tls.ipynb)
- Auth methods (scram, peer, cert-based)
- TLS configuration basics
- Secure connection strings and secret management

### [28. Application Security Patterns](7.%20security_and_access_control_industry_baselines/28.%20application_security_patterns.ipynb)
- Parameterization and avoiding SQL injection
- Row-Level Security (RLS) design patterns
- Multi-tenant security models
- Data masking approaches (practical options)

---

## Part VIII — Reliability: Backups, Recovery, and Migrations

### [29. Backup and Restore Fundamentals](8.%20reliability_backups_recovery_and_migrations/29.%20backup_and_restore_fundamentals.ipynb)
- Logical vs physical backups
- `pg_dump` / `pg_restore` best practices
- Backup verification (restore drills)
- Handling large databases

### [30. Point-in-Time Recovery (PITR) and WAL](8.%20reliability_backups_recovery_and_migrations/30.%20point_in_time_recovery_pitr_and_wal.ipynb)
- What WAL is and why it matters
- Archiving WAL and recovery targets
- RPO/RTO framing for teams
- Recovery runbooks

### [31. Schema Migrations in Real Teams](8.%20reliability_backups_recovery_and_migrations/31.%20schema_migrations_in_real_teams.ipynb)
- Migration tooling patterns (framework-agnostic)
- Forward-only vs down migrations
- Zero-downtime migration patterns
- Managing long-running migrations safely
- Compatibility across multiple app versions

### [32. Upgrades and Major Version Changes](8.%20reliability_backups_recovery_and_migrations/32.%20upgrades_and_major_version_changes.ipynb)
- Planning major upgrades
- `pg_upgrade` concepts and tradeoffs
- Extension compatibility checklist
- Post-upgrade validation

---

## Part IX — Replication, High Availability, and Scaling

### [33. Streaming Replication (Physical)](9.%20Replication_high_availability_and_scaling/33.%20streaming_replication_physical.ipynb)
- Primary/standby concepts
- Synchronous vs asynchronous replication
- Replication slots and retention risks
- Failover basics and caveats

### [34. Logical Replication](9.%20Replication_high_availability_and_scaling/34.%20logical_replication.ipynb)
- Publications/subscriptions
- Replicating subsets of data
- Zero-downtime migration use cases
- Conflict handling and limitations

### [35. Connection Management and Pooling](9.%20Replication_high_availability_and_scaling/35.%20connection_management_and_pooling.ipynb)
- Why connection count matters
- Pooling modes (session/transaction/statement)
- pgbouncer patterns and pitfalls
- Timeouts and safe defaults

### [36. Scaling Strategies (What Actually Works)](9.%20Replication_high_availability_and_scaling/36.%20scaling_strategies_what_actually_works.ipynb)
- Vertical scaling and tuning priorities
- Read scaling with replicas
- Sharding: when it becomes necessary (tradeoffs)
- Caching layers and consistency considerations

---

## Part X — Operations and Observability (Dev + SRE Friendly)

### [37. Configuration Basics (Practical, Not Mystical)](10.%20operations_and_observability_dev_sre_friendly/37.%20configuration_basics_practical_not_mystical.ipynb)
- Key settings: memory, WAL, checkpoints, autovacuum
- Environment-specific configuration strategy
- Reload vs restart changes

### [38. Vacuum, Analyze, and Bloat](10.%20operations_and_observability_dev_sre_friendly/38.%20vacuum_analyze_and_bloat.ipynb)
- Why vacuum exists (MVCC consequences)
- Autovacuum tuning signals
- Detecting and addressing bloat
- Routine maintenance checklist

### [39. Monitoring and Diagnostics](10.%20operations_and_observability_dev_sre_friendly/39.%20monitoring_and_diagnostics.ipynb)
- Core metrics to watch (latency, locks, WAL, vacuum)
- Slow query logging and sampling approaches
- Useful system views (`pg_stat_*`)
- Investigating incidents (a step-by-step workflow)

### [40. Performance Under Production Constraints](10.%20operations_and_observability_dev_sre_friendly/40.%20performance_under_production_constraints.ipynb)
- Hot spots and contention patterns
- Batch writes, idempotency, retries
- Timeouts, circuit breakers, and backpressure
- Load testing methodology and pitfalls

---

## Part XI — Advanced Features for Modern Applications

### [41. JSONB in Production](11.%20Advanced_features_for_modern_applications/41.%20jsonb_in_production.ipynb)
- Modeling choices: JSONB vs normalized tables
- Indexing JSONB effectively (GIN, expression indexes)
- Query patterns and anti-patterns
- Schema evolution strategies

### [42. Full-Text Search](11.%20Advanced_features_for_modern_applications/42.%20full_text_search.ipynb)
- `tsvector`, `tsquery`
- Dictionaries/configurations
- Ranking and highlighting
- When to use Postgres FTS vs external search engines

### [43. Geospatial (Optional, via PostGIS)](11.%20Advanced_features_for_modern_applications/43.%20geospatial.ipynb)
- When PostGIS is appropriate
- Core spatial types and indexes
- Common query patterns
- Operational considerations

### [44. Eventing and Asynchronous Work](11.%20Advanced_features_for_modern_applications/44.%20eventing_and_asynchronous_work.ipynb)
- LISTEN/NOTIFY patterns
- Outbox pattern with Postgres
- Jobs/queues considerations (and limitations)

---

## Part XII — Testing, Delivery, and Team Practices

### [45. Local Development Workflows](12.%20Testing_delivery_and_team_practices/45.%20local_development_workflows.ipynb)
- Seed data and fixtures
- Reproducible environments (Docker compose patterns)
- Managing multiple versions locally

### [46. Database Testing Strategies](12.%20Testing_delivery_and_team_practices/46.%20database_testing_strategies.ipynb)
- Unit tests for functions
- Integration tests with ephemeral databases
- Property-based testing ideas for SQL correctness
- Test data management and determinism

### [47. CI/CD for Databases](12.%20Testing_delivery_and_team_practices/47.%20cicd_for_databases.ipynb)
- Migration checks in CI
- Linting and formatting SQL
- Drift detection
- Release playbooks and roll-forward plans

### [48. Documentation and Standards (Handbook Within the Handbook)](12.%20Testing_delivery_and_team_practices/48.%20documentation_and_standards.ipynb)
- SQL style guide (team conventions)
- Schema review checklist
- Query review checklist
- Operational runbooks template

---

## Appendices (Reference + Checklists)

### A. `psql` Command Cheat Sheet
### B. SQL Style Guide (Recommended Conventions)
### C. Index Selection Cheat Sheet
### D. EXPLAIN Plan Reading Patterns
### E. Lock Types and Common Symptoms
### F. Backup/Restore Runbook Templates
### G. Migration Patterns Catalog (Zero-Downtime)
### H. Common Postgres Error Messages and What They Mean
### I. Glossary
### J. Recommended Reading / Official Docs Map

---