# Handbook Rewrite Audit

| Handbook | TOC Chapters | Notebooks | Missing Links | Broken Links | Orphans | Intro Issues | Malformed Dirs | Likely Missing Subtopic Sections |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| django | 50 | 50 | 1 | 0 | 0 | 0 | 0 | 0 |
| fastapi | 25 | 25 | 0 | 0 | 0 | 0 | 0 | 20 |
| asp_net | 25 | 25 | 0 | 0 | 0 | 0 | 0 | 1 |
| csharp | 29 | 29 | 0 | 0 | 0 | 0 | 0 | 8 |
| aspire | 12 | 16 | 0 | 0 | 4 | 0 | 0 | 4 |
| graphql | 17 | 17 | 0 | 0 | 0 | 0 | 0 | 2 |
| dsa | 40 | 40 | 0 | 0 | 0 | 0 | 0 | 13 |
| project_management | 20 | 20 | 0 | 0 | 0 | 0 | 0 | 1 |
| ci_cd | 62 | 66 | 0 | 0 | 4 | 0 | 0 | 14 |
| cybersecurity | 19 | 19 | 0 | 0 | 0 | 0 | 0 | 2 |

## django

- Missing TOC links: Chapter 18: Testing (Unit, Integration, E2E)

## fastapi

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 1: Setting Up the Development Environment: 1.1 Modern Python Setup: Virtual environments (venv) and package management (pip vs uv)., 1.3 The ASGI Server: Understanding Uvicorn and the role of ASGI., 1.5 Your First API: Creating a "Hello World" endpoint and understanding the instance app.
  - Chapter 2: Routing and Basic Path Operations: 2.2 Path Parameters: Dynamic URLs, type conversion, and validation., 2.3 Query Parameters: Optional arguments, default values, and required query params., 2.5 Response Models: Defining response shapes and automatic filtering.
  - Chapter 3: Automatic Documentation: 3.2 ReDoc: Alternative documentation at /redoc., 3.3 OpenAPI Specification: Understanding the JSON Schema behind your API., 3.4 Customizing Docs: Hiding endpoints, renaming, and organizing tags.
  - Chapter 5: Advanced Data Handling: 5.2 Serialization: Controlling JSON output, aliases, and excluding fields.
  - Chapter 6: Dependency Injection System: 6.4 Overrides: Testing and mocking dependencies efficiently.
  - Chapter 7: Request Handling and Context: 7.3 Cookies: Reading and setting cookies securely., 7.4 Headers: Accessing and manipulating HTTP headers.
  - Chapter 9: Project Architecture: 9.1 Modularization: Breaking the app into multiple files., 9.2 APIRouter: Creating mini-applications and mounting them., 9.3 The "Service-Repository" Pattern: Separating business logic from route logic., 9.4 Configuration Management: Centralizing settings.
  - Chapter 10: Middleware and Events: 10.3 Custom Middleware: Creating your own middleware classes.

## asp_net

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 25: Monitoring and Observability: Staying up-to-date with the .NET ecosystem, B: Cheat Sheet: Essential CLI commands (dotnet new, dotnet ef, dotnet run), C: Glossary of Terms

## csharp

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 3: Control Flow in Action: Loops: for, foreach, while, do-while
  - Chapter 5: Methods - The Building Blocks of Logic: This part covers the heart of C# development, teaching how to model real-world entities and build robust, maintainable code.*
  - Chapter 11: Encapsulation & Best Practices: This part moves into more sophisticated areas of the language that experienced C# developers use daily.*
  - Chapter 17: Pattern Matching in Depth: Property, Positional, and Tuple Patterns, This part focuses on the tools and libraries that make up the modern .NET developer's environment.*
  - Chapter 20: Attributes and Reflection: What are Attributes? Predefined Attributes ([Obsolete], [Serializable])
  - Chapter 21: Dependency Injection (DI): The Problem of Tight Coupling
  - Chapter 23: Unit Testing for Quality Code: Mocking Dependencies with Moq / NSubstitute, This part prepares the reader for complex, real-world enterprise development.*
  - Chapter 29: The Road Ahead - What's New in C#: A Look at the Latest Language Features (e.g., Required Members, Raw String Literals, List Patterns), C: Recommended Tools and Libraries, D: Glossary of Terms

## aspire

