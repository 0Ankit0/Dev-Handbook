# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: System Design Reference Tables

### Latency Numbers Every Developer Should Know

| Operation | Approximate Latency |
|-----------|-------------------|
| L1 cache reference | ~1 ns |
| L2 cache reference | ~4 ns |
| RAM access | ~100 ns |
| SSD read (random) | ~100 µs (0.1 ms) |
| HDD read (random) | ~10 ms |
| Network: same datacenter | ~0.5 ms |
| Network: US to Europe | ~150 ms |
| Network: US to Australia | ~300 ms |

> **Key insight**: Memory is 1000x faster than SSD. Same-DC network is 5000x faster than cross-continent. These numbers drive architecture decisions like caching and CDN placement.

### Back-of-Envelope Estimation

| Metric | Reference Numbers |
|--------|------------------|
| 1 server (typical web app) | ~1,000-10,000 req/sec |
| 1 PostgreSQL instance | ~10,000-50,000 simple queries/sec |
| 1 Redis instance | ~100,000+ operations/sec |
| 1 GB data | ~1 billion bytes |
| 1 TB data | ~1 trillion bytes |
| 1 million users × 1 req/day | ~12 req/sec |
| 1 million users × 10 req/day | ~120 req/sec |

### Database Comparison Matrix

| Database | Type | Best For | Drawbacks |
|----------|------|----------|-----------|
| PostgreSQL | Relational (SQL) | Structured data, complex queries, ACID transactions | Less flexible schema |
| MySQL | Relational (SQL) | Web apps, read-heavy workloads | Historically weaker with complex queries |
| MongoDB | Document (NoSQL) | Flexible schema, hierarchical data | No joins, eventual consistency |
| Redis | In-memory key-value | Caching, sessions, pub/sub | Data limited to memory size |
| Cassandra | Wide-column (NoSQL) | High-write workloads, geo-distribution | Complex to operate, no joins |
| Elasticsearch | Search/analytics | Full-text search, log analytics | Not a primary database |
| Neo4j | Graph | Highly connected data (social graphs, routing) | Niche use cases |

---

## Appendix B: System Design Glossary

### Scalability

**Horizontal Scaling (Scale Out)**
Adding more machines to distribute load. E.g., going from 1 to 10 web servers. Requires a load balancer and stateless application design.

**Vertical Scaling (Scale Up)**
Making a single machine more powerful (more CPU, RAM). Simpler but has a ceiling. A database often scales vertically before you shard it.

**Load Balancer**
A component that distributes incoming requests across multiple servers. Prevents any single server from being overwhelmed. Common algorithms: round-robin, least connections, IP hash.

### Data Storage

**Sharding**
Splitting a database into smaller pieces (shards) distributed across multiple servers. Each shard holds a subset of the data (e.g., users A-M on shard 1, N-Z on shard 2). Enables horizontal scaling of databases but adds complexity.

**Replication**
Copying data to multiple servers for fault tolerance and read scaling. A **primary** handles writes; **replicas** handle reads. If the primary fails, a replica can be promoted.

**CAP Theorem**
In a distributed system, you can guarantee at most two of three properties:
- **Consistency**: Every read returns the most recent write
- **Availability**: Every request gets a (non-error) response
- **Partition Tolerance**: The system continues operating despite network partitions

In practice, partition tolerance is non-negotiable in distributed systems, so you choose between CP (consistent, may be unavailable during partitions) or AP (always available, may return stale data).

**ACID**
Database transaction properties: Atomicity (all or nothing), Consistency (valid state to valid state), Isolation (concurrent transactions don't interfere), Durability (committed data persists). Relational databases guarantee ACID.

**BASE**
Contrast to ACID, common in NoSQL: Basically Available, Soft-state, Eventually Consistent. Prioritizes availability over strict consistency.

### Caching

**Cache Hit / Cache Miss**
A cache hit means the requested data was found in the cache (fast). A cache miss means it wasn't — the system must fetch from the source (slow) and then store it in the cache.

**Cache Eviction Policies**
- **LRU (Least Recently Used)**: Evict the item that hasn't been accessed for the longest time. Most common.
- **LFU (Least Frequently Used)**: Evict the item accessed the fewest times.
- **TTL (Time to Live)**: Evict after a fixed duration, regardless of access.

**Cache Invalidation**
The hardest problem in caching: ensuring the cache doesn't serve stale data after the source changes. Strategies: write-through (update cache when source updates), write-behind (buffer writes), cache-aside (application manages cache).

### Reliability

**SLA (Service Level Agreement)**
A contractual promise about system availability or performance. "99.9% uptime" = at most ~8.7 hours of downtime per year.

**SLO (Service Level Objective)**
An internal target (usually stricter than SLA). The team aims for 99.95% internally to ensure SLA of 99.9% is met.

**SLI (Service Level Indicator)**
The actual measured metric (e.g., the percentage of successful requests over the past 30 days).

**Circuit Breaker**
A pattern that prevents cascading failures. If downstream service calls fail too often, the circuit "opens" and immediately returns an error (fast-fail) instead of waiting for timeouts. After a cooldown period, it allows a test request through.

**Rate Limiting**
Restricting how many requests a client can make in a time window. Protects services from being overwhelmed by a single client (intentionally or accidentally). Common algorithms: token bucket, sliding window.

### Architecture Patterns

**Microservices**
Architecture where an application is divided into small, independently deployable services, each owning its data and communicating over APIs. Enables teams to deploy independently but adds operational complexity.

**Monolith**
A single deployable unit containing all application logic. Simpler to develop and test initially. Can become hard to scale and change as it grows.

**Event-Driven Architecture**
Services communicate by producing and consuming events through a message broker (Kafka, RabbitMQ). Decouples producers from consumers; enables async processing. Common in microservices.

**API Gateway**
A single entry point for client requests that routes them to appropriate backend services. Handles authentication, rate limiting, logging, and protocol translation in one place.

---

## Appendix C: Further Reading

### Books
- *Designing Data-Intensive Applications* — Martin Kleppmann (essential reading)
- *System Design Interview* Vol. 1 & 2 — Alex Xu
- *Building Microservices* — Sam Newman
- *The Art of Scalability* — Martin Abbott

### Engineering Blogs
- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- [Google Cloud Architecture Center](https://cloud.google.com/architecture)
- [Uber Engineering](https://www.uber.com/en-US/blog/engineering/)
- [Netflix Tech Blog](https://netflixtechblog.com/)
- [Discord Engineering](https://discord.com/category/engineering)

### Practice
- [system-design-primer](https://github.com/donnemartin/system-design-primer) — GitHub
- [ByteByteGo](https://bytebytego.com/) — visual system design explanations
