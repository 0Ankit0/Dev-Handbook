# Appendices

[← Back to TOC](./TOC.md)

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

## Appendix B: Essential SQL Reference

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

## Appendix C: Index Selection Guide

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

## Appendix E: Common Error Messages

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

## Appendix F: Monitoring Queries

```sql
-- Active queries (> 5 seconds)
SELECT pid, now() - pg_stat_activity.query_start AS duration, query, state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > INTERVAL '5 seconds'
  AND state != 'idle'
ORDER BY duration DESC;

-- Blocked queries
SELECT pid, wait_event_type, wait_event, query
FROM pg_stat_activity
WHERE wait_event IS NOT NULL AND state != 'idle';

-- Table sizes
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname || '.' || tablename) DESC
LIMIT 20;

-- Index usage stats
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,         -- number of times index was used
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC;  -- low idx_scan = possibly unused index

-- Kill a blocking query
SELECT pg_terminate_backend(pid)  -- or pg_cancel_backend for softer cancel
FROM pg_stat_activity
WHERE pid = <blocking_pid>;
```

---

## Appendix G: Glossary

**MVCC (Multi-Version Concurrency Control)**
PostgreSQL's concurrency model. Readers never block writers and writers never block readers. Each transaction sees a snapshot of the database at a point in time. Old versions are cleaned up by VACUUM.

**VACUUM**
The process that reclaims storage from dead tuples left behind by MVCC updates and deletes. `VACUUM ANALYZE` also updates query planner statistics. `AUTOVACUUM` runs this automatically.

**WAL (Write-Ahead Log)**
A transaction log where all changes are recorded before being applied to data files. Enables crash recovery, point-in-time recovery (PITR), and streaming replication.

**Planner / Query Optimizer**
The component that decides *how* to execute a query (which indexes to use, join order, etc.). Uses table statistics (`pg_statistic`) to estimate row counts and costs.

**Replication**
Streaming physical replication copies WAL from primary to standby servers. Standbys can be read-only replicas (for scaling reads) or hot standbys (for high availability).

**Connection Pooler (PgBouncer)**
PostgreSQL has a limited number of connections (each is a process). PgBouncer sits in front and multiplexes many application connections onto fewer actual database connections, improving performance at scale.

---

## Appendix H: Resources

- [PostgreSQL Official Docs](https://www.postgresql.org/docs/current/) — comprehensive reference
- [Use The Index, Luke](https://use-the-index-luke.com/) — SQL indexing for developers
- [pgexercises.com](https://pgexercises.com/) — interactive SQL practice
- [Explain.depesz.com](https://explain.depesz.com/) — EXPLAIN plan visualizer