- Orphan notebooks: aspire/1. laying_the_foundation/1. welcome_to_the_distributed_world.ipynb, aspire/1. laying_the_foundation/2. your_first_net_aspire_application.ipynb, aspire/1. laying_the_foundation/3. the_service_defaults_project.ipynb, aspire/1. laying_the_foundation/4. the_apphost_project_application_modeling.ipynb
- Chapters with likely missing TOC-covered subtopics:
  - Chapter 5: .NET Aspire Components: The "Connection String" Abstraction: How Aspire manages connections.
  - Chapter 12: Security from the Start: Integrating with Identity Providers:, Using the Aspire.Keycloak component (or similar) for auth., Passing connection strings and credentials securely to containers.
  - Chapter 13: Deployment Fundamentals with Aspire: Understanding the output: How Aspire resources map to Kubernetes concepts (Deployments, Services, ConfigMaps).
  - Chapter 16: Real-World Project Structure and Best Practices: Deploying the validated manifest., C. Glossary of Terms

## graphql

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 13: Monitoring and Observability: 13.4 Debugging with Apollo Sandbox and Extensions
  - Chapter 17: Future Trends and Conclusion: Appendix A: Common GraphQL Anti-Patterns, Appendix B: Glossary of Terms, Appendix C: Comparison of GraphQL Server Libraries, Appendix D: Useful Resources and Community Links

## dsa

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 9: Non-Comparison Sorting: Bucket Sort and Uniform Distribution Analysis
  - Chapter 10: Searching Algorithms: Binary Search: Standard, Lower/Upper Bound, Bisection Methods
  - Chapter 11: Binary Trees: Traversal Techniques: Recursive and Iterative (In-order, Pre-order, Post-order, Level-order), Diameter, Height, and LCA (Lowest Common Ancestor) Algorithms
  - Chapter 14: Heaps and Priority Queues: Heap Sort and Partial Sorting
  - Chapter 18: Minimum Spanning Trees: Applications: Cluster Analysis, Approximation Algorithms for TSP
  - Chapter 22: Greedy Algorithms: Task Scheduling and Load Balancing
  - Chapter 23: Dynamic Programming: Knapsack Variations (0-1, Unbounded, Bounded, Multiple), Interval DP (Matrix Chain Multiplication, Palindrome Partitioning), DP on Graphs (Shortest Path, DAG), Knuth Optimization and Monotone Queue Optimization
  - Chapter 24: String Matching: Z-Algorithm and Z-Box Computation

## project_management

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 20: The Future of Technical Project Management: Appendix A: Templates and Boilerplates*, A.1 Project Charter Template, A.2 Sprint Planning Template, A.3 Risk Register Template, A.4 Status Report Template

## ci_cd

- Orphan notebooks: ci_cd/11. real_world_projects/1. simple_web_app.ipynb, ci_cd/11. real_world_projects/2. microservices_architecture.ipynb, ci_cd/11. real_world_projects/3. multi_environment_enterprise_app.ipynb, ci_cd/11. real_world_projects/4. database_intensive_app.ipynb
- Chapters with likely missing TOC-covered subtopics:
  - Chapter 8: Advanced Docker Techniques: 8.3 Layer Caching Strategies
  - Chapter 9: Docker Image Optimization: 9.1 Image Size Reduction Techniques, 9.4 Build-time vs. Run-time Arguments, 9.5 Security Scanning Images
  - Chapter 11: Docker Registries: 11.2 Private Registry Options, 11.5 Azure ACR, 11.8 Image Tagging Strategies
  - Chapter 31: Kubernetes Deployments: 31.7 Rollback Commands
  - Chapter 33: Advanced Helm: 33.1 Writing Templates, 33.3 Values Files and Overrides, 33.6 Helm Plugins
  - Chapter 39: Multi-Environment Deployments: 39.8 Production Readiness Checks
  - Chapter 41: Database CI/CD: 41.6 Data Seeding, 41.8 NoSQL Considerations
  - Chapter 42: Infrastructure as Code in CI/CD: 42.6 Planning and Applying Changes, 42.7 Destruction and Cleanup

## cybersecurity

- Chapters with likely missing TOC-covered subtopics:
  - Chapter 18: Security Architecture & Engineering: 18.2 Secure Network Design: Segmentation, DMZs, and Cloud VPCs, 18.3 Application Security Architecture: WAFs, RASPs, and Microservices Security, 18.5 Security Pattern Library: Reusable Solutions for Common Problems
  - Chapter 19: Career Development & Continuous Learning: A: Comprehensive Glossary of Cybersecurity Terms, C: Lab & Exercise Index by Chapter and Tool, D: Mapping of Book Content to NIST CSF 2.0, OWASP Top 10, ISO 27001, and SANS Courses, E: Further Reading and Recommended Resources, Index*
