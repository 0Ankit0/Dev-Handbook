import json


def src(text):
    """Convert multiline string to Jupyter source list format."""
    lines = text.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        else:
            if line:
                result.append(line)
    return result


def md(text):
    return {"cell_type": "markdown", "id": "new-md", "metadata": {}, "source": src(text)}


def code_cell(text):
    return {
        "cell_type": "code", "id": "new-code", "execution_count": None,
        "metadata": {}, "outputs": [], "source": src(text)
    }


def replace_in_source(cell, old, new):
    full = ''.join(cell['source'])
    full = full.replace(old, new)
    cell['source'] = src(full)


def insert_after(cells, insertions):
    """insertions: {original_idx: [list_of_cells_to_insert_after]}"""
    result = []
    for i, cell in enumerate(cells):
        result.append(cell)
        if i in insertions:
            result.extend(insertions[i])
    return result


# ======================================================
# NOTEBOOK 5: data_types_done_right.ipynb
# ======================================================
def improve_nb5():
    path = '2. SQL_essentials/5. data_types_done_right.ipynb'
    with open(path) as f:
        nb = json.load(f)
    cells = nb['cells']

    # Fix Cell 41 - Array Operations placeholder
    placeholder_41 = (
        'The important beginner shift here is moving from "it works on my machine" to '
        '"it behaves predictably in a real environment." Each step matters because it '
        'reduces surprises when the software runs elsewhere.'
    )
    new_text_41 = (
        'Array operations work on the entire array or individual elements using '
        'PostgreSQL-specific operators. The containment operator `@>` checks if an '
        'array includes all elements of another (order-independent). The overlap '
        'operator `&&` returns `TRUE` if two arrays share any element. Array '
        'concatenation uses `||` or `array_append()`/`array_prepend()`. Arrays are '
        '**1-indexed** in PostgreSQL—the first element is `arr[1]`, not `arr[0]`—a '
        'common source of off-by-one errors for developers coming from other languages.'
    )
    replace_in_source(cells[41], placeholder_41, new_text_41)

    # Insert hstore section after cell 44 (GIN array index code)
    hstore_md_text = """\
### 5.6.4 `hstore`: Key-Value Extension (PostgreSQL-Specific)

`hstore` is a PostgreSQL extension that stores a **flat** set of text key-value pairs in a single column. It predates `JSONB` and lacks nesting and typed values—both keys and values are `TEXT` (or `NULL`). It supports GIN and GiST indexing for key and value lookups, making it usable for attribute-bag patterns in legacy systems.

**When to use:** Prefer `JSONB` over `hstore` for all new development—`JSONB` supports nesting, typed values, and a richer operator set. You will encounter `hstore` mainly in legacy codebases; migrate to `JSONB` during refactoring."""

    hstore_code_text = """\
-- Enable the hstore extension (run once per database)
CREATE EXTENSION IF NOT EXISTS hstore;

-- hstore column definition
CREATE TABLE product_attributes (
    product_id BIGINT PRIMARY KEY,
    attrs      hstore NOT NULL DEFAULT ''::hstore
);

-- Insert key-value pairs (comma-separated key => value pairs)
INSERT INTO product_attributes VALUES
    (1, 'color => red, size => large, material => cotton');

-- Access a value by key (returns TEXT or NULL if key absent)
SELECT attrs -> 'color' FROM product_attributes;   -- 'red'
SELECT attrs -> 'missing_key';                      -- NULL

-- Test key existence
SELECT * FROM product_attributes WHERE attrs ? 'color';

-- Containment: rows that have this exact key-value pair
SELECT * FROM product_attributes WHERE attrs @> 'color => red';

-- GIN index for fast key/value lookups (same as JSONB)
CREATE INDEX idx_product_attrs ON product_attributes USING GIN (attrs);

-- Modern equivalent (prefer for new code):
-- attrs JSONB NOT NULL DEFAULT '{}'"""

    # Insert domain section and "when to use" quick reference after cell 48
    domain_md_text = """\
## 5.9 Domain Types: Reusable Column Constraints

A **`domain`** is a user-defined type that wraps an existing base type and attaches `NOT NULL` and/or `CHECK` constraints to it. Domains make validation logic reusable: define the rule once, apply it to any number of columns across any number of tables. Updating the domain's constraint immediately affects every column that uses it.

**When to use domains:**
- The same validation rule applies to the same semantic type in many places (e.g., every email column, every positive-price column)
- You want column types to be self-documenting (`email_address` is clearer than `TEXT CHECK (value ~ '^...$')`)
- You want a single point of change for validation logic—update the domain, not every table definition"""

    domain_code_text = """\
-- Define reusable validated types
CREATE DOMAIN email_address AS TEXT
    CHECK (
        VALUE ~ '^[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,}$'
        AND LENGTH(VALUE) <= 254  -- RFC 5321 maximum
    );

CREATE DOMAIN positive_amount AS NUMERIC(19, 4)
    CHECK (VALUE > 0);

CREATE DOMAIN url_slug AS TEXT
    CHECK (VALUE ~ '^[a-z0-9\\-]+$' AND LENGTH(VALUE) BETWEEN 1 AND 100);

-- Use domains in table definitions — constraints fire automatically on INSERT/UPDATE
CREATE TABLE contacts (
    contact_id  BIGINT          PRIMARY KEY,
    email       email_address   NOT NULL,  -- validated on every write
    work_email  email_address,             -- same domain, different column
    price       positive_amount NOT NULL,
    slug        url_slug        UNIQUE NOT NULL
);

-- INSERT with invalid email triggers domain constraint automatically:
-- INSERT INTO contacts VALUES (1, 'not-an-email', NULL, 9.99, 'ok-slug');
-- ERROR: value for domain email_address violates check constraint

-- Alter a domain (change propagates to ALL columns using it across ALL tables)
ALTER DOMAIN email_address
    ADD CONSTRAINT no_test_emails CHECK (VALUE NOT LIKE '%@test.%');

-- List existing domains in the current database
SELECT typname, pg_catalog.format_type(typbasetype, typtypmod) AS base_type
FROM pg_catalog.pg_type
WHERE typtype = 'd'
ORDER BY typname;"""

    when_to_use_text = """\
## Quick Reference: Choosing the Right Data Type

| Use Case | Recommended Type | Avoid |
|---|---|---|
| Primary keys (new systems) | `BIGINT GENERATED ALWAYS AS IDENTITY` | `SERIAL` (legacy) |
| External / public-facing IDs | `UUID` (`gen_random_uuid()`) | Exposing sequential `BIGINT` in URLs |
| Integer counts, ages, flags | `INTEGER` or `SMALLINT` | `BIGINT` when smaller fits |
| Financial amounts | `BIGINT` (cents) or `NUMERIC(19,4)` | `FLOAT`, `DOUBLE PRECISION`, `MONEY` |
| Scientific measurements | `REAL` or `DOUBLE PRECISION` | `NUMERIC` (overkill, 5-10x slower) |
| Variable-length text | `TEXT` + `CHECK` constraint | `VARCHAR(n)` (identical storage, less flexible) |
| Fixed-length codes (ISO 3166, currency) | `CHAR(n)` | `TEXT` when length truly varies |
| Binary data (images, files, hashes) | `BYTEA` | `TEXT` (encoding corruption risk) |
| Timestamps with timezone | `TIMESTAMPTZ` | `TIMESTAMP` (drops timezone context) |
| Date only (birthday, due date) | `DATE` | `TIMESTAMPTZ` (unnecessary precision) |
| Duration / elapsed time | `INTERVAL` | `INTEGER` days (loses month/year semantics) |
| Enumerated states | `ENUM` (stable) or lookup table (dynamic) | Plain `TEXT` (no constraint) |
| Tags / small value lists per row | `TEXT[]` + GIN index | Multiple join tables for simple tags |
| Dynamic / schemaless attributes | `JSONB` | `JSON` (no indexing), `hstore` (no nesting) |
| Time ranges / scheduling overlap | `TSTZRANGE` + exclusion constraint | Two separate `start`/`end` timestamp columns |
| Reusable validation rules | `DOMAIN` | Duplicating `CHECK` constraints in every table |

**Decision heuristic**: Start with `TEXT` + `CHECK`, `BIGINT`, `TIMESTAMPTZ`, and `NUMERIC`. Specialize only when you have a concrete reason: storage savings, performance measurement, or semantic clarity."""

    insertions = {
        44: [md(hstore_md_text), code_cell(hstore_code_text)],
        48: [md(domain_md_text), code_cell(domain_code_text), md(when_to_use_text)],
    }
    cells = insert_after(cells, insertions)
    nb['cells'] = cells

    with open(path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  NB5: {len(cells)} cells written")


# ======================================================
# NOTEBOOK 7: crud_and_filtering.ipynb
# ======================================================
def improve_nb7():
    path = '2. SQL_essentials/7. crud_and_filtering.ipynb'
    with open(path) as f:
        nb = json.load(f)
    cells = nb['cells']

    placeholder = (
        'Production-oriented material makes more sense when you see it as reliability work. '
        'The tools and steps here exist to make behavior repeatable, observable, and safer to change.'
    )

    # Cell 1: Replace placeholder with DML definition
    replace_in_source(cells[1], placeholder,
        '**DML (Data Manipulation Language)** is the subset of SQL responsible for adding, '
        'changing, and removing data: `INSERT`, `UPDATE`, `DELETE`, and (in PostgreSQL 15+) '
        '`MERGE`. DML statements participate in transactions, are governed by row-level security, '
        'trigger row-level triggers, and must satisfy all active constraints. Understanding how '
        'PostgreSQL executes each DML operation—and where it can fail under concurrent load—is '
        'the foundation of reliable application development.'
    )

    # Cell 9: Replace placeholder
    replace_in_source(cells[9], placeholder,
        '`UPDATE` modifies existing rows in-place. The critical production concerns are '
        '**atomicity** (the update fully succeeds or fully rolls back), **concurrency** '
        '(two transactions updating the same row create lock contention—without optimistic '
        'locking, one silently overwrites the other), and **performance** (large `UPDATE`s '
        'lock rows, generate WAL, and cause table bloat). Always narrow the scope with a '
        '`WHERE` clause, and use `RETURNING` to confirm exactly which rows were affected.'
    )

    # Cell 15: Replace placeholder
    replace_in_source(cells[15], placeholder,
        "`DELETE` removes rows that satisfy a `WHERE` clause. Unlike `TRUNCATE`, `DELETE` "
        'respects foreign key constraints, fires row-level triggers, and can be filtered '
        "row-by-row. Deleted rows are not immediately reclaimed from disk—PostgreSQL's MVCC "
        'model marks them as invisible and `VACUUM` reclaims the space later. Heavy repeated '
        'deletes on large tables therefore cause **table bloat** unless autovacuum keeps pace.'
    )

    # Cell 21: Replace performance advice placeholder
    perf_placeholder = (
        'Performance advice only becomes useful once you tie each technique to the bottleneck '
        'it addresses. Keep asking what is slow, how you can prove it, and what side effect each '
        'optimization introduces.'
    )
    replace_in_source(cells[21], perf_placeholder,
        'The `WHERE` clause filters rows before returning, updating, or deleting them. Whether '
        'the database uses an **index scan** (fast: jumps to matching rows via the index) or a '
        '**sequential scan** (slow: reads every row in the table) depends on whether the '
        'predicate is written in a way the index can satisfy. Writing **SARGable** '
        '(Search ARGument ABLE) predicates—conditions applied directly to indexed column values, '
        'without wrapping them in functions—is the single most impactful SQL optimization '
        'technique available to most developers.'
    )

    # Cell 23: Expand NULL semantics explanation
    null_old = 'SQL uses three-valued logic: TRUE, FALSE, and NULL. NULL comparisons require special operators.'
    null_new = """\
SQL uses **three-valued logic**: every expression evaluates to `TRUE`, `FALSE`, or `NULL` \
(unknown). **`NULL` semantics**: `NULL` means *absent* or *unknown*—it is not zero, empty \
string, or false. This differs fundamentally from boolean `false` in most programming languages.

**Core NULL rules:**
- `NULL = NULL` evaluates to `NULL` (we cannot know if two unknowns are equal)—use `IS NULL` to test for absence
- `NULL != 5` evaluates to `NULL` (not `FALSE`)
- `NOT NULL` evaluates to `NULL` (negating an unknown is still unknown)
- `TRUE AND NULL` → `NULL`  ·  `FALSE AND NULL` → `FALSE`  ·  `TRUE OR NULL` → `TRUE`  ·  `FALSE OR NULL` → `NULL`

**`WHERE` clause implication**: Only rows where the condition is `TRUE` are returned. \
Rows where the condition evaluates to `NULL` are **silently excluded**—this surprises \
developers when filtering nullable columns: `WHERE role != 'admin'` excludes rows where \
`role IS NULL`.

**NULL in aggregates**: `COUNT(*)` counts all rows; `COUNT(column)` skips `NULL` values. \
`SUM`, `AVG`, `MIN`, `MAX` all ignore `NULL`s silently."""
    replace_in_source(cells[23], null_old, null_new)

    # Insert SQL injection section before the chapter summary (cell 33)
    sqli_md_text = """\
## 7.6 Security: SQL Injection and Parameterized Queries

**SQL injection** is an attack where a malicious actor manipulates an application's SQL query \
by embedding SQL syntax into user-supplied input. When applications construct queries by string \
concatenation, an attacker can escape the intended query structure and execute arbitrary \
SQL—exposing, modifying, or deleting any data the database role can access.

**Why SQL injection is dangerous:**
- **Data theft**: `' UNION SELECT password FROM users --` dumps the passwords table
- **Authentication bypass**: `' OR '1'='1` makes `WHERE` conditions always evaluate `TRUE`
- **Data destruction**: `'; DROP TABLE orders; --` permanently destroys critical tables
- **Privilege escalation**: Superuser connections can call `pg_read_file()`, execute OS commands, or create backdoor accounts

**The fix: parameterized queries (prepared statements)**

A parameterized query separates the SQL *structure* (the template, sent once) from the \
*data* (sent separately as typed values). The database driver never interpolates user data \
into the SQL string—it is physically impossible for data to become SQL code, regardless of \
what the data contains."""

    sqli_code_text = """\
-- ============================================================
-- SQL INJECTION DEMONSTRATION (NEVER DO THIS IN PRODUCTION)
-- ============================================================

-- Scenario: the application builds a login query with string concatenation.
-- Attacker supplies: user_input = "' OR '1'='1"

-- Vulnerable application code (Python f-string):
--   query = f"SELECT * FROM users WHERE email = '{user_input}'"
--
-- Resulting SQL sent to PostgreSQL:
--   SELECT * FROM users WHERE email = '' OR '1'='1'
--                                        ^^^^^^^^^^^ always TRUE
--   RESULT: returns ALL rows -- authentication completely bypassed!

-- Another payload: user_input = "'; DROP TABLE users; --"
-- Resulting SQL:
--   SELECT * FROM users WHERE email = ''; DROP TABLE users; --'
--   RESULT: the ENTIRE users table is DROPPED.

-- ============================================================
-- SAFE: Parameterized queries (the only correct approach)
-- ============================================================

-- In raw PostgreSQL (PREPARE / EXECUTE syntax):
PREPARE get_user_by_email(TEXT) AS
    SELECT user_id, email, role
    FROM users
    WHERE email = $1;          -- $1 is a typed placeholder, NEVER interpolated

-- Safe execution with legitimate input:
EXECUTE get_user_by_email('alice@example.com');

-- Safe execution with malicious input -- returns 0 rows, causes no harm:
EXECUTE get_user_by_email(''' OR ''1''=''1');
-- The entire string is treated as literal text data, not SQL

-- ============================================================
-- APPLICATION CODE EXAMPLES
-- ============================================================

-- Python (psycopg2 / psycopg3) -- CORRECT:
--   cursor.execute(
--       "SELECT user_id, email FROM users WHERE email = %s",
--       (user_input,)       <-- data passed separately as a tuple
--   )
--
-- Python -- WRONG (SQL injection vulnerability):
--   cursor.execute(f"SELECT * FROM users WHERE email = '{user_input}'"  )
--   cursor.execute("SELECT * FROM users WHERE email = '" + email + "'"  )

-- Node.js (pg / node-postgres) -- CORRECT:
--   await client.query(
--       'SELECT * FROM users WHERE email = $1',
--       [userInput]         <-- data passed as array
--   );
--
-- Node.js -- WRONG:
--   await client.query(`SELECT * FROM users WHERE email = '${userInput}'`);"""

    sqli_rules_text = """\
**Parameterized Query Rules — Non-Negotiable:**

1. **Always use placeholders** (`$1, $2, ...` in PostgreSQL; `%s` in psycopg2; `?` in SQLite; `:name` in SQLAlchemy)—never f-strings, `format()`, or string concatenation for SQL construction.
2. **Validate input types** before the query: `int(user_id)` ensures an integer cannot smuggle SQL syntax.
3. **Principle of least privilege**: the database role your application uses should have only `SELECT`/`INSERT`/`UPDATE`/`DELETE` on the specific tables it needs—never `DROP`, `CREATE`, `TRUNCATE`, or superuser privileges.
4. **Use an ORM** (SQLAlchemy, Django ORM, Prisma, GORM) which parameterizes by default—but audit any `raw()`, `.execute()`, or string-format bypass patterns.
5. **Never trust any source of input**: URL parameters, form fields, cookies, HTTP headers, file names, and even values read back from the database can all carry injection payloads.
6. **Log and monitor**: SQL injection attempts often produce syntax errors or type mismatch errors. Structured error logging helps detect and respond to attacks."""

    insertions = {
        32: [md(sqli_md_text), code_cell(sqli_code_text), md(sqli_rules_text)],
    }
    cells = insert_after(cells, insertions)
    nb['cells'] = cells

    with open(path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  NB7: {len(cells)} cells written")


# ======================================================
# NOTEBOOK 8: joins_aggregation_and_set_logic.ipynb
# ======================================================
def improve_nb8():
    path = '2. SQL_essentials/8. joins_aggregation_and_set_logic.ipynb'
    with open(path) as f:
        nb = json.load(f)
    cells = nb['cells']

    # Cell 35: Replace placeholder with proper explanation
    placeholder = (
        'Production-oriented material makes more sense when you see it as reliability work. '
        'The tools and steps here exist to make behavior repeatable, observable, and safer to change.'
    )
    replace_in_source(cells[35], placeholder,
        '**Aggregate window functions** (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX` with `OVER()`) '
        'compute a cumulative or windowed value for each row without collapsing the result set. '
        'The **frame clause** controls which rows within the current partition are included in '
        "each row's calculation:\n\n"
        '- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` — running total from first row to current\n'
        '- `ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING` — centered 5-row moving average\n'
        "- `RANGE BETWEEN INTERVAL '7 days' PRECEDING AND CURRENT ROW` — rolling 7-day window by value\n\n"
        '**Frame modes:** `ROWS` counts physical rows by position; `RANGE` counts rows with the same '
        '`ORDER BY` value (handles ties identically); `GROUPS` counts peer groups (PostgreSQL 11+). '
        'The default frame when `ORDER BY` is present is `RANGE BETWEEN UNBOUNDED PRECEDING AND '
        'CURRENT ROW`—meaning without an explicit frame, aggregate windows are *cumulative*, not '
        'full-partition.'
    )

    # Insert "Window Functions vs GROUP BY" guidance after cell 40
    window_vs_groupby_text = """\
## When to Use Window Functions vs `GROUP BY`

| Scenario | Use | Why |
|---|---|---|
| Aggregate and collapse to one row per group | `GROUP BY` | Simpler; generally faster for pure summarization |
| Keep all rows **and** add a group-level value | Window function | `GROUP BY` removes individual rows |
| Rank, number, or order rows within a group | Window (`ROW_NUMBER`, `RANK`, `DENSE_RANK`) | No `GROUP BY` equivalent |
| Running totals, moving averages, cumulative sums | Window function + frame clause | Cannot be expressed with `GROUP BY` |
| Compare each row to its group aggregate (% of total) | Window function | `GROUP BY` loses per-row context |
| Deduplicate: keep first or last row per group | Window function + CTE + `WHERE rn = 1` | `GROUP BY` alone cannot select "the first row" |
| Multi-level subtotals + grand total | `ROLLUP` / `CUBE` / `GROUPING SETS` | Efficient single-pass multi-dimensional aggregation |

**The core rule**: If your output needs the **same number of rows as the input** (or a subset \
filtered by rank/position), use window functions. If your output needs **one summary row per \
group**, use `GROUP BY`.

**Performance note**: Window functions are evaluated after `WHERE`, `JOIN`, and `GROUP BY` but \
before `HAVING` and final `ORDER BY`. For complex queries, materializing intermediate window \
results into a CTE can improve plan stability. Always validate with `EXPLAIN ANALYZE`."""

    insertions = {
        40: [md(window_vs_groupby_text)],
    }
    cells = insert_after(cells, insertions)
    nb['cells'] = cells

    with open(path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  NB8: {len(cells)} cells written")


# ======================================================
# NOTEBOOK 9: functions_expressions_and_common_patterns.ipynb
# ======================================================
def improve_nb9():
    path = '2. SQL_essentials/9. functions_expressions_and_common_patterns.ipynb'
    with open(path) as f:
        nb = json.load(f)
    cells = nb['cells']

    # Cell 9: Replace string functions placeholder
    placeholder = (
        'Production-oriented material makes more sense when you see it as reliability work. '
        'The tools and steps here exist to make behavior repeatable, observable, and safer to change.'
    )
    replace_in_source(cells[9], placeholder,
        '**String functions** transform, extract, and compare text values within SQL. PostgreSQL '
        'provides both ANSI SQL standard functions (`SUBSTRING`, `TRIM`, `UPPER`, `LOWER`, '
        '`POSITION`) and PostgreSQL-specific extensions (`||` concatenation, `REGEXP_REPLACE`, '
        '`FORMAT`, `SPLIT_PART`). For multi-byte UTF-8 text, always use `CHAR_LENGTH()` '
        '(counts Unicode code points) rather than `LENGTH()` (counts bytes)—a single emoji '
        'is 1 character but 4 bytes. The `FORMAT()` function uses `%s` (value), `%I` (quoted '
        'identifier), and `%L` (quoted literal) for type-safe string construction without '
        'injection risk. **Date functions** (`DATE_TRUNC`, `DATE_PART`, `AGE`, `TO_CHAR`, '
        '`AT TIME ZONE`) are covered in Section 9.3 and operate on `TIMESTAMP`, `TIMESTAMPTZ`, '
        '`DATE`, and `INTERVAL` values.'
    )

    # Insert CTEs vs subqueries after cell 34 (CTE performance code)
    cte_vs_subquery_text = """\
## When to Use CTEs vs Subqueries

| Scenario | Prefer | Reason |
|---|---|---|
| Recursive queries (tree traversal, graph walks) | **CTE** (`WITH RECURSIVE`) | The only SQL construct that supports recursion |
| Long query with multiple logical steps | **CTE** | Each step is named; query reads top-to-bottom |
| Same result set referenced 2+ times in one query | **CTE** with `MATERIALIZED` | Prevents repeated evaluation of an expensive subquery |
| Short inline filter or simple lookup | **Subquery** | Less syntax overhead; planner optimizes freely |
| Correlated per-row scalar value | **Correlated subquery** or **LATERAL** | CTEs cannot reference outer query columns |
| Debugging intermediate results | **CTE** | Name each step; `SELECT * FROM step_name` isolates issues |
| Enforcing a specific execution order | **CTE** with `MATERIALIZED` | Acts as an optimization fence: computed once, result cached |

**PostgreSQL 12+ behavior**: CTEs are **not** automatically optimization fences—the planner may \
inline them and push predicates into the CTE body. To force materialization: \
`WITH my_cte AS MATERIALIZED (...)`. To force inlining: `WITH my_cte AS NOT MATERIALIZED (...)`. \
Before PostgreSQL 12, every CTE was always materialized regardless.

**General rule**: Use CTEs to make queries readable for humans; let the query planner handle \
performance decisions. Measure actual behavior with `EXPLAIN ANALYZE` before assuming a CTE or \
subquery is faster."""

    # Insert LATERAL vs regular JOINs guidance after cell 38 (LATERAL performance code)
    lateral_vs_joins_text = """\
## When to Use `LATERAL` vs Regular JOINs

A regular `JOIN` combines two complete table sets based on a matching condition—both sides are \
evaluated independently, then combined. `LATERAL` re-evaluates the right-side subquery \
**once per row of the left side**, with full access to left-table columns. It is a correlated \
subquery in the `FROM` clause that can return multiple rows per outer row.

| Scenario | Prefer | Reason |
|---|---|---|
| Top-N rows per group (top 3 orders per user) | **LATERAL** with `LIMIT` | Each outer row drives its own bounded inner query |
| Call a set-returning function with per-row arguments | **LATERAL** (often implicit) | The function argument must reference the current outer row |
| Outer table is small, inner table is large + indexed | **LATERAL** | Executes N focused index lookups—very fast |
| Both tables are large, full aggregation needed | **Window function** or `GROUP BY` | LATERAL executes N times; a single-pass plan is faster |
| Simple equality or range join | **Regular JOIN** | Simpler syntax; planner has full freedom to choose join strategy |
| Correlated scalar value (one result per outer row) | **Correlated subquery** or **LATERAL** | Both work; LATERAL is cleaner when returning multiple columns |
| Expand an array or set-returning function into rows | **LATERAL** (often implicit) | `FROM t, UNNEST(t.arr) AS elem` implicitly uses LATERAL |

**Key distinction**: Use LATERAL when the inner query *depends on* a specific value from the \
outer row—especially when it needs its own `LIMIT`, `ORDER BY`, or complex logic per outer row. \
Without a LATERAL, subqueries cannot reference outer table columns.

**Index requirement**: LATERAL is only fast if the inner subquery uses an index on the \
correlation column (e.g., `WHERE o.user_id = u.user_id` needs an index on \
`orders(user_id, ...)`). Without the index, LATERAL degrades to a nested-loop sequential scan."""

    insertions = {
        34: [md(cte_vs_subquery_text)],
        38: [md(lateral_vs_joins_text)],
    }
    cells = insert_after(cells, insertions)
    nb['cells'] = cells

    with open(path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  NB9: {len(cells)} cells written")


if __name__ == '__main__':
    print("Improving notebooks...")
    improve_nb5()
    improve_nb7()
    improve_nb8()
    improve_nb9()
    print("Done!")
