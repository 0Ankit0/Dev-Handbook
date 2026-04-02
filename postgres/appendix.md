# Appendices

[← Back to TOC](./TOC.md)

---

## Table of Contents

- [Appendix A: psql Command Cheat Sheet](#appendix-a-psql-command-cheat-sheet)
- [Appendix B: SQL Style Guide (Recommended Conventions)](#appendix-b-sql-style-guide-recommended-conventions)
- [Appendix C: Index Selection Cheat Sheet](#appendix-c-index-selection-cheat-sheet)
- [Appendix D: EXPLAIN Plan Reading Patterns](#appendix-d-explain-plan-reading-patterns)
- [Appendix E: Lock Types and Common Symptoms](#appendix-e-lock-types-and-common-symptoms)
- [Appendix F: Backup/Restore Runbook Templates](#appendix-f-backuprestore-runbook-templates)
- [Appendix G: Migration Patterns Catalog (Zero-Downtime)](#appendix-g-migration-patterns-catalog-zero-downtime)
- [Appendix H: Common Postgres Error Messages and What They Mean](#appendix-h-common-postgres-error-messages-and-what-they-mean)
- [Appendix I: Glossary](#appendix-i-glossary)
- [Appendix J: Recommended Reading / Official Docs Map](#appendix-j-recommended-reading--official-docs-map)

---

## Appendix A: psql Command Cheat Sheet

### Connecting

```bash
# Connect to database
psql -h localhost -p 5432 -U myuser -d mydb

# Connect with URL
psql "postgresql://myuser:mypassword@localhost:5432/mydb"

# Connect to local socket (superuser)
sudo -u postgres psql
```

### Meta-Commands (inside psql)

```text
\l                   List all databases
\c mydb              Switch to database mydb
\dt                  List tables in current schema
\dt *.*              List tables in all schemas
\d tablename         Describe table (columns, types, constraints)
\d+ tablename        Describe table with storage info
\di                  List indexes
\dv                  List views
\df                  List functions
\dn                  List schemas
\du                  List roles/users

\e                   Open query in $EDITOR
\i file.sql          Execute SQL from file
\o output.txt        Redirect output to file
\copy (SELECT ...) TO 'file.csv' CSV HEADER    Export query to CSV

\timing              Toggle query execution time display
\x                   Toggle expanded (vertical) output
\pset pager off      Disable pager (useful in scripts)

\q                   Quit
```

### Session Info

```sql
SELECT current_user;             -- your username
SELECT current_database();       -- current database
SELECT version();                -- PostgreSQL version
SELECT pg_postmaster_start_time(); -- when server started
SHOW search_path;                -- current schema search path
SHOW max_connections;
```

---

## Appendix B: SQL Style Guide (Recommended Conventions)

A consistent SQL style guide makes queries easier to read, review, and debug across a team. These are widely-adopted conventions used in production PostgreSQL projects.

### Naming Conventions

```sql
-- Tables: plural, snake_case
-- CREATE TABLE users (...)
-- CREATE TABLE order_items (...)

-- Columns: singular, snake_case, no abbreviations
-- user_id       -- not usr_id or uid
-- created_at    -- not create_date or CreatedAt
-- is_active     -- boolean columns use is_ or has_ prefix

-- Primary keys: always named {table_singular}_id
CREATE TABLE users (
    user_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);

-- Foreign keys: {referenced_table_singular}_id
-- orders.user_id references users.user_id

-- Indexes: idx_{table}_{columns}
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);

-- Unique indexes: uidx_{table}_{columns}
CREATE UNIQUE INDEX uidx_users_email ON users(email);

-- Constraints: {table}_{column(s)}_{type}
-- CONSTRAINT orders_total_positive CHECK (total > 0)
-- CONSTRAINT order_items_order_id_fk FOREIGN KEY (order_id) REFERENCES orders(order_id)
```

### Keyword and Formatting Style

```sql
-- Keywords: UPPERCASE
-- Identifiers: lowercase
-- Indentation: 4 spaces

SELECT
    u.user_id,
    u.email,
    COUNT(o.order_id) AS order_count,
    SUM(o.total)      AS total_spent
FROM users AS u
LEFT JOIN orders AS o
    ON o.user_id = u.user_id
WHERE
    u.is_active = TRUE
    AND u.created_at > NOW() - INTERVAL '90 days'
GROUP BY
    u.user_id,
    u.email
HAVING
    COUNT(o.order_id) > 0
ORDER BY
    total_spent DESC
LIMIT 100;
```

### Column Type Conventions

| Use Case | Preferred Type | Avoid |
|----------|---------------|-------|
| Auto-increment PK | `BIGINT GENERATED ALWAYS AS IDENTITY` | `SERIAL` |
| Distributed/external ID | `UUID` (v7 preferred) | `VARCHAR` as UUID |
| Monetary values | `NUMERIC(19, 4)` | `FLOAT`, `MONEY` |
| Timestamps | `TIMESTAMPTZ` | `TIMESTAMP` (no timezone) |
| Flags/toggles | `BOOLEAN` | `SMALLINT`, `CHAR(1)` |
| Short strings | `TEXT` with CHECK constraint | `VARCHAR(N)` |
| JSON data | `JSONB` | `JSON`, `TEXT` |
| Status/category | `TEXT` with CHECK or `ENUM` | unconstrained `VARCHAR` |

---

### Essential SQL Reference

The following patterns cover the most frequently used SQL in PostgreSQL applications.

### DDL (Data Definition Language)

```sql
-- Create table
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,         -- auto-incrementing integer
    email       TEXT NOT NULL UNIQUE,
    name        TEXT NOT NULL,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    is_active   BOOLEAN DEFAULT TRUE
);

-- Add column
ALTER TABLE users ADD COLUMN phone TEXT;

-- Rename column (non-destructive)
ALTER TABLE users RENAME COLUMN phone TO phone_number;

-- Add constraint
ALTER TABLE users ADD CONSTRAINT chk_email CHECK (email LIKE '%@%');

-- Drop column
ALTER TABLE users DROP COLUMN phone_number;

-- Create index
CREATE INDEX idx_users_email ON users(email);
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Partial index (index only active users)
CREATE INDEX idx_active_users ON users(email) WHERE is_active = TRUE;

-- Index on expression
CREATE INDEX idx_lower_email ON users(LOWER(email));
```

### DML (Data Manipulation Language)

```sql
-- Insert
INSERT INTO users (email, name) VALUES ('alice@example.com', 'Alice');

-- Insert multiple rows
INSERT INTO users (email, name) VALUES
    ('bob@example.com', 'Bob'),
    ('carol@example.com', 'Carol');

-- Insert or update (upsert)
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice Updated')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- Update
UPDATE users SET name = 'Alice Smith' WHERE email = 'alice@example.com';

-- Update with join
UPDATE orders
SET status = 'shipped'
FROM users
WHERE orders.user_id = users.id AND users.tier = 'premium';

-- Delete
DELETE FROM users WHERE is_active = FALSE;

-- Returning — get affected rows back
INSERT INTO users (email, name) VALUES ('dave@example.com', 'Dave')
RETURNING id, created_at;
```

### Queries

```sql
-- Basic select with filter and sort
SELECT id, name, email
FROM users
WHERE is_active = TRUE
ORDER BY created_at DESC
LIMIT 10;

-- Pagination
SELECT * FROM users ORDER BY id LIMIT 20 OFFSET 40;  -- page 3

-- Aggregation
SELECT
    COUNT(*) AS total_users,
    COUNT(*) FILTER (WHERE is_active = TRUE) AS active_count,
    MAX(created_at) AS latest_signup
FROM users;

-- Group by
SELECT
    DATE_TRUNC('month', created_at) AS month,
    COUNT(*) AS signups
FROM users
GROUP BY 1
ORDER BY 1;

-- Join types
SELECT u.name, o.id AS order_id
FROM users u
INNER JOIN orders o ON o.user_id = u.id;     -- only matching rows

SELECT u.name, o.id AS order_id
FROM users u
LEFT JOIN orders o ON o.user_id = u.id;      -- all users, null if no orders

-- CTE (Common Table Expression)
WITH active_users AS (
    SELECT id, name FROM users WHERE is_active = TRUE
),
recent_orders AS (
    SELECT user_id, COUNT(*) AS order_count
    FROM orders
    WHERE created_at > NOW() - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT u.name, COALESCE(o.order_count, 0) AS orders
FROM active_users u
LEFT JOIN recent_orders o ON o.user_id = u.id;

-- Window function
SELECT
    name,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

-- Subquery
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 1000);
```

### Transactions

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- If anything went wrong:
ROLLBACK;

-- If everything looks good:
COMMIT;

-- Savepoints — partial rollback
BEGIN;
  UPDATE foo SET x = 1;
  SAVEPOINT my_savepoint;
  UPDATE foo SET y = 2;
  ROLLBACK TO SAVEPOINT my_savepoint;  -- undo the y=2 update
COMMIT;
```

---

## Appendix C: Index Selection Cheat Sheet

| Index Type | Use When | Example |
|-----------|----------|---------|
| **B-tree** (default) | Equality and range queries on any type | `WHERE age > 30`, `WHERE email = 'x'` |
| **GIN** | Full-text search, array containment, JSONB keys | `WHERE tags @> '{postgres}'`, `tsvector` columns |
| **GiST** | Geometric data, full-text, range types | Polygon overlap, `tsrange` |
| **BRIN** | Very large tables with physically sorted data | Append-only logs with timestamp, time-series |
| **Hash** | Equality only (rarely better than B-tree) | `WHERE id = 42` |

### Composite Index Rule
```sql
-- Index on (a, b) helps: WHERE a = ? AND b = ?
--                        WHERE a = ?
-- Does NOT help:         WHERE b = ?

CREATE INDEX idx_user_status ON orders(user_id, status);
-- Good for: WHERE user_id = 5 AND status = 'pending'
-- Good for: WHERE user_id = 5
-- Not used: WHERE status = 'pending'
```

---

## Appendix D: EXPLAIN Output Quick Guide

```sql
-- Always use EXPLAIN ANALYZE BUFFERS for real diagnostics
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 42;
```

**Key terms in EXPLAIN output:**

| Term | Meaning |
|------|---------|
| `Seq Scan` | Full table scan — fine for small tables, bad for large ones |
| `Index Scan` | Using an index, fetches heap rows — good |
| `Index Only Scan` | All needed columns in index — best |
| `Nested Loop` | Join by looping — good for small sets |
| `Hash Join` | Join by building hash table — good for larger sets |
| `Merge Join` | Join pre-sorted sets — good for large sorted data |
| `cost=X..Y` | Estimated startup cost X, total cost Y (in "units") |
| `rows=N` | Estimated rows returned — check against actual |
| `actual time=X..Y` | Real milliseconds (only with ANALYZE) |
| `Buffers: hit=N` | Pages served from cache (fast) |
| `Buffers: read=N` | Pages read from disk (slow) |

---

---

## Appendix E: Lock Types and Common Symptoms

PostgreSQL has a rich locking model. Understanding the common lock types helps you diagnose blocking queries and design operations that avoid unnecessary contention.

### Row-Level Locks

These locks are acquired automatically during DML operations and can also be requested explicitly.

| Lock Mode | Acquired By | Blocks |
|-----------|-------------|--------|
| `FOR UPDATE` | `SELECT ... FOR UPDATE` | `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, `FOR KEY SHARE` |
| `FOR NO KEY UPDATE` | `UPDATE` (non-key columns) | `FOR UPDATE`, `FOR NO KEY UPDATE` |
| `FOR SHARE` | `SELECT ... FOR SHARE` | `FOR UPDATE`, `FOR NO KEY UPDATE` |
| `FOR KEY SHARE` | `SELECT ... FOR KEY SHARE` | `FOR UPDATE` only |

**Practical Notes:**
- `FOR UPDATE` is the most common explicit lock — use it when you read a row and intend to update it in the same transaction (prevents lost updates).
- `FOR NO KEY UPDATE` allows concurrent foreign key checks (used internally by PostgreSQL for FK enforcement).
- `FOR SHARE` allows concurrent reads but prevents updates — rarely needed.

### Table-Level Locks

These are acquired automatically by DDL and DML operations. Many can block each other.

| Operation | Lock Acquired | What It Blocks |
|-----------|--------------|----------------|
| `SELECT` | `AccessShareLock` | Only `AccessExclusiveLock` |
| `INSERT`, `UPDATE`, `DELETE` | `RowExclusiveLock` | `SHARE`, `SHARE ROW EXCLUSIVE`, `EXCLUSIVE`, `ACCESS EXCLUSIVE` |
| `CREATE INDEX CONCURRENTLY` | `ShareUpdateExclusiveLock` | Writes, `VACUUM`, other concurrent DDL |
| `ALTER TABLE` (most forms) | `AccessExclusiveLock` | **Everything** including reads |
| `TRUNCATE` | `AccessExclusiveLock` | **Everything** |
| `VACUUM FULL` | `AccessExclusiveLock` | **Everything** |
| `DROP TABLE` | `AccessExclusiveLock` | **Everything** |
| `LOCK TABLE ... EXCLUSIVE` | `ExclusiveLock` | All except `AccessShareLock` |

**Key Insight:** `ALTER TABLE` and `VACUUM FULL` acquire `AccessExclusiveLock`, which blocks ALL other operations including reads. On busy tables, these must be done carefully (during low-traffic windows or using online alternatives).

### Advisory Locks

Advisory locks are application-defined locks not tied to any table. They're useful for distributed mutual exclusion — ensuring only one process runs a specific task at a time.

```sql
-- Session-level advisory lock (released at session end or explicit unlock)
SELECT pg_advisory_lock(12345);        -- Acquire
-- ... do work ...
SELECT pg_advisory_unlock(12345);      -- Release

-- Transaction-level advisory lock (released at transaction end)
SELECT pg_advisory_xact_lock(12345);  -- No explicit unlock needed

-- Try to acquire without blocking
SELECT pg_try_advisory_lock(12345);   -- Returns true if acquired, false if already held
```

### Common Locking Symptoms and Diagnostics

```sql
-- Find currently blocked queries
SELECT
    blocked.pid         AS blocked_pid,
    blocked.query       AS blocked_query,
    blocking.pid        AS blocking_pid,
    blocking.query      AS blocking_query,
    blocked.wait_event_type,
    blocked.wait_event
FROM pg_stat_activity AS blocked
JOIN pg_stat_activity AS blocking
    ON blocking.pid = ANY(pg_blocking_pids(blocked.pid))
WHERE blocked.wait_event_type = 'Lock';

-- Find long-running transactions (often the root cause of lock waits)
SELECT
    pid,
    now() - xact_start AS transaction_duration,
    now() - query_start AS query_duration,
    state,
    left(query, 100) AS query_snippet
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
ORDER BY xact_start ASC;

-- Kill a blocking process (use terminate for active queries, cancel for idle-in-transaction)
SELECT pg_cancel_backend(pid);    -- Sends SIGINT, kills the query but not the connection
SELECT pg_terminate_backend(pid); -- Sends SIGTERM, kills the connection entirely
```

**Common Lock Problem Scenarios:**

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| `ALTER TABLE` hanging | Long-running queries or idle transactions holding locks | Find and terminate blockers; use `lock_timeout` |
| Deadlock errors | Two transactions acquiring locks in different orders | Standardize lock acquisition order in application code |
| Queue of blocked writes | One long-running transaction | Set `idle_in_transaction_session_timeout` |
| Slow application after deploy | New schema migration holding AccessExclusiveLock | Use zero-downtime migration patterns |

---

## Appendix F: Backup/Restore Runbook Templates

### Logical Backup with pg_dump

```bash
#!/bin/bash
# backup-logical.sh — run daily for databases under ~100GB

DB_HOST="db.example.com"
DB_PORT="5432"
DB_USER="backup_user"
DB_NAME="production"
BACKUP_DIR="/backups/pg_dumps"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/${DB_NAME}_${TIMESTAMP}.dump"

# Create backup in custom format (compressed, supports parallel restore)
pg_dump \
  --host="${DB_HOST}" \
  --port="${DB_PORT}" \
  --username="${DB_USER}" \
  --format=custom \
  --compress=9 \
  --no-password \
  --file="${BACKUP_FILE}" \
  "${DB_NAME}"

if [ $? -eq 0 ]; then
  echo "Backup successful: ${BACKUP_FILE}"
  # Upload to S3 or other offsite storage
  aws s3 cp "${BACKUP_FILE}" "s3://your-backup-bucket/pg_dumps/"
  # Verify upload
  aws s3 ls "s3://your-backup-bucket/pg_dumps/$(basename ${BACKUP_FILE})"
else
  echo "Backup FAILED" >&2
  exit 1
fi

# Retention: remove backups older than 14 days
find "${BACKUP_DIR}" -name "*.dump" -mtime +14 -delete
```

### Restore from pg_dump

```bash
#!/bin/bash
# restore-logical.sh — restore a pg_dump backup

BACKUP_FILE="$1"         # Path to .dump file
TARGET_DB="$2"           # Target database name
DB_HOST="db.example.com"
DB_USER="postgres"

if [ -z "${BACKUP_FILE}" ] || [ -z "${TARGET_DB}" ]; then
  echo "Usage: $0 <backup_file.dump> <target_database>"
  exit 1
fi

# Create the target database (must not exist)
createdb --host="${DB_HOST}" --username="${DB_USER}" "${TARGET_DB}"

# Restore with parallel jobs (speeds up large restores)
pg_restore \
  --host="${DB_HOST}" \
  --username="${DB_USER}" \
  --dbname="${TARGET_DB}" \
  --jobs=4 \
  --verbose \
  "${BACKUP_FILE}"

if [ $? -eq 0 ]; then
  echo "Restore complete. Run ANALYZE to update statistics:"
  psql --host="${DB_HOST}" --username="${DB_USER}" --dbname="${TARGET_DB}" \
       -c "ANALYZE VERBOSE;"
else
  echo "Restore FAILED" >&2
  exit 1
fi
```

### Physical Backup with pg_basebackup

```bash
#!/bin/bash
# backup-physical.sh — base backup for PITR setup

PGDATA="/var/lib/postgresql/16/main"
BACKUP_DIR="/backups/base_backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
TARGET_DIR="${BACKUP_DIR}/base_${TIMESTAMP}"

# pg_basebackup requires a replication-capable user
pg_basebackup \
  --host=localhost \
  --username=replication_user \
  --pgdata="${TARGET_DIR}" \
  --format=tar \
  --gzip \
  --checkpoint=fast \
  --wal-method=stream \
  --progress \
  --verbose

if [ $? -eq 0 ]; then
  echo "Base backup complete: ${TARGET_DIR}"
  echo "WAL archiving must be running for PITR to work"
else
  echo "Base backup FAILED" >&2
  exit 1
fi
```

### Restore Drill Checklist

A backup you've never tested is a hope, not a backup. Run this drill monthly:

```text
□ Download the most recent backup from offsite storage
□ Spin up a test server (can be smaller than production)
□ Run the restore procedure
□ Verify row counts match production samples
□ Run ANALYZE on restored database
□ Test critical application queries
□ Measure restore time (record for RTO planning)
□ Document any issues or deviations
□ Destroy test environment
```

---

## Appendix G: Migration Patterns Catalog (Zero-Downtime)

These patterns allow you to change database schema without taking the application offline. The key constraint: during the migration window, **both old and new application code must work with the same schema**.

### Pattern 1: Add a Nullable Column

Safe to add at any time. No downtime required.

```sql
-- Step 1: Add the column (instantly, no rewrite needed)
ALTER TABLE users ADD COLUMN phone TEXT;

-- Step 2: Backfill existing rows if needed (do in batches to avoid locks)
UPDATE users SET phone = '' WHERE phone IS NULL AND id BETWEEN 1 AND 10000;
-- Repeat for subsequent ID ranges

-- Step 3 (later): Add NOT NULL constraint once all rows have values
ALTER TABLE users ALTER COLUMN phone SET NOT NULL;
-- Note: This requires a table scan to verify. Consider a CHECK constraint first:
ALTER TABLE users ADD CONSTRAINT users_phone_not_null CHECK (phone IS NOT NULL) NOT VALID;
ALTER TABLE users VALIDATE CONSTRAINT users_phone_not_null;  -- Validates without full lock
```

### Pattern 2: Rename a Column (Safe, Multi-Phase)

Never rename directly in a busy system. Use this expand-contract pattern:

```sql
-- Phase 1 (deploy with old app): Add new column alongside old
ALTER TABLE users ADD COLUMN full_name TEXT;

-- Phase 2 (dual-write app): App writes to BOTH old and new columns
-- Keep them in sync with a trigger:
CREATE OR REPLACE FUNCTION sync_name() RETURNS TRIGGER AS $$
BEGIN
    NEW.full_name := NEW.name;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER sync_name_trigger
BEFORE INSERT OR UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION sync_name();

-- Backfill existing rows
UPDATE users SET full_name = name WHERE full_name IS NULL;

-- Phase 3 (new app only reads new column)
-- Phase 4 (cleanup): Drop old column and trigger
DROP TRIGGER sync_name_trigger ON users;
ALTER TABLE users DROP COLUMN name;
```

### Pattern 3: Add NOT NULL Constraint Safely

Adding NOT NULL directly on a large table takes an `AccessExclusiveLock` for the entire duration of the table scan.

```sql
-- Step 1: Add as NOT VALID (no scan, instant)
ALTER TABLE orders ADD CONSTRAINT orders_user_id_not_null 
  CHECK (user_id IS NOT NULL) NOT VALID;

-- Step 2: Validate (scans table but only holds ShareUpdateExclusiveLock — reads still work)
ALTER TABLE orders VALIDATE CONSTRAINT orders_user_id_not_null;

-- Step 3: Convert to actual NOT NULL (requires scan — do during low traffic)
ALTER TABLE orders ALTER COLUMN user_id SET NOT NULL;
ALTER TABLE orders DROP CONSTRAINT orders_user_id_not_null;
```

### Pattern 4: Add an Index Without Downtime

`CREATE INDEX` locks out writes. Use `CONCURRENTLY` to build without blocking.

```sql
-- Creates index without blocking reads or writes
-- Takes longer (two passes over the table) but safe on production
CREATE INDEX CONCURRENTLY idx_orders_created_at ON orders(created_at);

-- Never run CREATE INDEX CONCURRENTLY inside an explicit transaction block
-- If it fails, drop the invalid partial index and retry:
DROP INDEX CONCURRENTLY idx_orders_created_at;
```

### Pattern 5: Drop a Column Safely

```sql
-- Step 1: Stop reading the column in application code (deploy first)
-- Step 2: Remove NOT NULL constraint if present
ALTER TABLE users ALTER COLUMN old_field DROP NOT NULL;
-- Step 3: Drop (marking column as dropped is instant; space reclaimed on next VACUUM FULL)
ALTER TABLE users DROP COLUMN old_field;
```

### Pattern 6: Change Column Type

Direct type casting can be instant (e.g., TEXT → JSONB) or require a table rewrite (locks table). Use expand-contract for non-trivial changes.

```sql
-- Check if the cast is safe (won't rewrite table)
-- INT → BIGINT: safe, instant
ALTER TABLE orders ALTER COLUMN amount TYPE BIGINT;

-- INT → TEXT: rewrites table (locks reads+writes)
-- Use expand-contract pattern instead:
-- 1. Add new TEXT column
-- 2. Backfill it
-- 3. Switch application to new column
-- 4. Drop old column
```

---

## Appendix H: Common Postgres Error Messages and What They Mean

| Error | Meaning | Fix |
|-------|---------|-----|
| `duplicate key value violates unique constraint` | Inserted a value that already exists in a UNIQUE column | Check for existing row before insert or use `ON CONFLICT` |
| `null value in column violates not-null constraint` | Tried to insert NULL into a NOT NULL column | Provide a value or add a DEFAULT |
| `could not connect to server` | Database not running or wrong host/port | Check `pg_ctl status` and connection params |
| `FATAL: role "x" does not exist` | Connecting with a role that doesn't exist | `CREATE ROLE x LOGIN` |
| `ERROR: deadlock detected` | Two transactions blocked each other | Check transaction ordering; acquire locks in consistent order |
| `ERROR: canceling statement due to lock timeout` | Waited too long for a lock | Investigate blocking queries with `pg_stat_activity` |
| `out of shared memory` | Too many locks or shared objects | Increase `max_locks_per_transaction` in postgresql.conf |

---

## Appendix H: Common Postgres Error Messages and What They Mean

| Error | Meaning | Fix |
|-------|---------|-----|
| `duplicate key value violates unique constraint` | Inserted a value that already exists in a UNIQUE column | Check for existing row before insert or use `ON CONFLICT` |
| `null value in column violates not-null constraint` | Tried to insert NULL into a NOT NULL column | Provide a value or add a DEFAULT |
| `could not connect to server` | Database not running or wrong host/port | Check `pg_ctl status` and connection params |
| `FATAL: role "x" does not exist` | Connecting with a role that doesn't exist | `CREATE ROLE x LOGIN` |
| `ERROR: deadlock detected` | Two transactions blocked each other | Check transaction ordering; acquire locks in consistent order |
| `ERROR: canceling statement due to lock timeout` | Waited too long for a lock | Investigate blocking queries with `pg_stat_activity` |
| `out of shared memory` | Too many locks or shared objects | Increase `max_locks_per_transaction` in postgresql.conf |
| `FATAL: remaining connection slots are reserved` | At max_connections limit (minus superuser slots) | Check for connection leaks; use a connection pooler |
| `ERROR: value too long for type character varying(N)` | String exceeds the column's length limit | Use TEXT instead of VARCHAR(N), or validate input length |
| `could not serialize access due to concurrent update` | Serializable isolation conflict | Retry the transaction — this is expected behavior |
| `relation "x" does not exist` | Table not in current search_path | Qualify with schema name: `SELECT * FROM myschema.mytable` |
| `column "x" does not exist` | Column misspelled, or identifier case issue | Unquoted identifiers are lowercased; check `\d tablename` |
| `permission denied for table x` | Role lacks SELECT/INSERT/UPDATE/DELETE privilege | `GRANT SELECT ON x TO rolename` |
| `FATAL: password authentication failed` | Wrong password or role not found | Verify username/password; check pg_hba.conf auth method |
| `invalid byte sequence for encoding "UTF8"` | Data contains non-UTF8 bytes | Validate encoding at application level; use `convert_from()` |
| `division by zero` | Dividing by zero in a query | Add `NULLIF(denominator, 0)` to return NULL instead |
| `function x does not exist` | Function called with wrong argument types | Check function signature: `\df function_name` |
| `there is no unique constraint matching given keys for referenced table` | FOREIGN KEY references non-unique column | Add UNIQUE constraint or PRIMARY KEY to referenced column |

### Monitoring Queries Reference

```sql
-- Active queries running longer than 5 seconds
SELECT
    pid,
    now() - query_start AS duration,
    state,
    left(query, 120) AS query_snippet
FROM pg_stat_activity
WHERE state != 'idle'
  AND (now() - query_start) > INTERVAL '5 seconds'
ORDER BY duration DESC;

-- Find blocked queries and their blockers
SELECT
    blocked.pid         AS blocked_pid,
    blocked.query       AS blocked_query,
    blocking.pid        AS blocking_pid,
    blocking.query      AS blocking_query
FROM pg_stat_activity AS blocked
JOIN pg_stat_activity AS blocking
    ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));

-- Table sizes (top 20)
SELECT
    schemaname || '.' || tablename AS table,
    pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size,
    pg_size_pretty(pg_relation_size(schemaname || '.' || tablename)) AS table_size,
    pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)
                   - pg_relation_size(schemaname || '.' || tablename)) AS index_size
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname || '.' || tablename) DESC
LIMIT 20;

-- Potentially unused indexes (low scan count)
SELECT
    schemaname || '.' || tablename AS table,
    indexname,
    idx_scan AS times_used,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
WHERE idx_scan < 50
ORDER BY pg_relation_size(indexrelid) DESC;

-- Table bloat estimate
SELECT
    schemaname,
    tablename,
    n_dead_tup,
    n_live_tup,
    ROUND(n_dead_tup::numeric / NULLIF(n_live_tup + n_dead_tup, 0) * 100, 1) AS dead_pct,
    last_autovacuum,
    last_autoanalyze
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY n_dead_tup DESC;
```

---

## Appendix I: Glossary

**ACID**
The four properties that guarantee database transactions are reliable: Atomicity (all-or-nothing), Consistency (constraints never violated), Isolation (concurrent transactions don't interfere), Durability (committed data survives crashes). PostgreSQL fully implements ACID.

**Advisory Lock**
An application-defined lock using arbitrary integer keys. Not tied to any table row. Used for distributed mutual exclusion — e.g., ensuring only one background process runs a specific job at a time.

**Autovacuum**
A background daemon that automatically runs VACUUM and ANALYZE on tables when they accumulate enough dead tuples or stale statistics. Should never be disabled; tune it instead of disabling it.

**B-tree Index**
The default index type in PostgreSQL. A self-balancing tree where each leaf points to a heap row. Supports equality, range queries, ORDER BY, IS NULL, and IN operations.

**Bloat**
Wasted space in tables and indexes caused by dead tuples (from MVCC) that haven't been reclaimed by VACUUM. Some bloat is normal (~10-20%). Severe bloat degrades performance and wastes disk.

**Checkpoint**
The moment when PostgreSQL writes all dirty data pages from shared_buffers to disk. Checkpoints happen periodically and ensure data durability. Frequent checkpoints spike I/O; infrequent ones lengthen crash recovery.

**Cluster**
A PostgreSQL installation — a single running server that manages one data directory (`PGDATA`). A cluster can contain many databases. Not related to server clustering in the high-availability sense.

**CTE (Common Table Expression)**
A named subquery defined using the `WITH` keyword. Makes complex queries more readable. In PostgreSQL 12+, CTEs are inlined by default (optimizer can push down filters). Use `WITH ... AS MATERIALIZED` to force the old optimization barrier behavior.

**Dead Tuple**
An old row version created by MVCC when a row is updated or deleted. Still visible to older transactions. Cleaned up by VACUUM. Too many dead tuples cause table bloat.

**DDL (Data Definition Language)**
SQL statements that modify the database structure: `CREATE TABLE`, `ALTER TABLE`, `DROP INDEX`, etc. Most DDL statements in PostgreSQL acquire `AccessExclusiveLock`, blocking all other operations.

**DML (Data Manipulation Language)**
SQL statements that manipulate data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`. These acquire row-level locks and are the bulk of day-to-day queries.

**Deadlock**
When two or more transactions each hold a lock that the other needs, causing both to wait indefinitely. PostgreSQL detects this and automatically rolls back one of the transactions with `ERROR: deadlock detected`. Prevention: always acquire locks in the same order.

**Extension**
A packaged set of SQL objects (types, functions, operators, indexes) that can be installed as a unit with `CREATE EXTENSION`. Versioned and trackable. Common examples: `pgcrypto`, `uuid-ossp`, `PostGIS`, `pg_stat_statements`.

**Foreign Key (FK)**
A column or set of columns that references the primary key of another table, enforcing referential integrity. PostgreSQL checks FK constraints on INSERT, UPDATE, and DELETE.

**GIN (Generalized Inverted Index)**
An index type optimized for values that contain multiple components — like arrays, JSONB, and full-text search vectors. Like a book index: maps individual items (words, keys) to the rows that contain them.

**GiST (Generalized Search Tree)**
A flexible index framework for complex data types: geometric shapes, geographic data, range types, and full-text search. Used by PostGIS for spatial queries.

**Heap**
The main storage file for a table — the physical file containing the actual rows. Contrasted with indexes, which are separate files containing sorted references to heap rows.

**Hot Standby**
A standby server in streaming replication that can accept read-only queries while continuously applying WAL from the primary. Useful for read scaling and as a failover target.

**Index Scan**
A query execution strategy that uses an index to find matching rows, then fetches those rows from the heap. Efficient when the query matches a small fraction of rows.

**information_schema**
A SQL-standard schema available in all PostgreSQL databases containing views that describe the database structure (tables, columns, constraints, privileges). Use it for portable introspection queries.

**MVCC (Multi-Version Concurrency Control)**
PostgreSQL's concurrency model. When a row is updated or deleted, the old version is kept alongside the new one. Each transaction sees the version that was current when the transaction started. Readers never block writers; writers never block readers. Dead versions are cleaned up by VACUUM.

**N+1 Query Problem**
A performance anti-pattern where application code runs one query to fetch N records, then N additional queries to fetch related data for each record. Results in N+1 database round trips. Solved by JOINs, batch loading, or eager loading.

**OLTP (Online Transaction Processing)**
Database workloads characterized by high-frequency, short-duration, concurrent transactions — like e-commerce, banking, or user management systems. PostgreSQL is optimized for OLTP.

**OLAP (Online Analytical Processing)**
Database workloads characterized by complex analytical queries on large datasets — like data warehousing and reporting. PostgreSQL supports OLAP with partitioning, materialized views, and extensions like Citus.

**Outbox Pattern**
A technique to reliably publish events alongside database writes. Instead of calling an external system directly (which can fail), write an event record to an "outbox" table in the same transaction. A separate process reads and delivers the events.

**Parameterized Query**
A query where user-supplied values are passed as separate parameters rather than interpolated into the SQL string. Prevents SQL injection by ensuring input is never interpreted as SQL code.

**Partition**
A physical sub-table that stores a subset of a parent table's data. PostgreSQL's declarative partitioning splits one logical table into multiple physical files based on a partition key. Query planning automatically skips irrelevant partitions (partition pruning).

**pg_catalog**
The system schema that stores PostgreSQL's internal metadata — tables, columns, indexes, functions, roles, and everything else the server tracks. Avoid modifying pg_catalog directly. Use `\d`, `information_schema`, or the `pg_stat_*` views for routine introspection.

**PgBouncer**
A lightweight connection pooler for PostgreSQL. Sits between the application and the database, allowing many application connections to share a smaller set of actual PostgreSQL connections. Dramatically reduces connection overhead at scale.

**PITR (Point-in-Time Recovery)**
The ability to restore a database to any specific moment in the past. Requires a base backup plus continuous WAL archiving. Used to recover from accidental data deletion or corruption.

**PL/pgSQL**
PostgreSQL's built-in procedural language. Extends SQL with variables, conditionals, loops, and exception handling. Used for stored functions, procedures, and triggers.

**Primary Key (PK)**
A column or set of columns that uniquely identifies each row in a table. Automatically creates a unique B-tree index. Cannot contain NULL. Should be used in foreign key references from other tables.

**Publication (Logical Replication)**
A named set of tables and operations to replicate. Created on the source server with `CREATE PUBLICATION`. Part of logical replication.

**Query Planner / Optimizer**
The PostgreSQL component that decides HOW to execute a query — which indexes to use, what join strategy to use, in what order to join tables. Uses column statistics to estimate row counts and compare plan costs.

**Replication Slot**
A mechanism that prevents the primary server from discarding WAL segments that a standby hasn't consumed yet. Essential for reliable replication. Risk: if a standby disconnects and the slot is not dropped, WAL accumulates indefinitely and can fill disk.

**RPO (Recovery Point Objective)**
The maximum acceptable amount of data loss after a disaster. "Our RPO is 5 minutes" means we accept losing up to 5 minutes of committed transactions. Drives backup frequency and replication requirements.

**RTO (Recovery Time Objective)**
The maximum acceptable time to restore service after a disaster. "Our RTO is 1 hour" means the database must be back online within 1 hour. Drives decisions about backup format, restore automation, and standby setup.

**Row-Level Security (RLS)**
A PostgreSQL feature that restricts which rows a user can see or modify, enforced at the database level. Policies are defined per-table and evaluated for every query, regardless of which application makes the request.

**Schema**
A namespace inside a PostgreSQL database. Organizes related objects (tables, views, functions) together. The default schema is `public`. Multiple schemas in one database are used for multi-tenancy, module separation, or permission isolation.

**Sequence**
A database object that generates a series of unique integers. Used for auto-increment primary keys. Sequence advances even if the transaction that used it rolls back, so gaps are normal and expected.

**Sequential Scan (Seq Scan)**
A query execution strategy that reads every row in a table from start to finish. Fast for small tables or queries that need most of the table's rows. Slow for large tables when only a few rows are needed.

**Shared Buffers**
PostgreSQL's in-memory page cache. Hot data pages are stored here to avoid disk reads. Typically set to 25% of available RAM.

**TOAST (The Oversized Attribute Storage Technique)**
PostgreSQL's mechanism for storing large column values. When a row exceeds ~8KB (one page), large values are compressed and/or moved to a separate TOAST table. Transparent to the user — you query the main table as normal.

**Transaction**
A unit of work that either completes entirely or not at all (atomic). Groups multiple SQL statements that must succeed or fail together. Defined by `BEGIN` ... `COMMIT` (or `ROLLBACK`).

**Transaction ID (XID)**
A 32-bit integer assigned to each transaction. PostgreSQL uses XIDs to determine row visibility (MVCC). After ~2 billion transactions, XIDs wrap around — VACUUM must "freeze" old rows to prevent this catastrophic event.

**Trigger**
Code that PostgreSQL automatically executes BEFORE or AFTER an INSERT, UPDATE, or DELETE operation (or INSTEAD OF for views). Triggers call a trigger function written in PL/pgSQL or another procedural language.

**VACUUM**
The process that reclaims storage from dead tuples, preventing table bloat and transaction ID wraparound. `VACUUM ANALYZE` also updates query planner statistics. `AUTOVACUUM` runs automatically in the background.

**WAL (Write-Ahead Log)**
A transaction log where all data changes are recorded *before* being written to data files. This guarantees crash recovery. WAL is also the foundation of streaming replication (standby servers replay WAL) and PITR.

**Window Function**
A SQL function that performs calculations across a set of rows related to the current row, without collapsing rows like `GROUP BY` does. Uses the `OVER()` clause. Common examples: `RANK()`, `ROW_NUMBER()`, `LAG()`, `SUM() OVER()`.

**XID Wraparound**
A catastrophic event that occurs when a PostgreSQL database reaches ~2.1 billion transactions without VACUUM running to freeze old rows. PostgreSQL enters a safety mode where it refuses all connections to prevent data corruption. Avoided by monitoring transaction age and ensuring autovacuum runs regularly.

---

## Appendix J: Recommended Reading / Official Docs Map

### Official Documentation

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [PostgreSQL Official Docs](https://www.postgresql.org/docs/current/) | Everything — the authoritative reference | Any specific feature, function signature, configuration parameter |
| [Postgres Documentation: SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html) | Every SQL statement with complete syntax | Looking up exact syntax for CREATE TABLE, ALTER TABLE, etc. |
| [Postgres Documentation: System Catalogs](https://www.postgresql.org/docs/current/catalogs.html) | pg_class, pg_stat_*, information_schema | Writing diagnostic queries |
| [Postgres Documentation: Configuration](https://www.postgresql.org/docs/current/runtime-config.html) | All postgresql.conf parameters | Tuning memory, WAL, connections, autovacuum |
| [Postgres Documentation: Release Notes](https://www.postgresql.org/docs/current/release.html) | What changed in each version | Planning upgrades, finding new features |

### Indexing and Query Performance

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [Use The Index, Luke](https://use-the-index-luke.com/) | SQL indexing explained for developers | Understanding how indexes work, when they're used, and why queries are slow |
| [Explain.depesz.com](https://explain.depesz.com/) | EXPLAIN output visualizer | Pasting EXPLAIN output to get a readable analysis |
| [pgMustard](https://www.pgmustard.com/) | EXPLAIN ANALYZE visualizer with recommendations | Getting actionable suggestions from slow query plans |
| [Postgres EXPLAIN documentation](https://www.postgresql.org/docs/current/using-explain.html) | Official EXPLAIN guide | Understanding every field in EXPLAIN output |

### Reliability and Operations

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [pganalyze Blog](https://pganalyze.com/blog) | Query performance, VACUUM, autovacuum tuning | Deep dives on production PostgreSQL operations |
| [Crunchy Data Blog](https://www.crunchydata.com/blog) | PostgreSQL features, operations, best practices | Practical articles on real-world PostgreSQL usage |
| [Postgres Weekly Newsletter](https://postgresweekly.com/) | Curated weekly PostgreSQL news | Staying current with new features and community articles |
| [High Performance PostgreSQL for Rails](https://pragprog.com/titles/aapsql/high-performance-postgresql-for-rails/) | Performance optimization (applies beyond Rails) | Deep understanding of indexing, query tuning, connection pooling |

### Interactive Learning

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [pgexercises.com](https://pgexercises.com/) | SQL exercises with instant feedback | Practicing SQL queries and joins |
| [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) | Step-by-step SQL tutorials | Beginners learning PostgreSQL syntax |
| [sql-practice.com](https://www.sql-practice.com/) | Interactive SQL challenges | Building query fluency |

### Security

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [Postgres Documentation: Role Attributes](https://www.postgresql.org/docs/current/role-attributes.html) | Role creation and privilege flags | Understanding SUPERUSER, LOGIN, CREATEDB, etc. |
| [Postgres Documentation: Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) | RLS policy syntax and examples | Implementing tenant isolation |
| [Postgres Documentation: pg_hba.conf](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html) | Host-based authentication configuration | Securing connection access |

### Migrations and Schema Changes

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [Strong Migrations (Ruby)](https://github.com/ankane/strong_migrations) | Safe migration patterns and anti-patterns | Understanding zero-downtime migration principles (applies beyond Ruby) |
| [Squawk SQL Linter](https://squawkhq.com/) | Linting SQL migrations for dangerous patterns | Catching `ALTER TABLE` without `CONCURRENTLY` and similar issues |
| [Postgres Documentation: DDL](https://www.postgresql.org/docs/current/ddl.html) | Table creation, constraints, partitioning | Reference for any schema definition topic |

### Extensions and Ecosystem

| Resource | What It Covers | Best For |
|----------|---------------|----------|
| [PostGIS Documentation](https://postgis.net/documentation/) | Spatial types, functions, indexes | Geospatial feature implementation |
| [pgvector GitHub](https://github.com/pgvector/pgvector) | Vector similarity search | AI/ML embedding storage and search |
| [TimescaleDB Docs](https://docs.timescale.com/) | Time-series PostgreSQL | High-volume time-series ingestion and queries |
| [PGXN (PostgreSQL Extension Network)](https://pgxn.org/) | Community PostgreSQL extensions | Discovering available extensions |

---

[← Back to TOC](./TOC.md)
