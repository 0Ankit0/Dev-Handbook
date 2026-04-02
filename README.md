# Dev-Handbook

A structured, beginner-friendly developer handbook covering 26 technology domains — from Python fundamentals to AI engineering, from system design to blockchain. Each handbook is an interactive Jupyter notebook series written to be read sequentially, with clear definitions, practical examples, and navigation links throughout.

---

## How to Use This Handbook

Each handbook section follows a progressive learning path:
1. **Open the `TOC.md`** in any topic folder to see the full chapter list.
2. **Open notebooks sequentially** — each chapter builds on the previous one.
3. **Every chapter has navigation links** at the top and bottom to move between chapters.
4. **Use Jupyter Lab or Jupyter Notebook** to read the `.ipynb` files interactively.

```bash
# Install Jupyter if you don't have it
pip install jupyterlab

# Launch from the repository root
jupyter lab
```

> **Tip:** You can also read the notebooks on GitHub directly — GitHub renders `.ipynb` files in the browser without needing Jupyter.

---

## 📚 Handbook Index

### 🐍 Python Ecosystem

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [Python](./python/TOC.md) | 22 | Core language, OOP, async, testing, packaging |
| [Django](./django/TOC.md) | 50 | Full-stack web apps with Python's most complete framework |
| [FastAPI](./fastapi/TOC.md) | 25 | High-performance async APIs with automatic docs |
| [Flask](./flask/TOC.md) | 19 | Lightweight web apps and REST APIs |

### 🟦 .NET Ecosystem

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [C#](./csharp/TOC.md) | 29 | C# language fundamentals to advanced patterns |
| [ASP.NET Core](./asp_net/TOC.md) | 25 | Web APIs, MVC, authentication, and deployment |
| [.NET Aspire](./aspire/TOC.md) | 16 | Cloud-native distributed app development |

### 🌐 Frontend

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [Frontend Fundamentals](./frontend/TOC.md) | 30 | HTML, CSS, JavaScript, and browser APIs |
| [TypeScript](./typescript/TOC.md) | 46 | Static typing, type system mastery, tooling |
| [Next.js](./nextjs/TOC.md) | 54 | React framework for production — SSR, routing, deployment |
| [Flutter](./flutter/TOC.md) | 54 | Cross-platform mobile and web apps with Dart |

### 🗄️ Databases

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [PostgreSQL](./postgres/TOC.md) | 48 | Relational database design, queries, optimization |
| [GraphQL](./graphql/TOC.md) | 17 | Query language, schemas, resolvers, federation |

### 🤖 AI & Data Science

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [AI Engineering](./ai_engineering/TOC.md) | 32 | ML fundamentals, deep learning, LLMs, MLOps |
| [Time Series Prediction](./time_series_prediction/TOC.md) | 99 | Statistical methods, neural networks, production forecasting |
| [Share Analysis](./share_analysis/TOC.md) | 21 | Financial data analysis, portfolio theory, modeling |

### 🏗️ Computer Science Fundamentals

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [Data Structures & Algorithms](./dsa/TOC.md) | 40 | Arrays, trees, graphs, sorting, complexity analysis |
| [Design Patterns](./design_patterns/TOC.md) | 22 | Creational, structural, behavioral, and architectural patterns |
| [System Design](./system_design/TOC.md) | 26 | Scalability, caching, databases, distributed systems |
| [Networking](./networking/TOC.md) | 24 | TCP/IP, HTTP, DNS, TLS, protocols |

### ⚙️ DevOps & Cloud

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [CI/CD](./ci_cd/TOC.md) | 66 | Pipelines, Docker, Kubernetes, GitHub Actions, deployment |
| [Cloud Computing](./cloud_computing/TOC.md) | 24 | AWS/GCP/Azure, serverless, IaC, cost optimization |

### 🔒 Security & Quality

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [Cybersecurity](./cybersecurity/TOC.md) | 19 | Threat models, secure coding, encryption, pen testing |
| [Software Testing](./software_testing/TOC.md) | 77 | Unit, integration, E2E, performance, and security testing |

### ⛓️ Other Topics

| Handbook | Chapters | What You'll Learn |
|----------|----------|-------------------|
| [Blockchain](./blockchain/TOC.md) | 40 | Distributed ledgers, smart contracts, DeFi, Solidity |
| [Project Management](./project_management/TOC.md) | 20 | Agile, Scrum, Kanban, estimation, team dynamics |

---

## 📖 Recommended Learning Paths

If you're not sure where to start, here are some suggested paths:

### Path 1: Python Backend Developer
`Python` → `Flask` → `FastAPI` → `Django` → `PostgreSQL` → `CI/CD`

### Path 2: Full-Stack JavaScript Developer
`Frontend Fundamentals` → `TypeScript` → `Next.js` → `GraphQL` → `System Design`

### Path 3: AI / ML Engineer
`Python` → `AI Engineering` → `Time Series Prediction` → `System Design` → `CI/CD`

### Path 4: DevOps / Cloud Engineer
`Networking` → `CI/CD` → `Cloud Computing` → `System Design` → `Cybersecurity`

### Path 5: Computer Science Foundations
`Data Structures & Algorithms` → `System Design` → `Design Patterns` → `Networking`

---

## 🗂️ Repository Structure

Each handbook directory follows this layout:

```text
<handbook_name>/
├── TOC.md              ← Table of contents with chapter links
├── appendix.md         ← Cheat sheets, glossary, and extra reference
├── 1. section_name/
│   ├── 1. chapter_name.ipynb
│   ├── 2. chapter_name.ipynb
│   └── ...
├── 2. section_name/
│   └── ...
└── ...
```

---

## 🛠️ Maintenance Utilities

The repository includes scripts for maintaining content quality:

| Script | Purpose |
|--------|---------|
| `add_nav_links.py` | Adds/updates Previous ↔ Next navigation in all notebooks |
| `update_toc_links.py` | Converts chapter names in TOC.md files to clickable links |
| `create_folders.py` | Generates folder structure from a TOC.md outline |
| `rewrite_handbooks_for_beginners.py` | Audit orchestrator for structural normalization |
| `scripts/fix_handbook_quality.py` | Removes boilerplate, labels code fences, converts ASCII cells |

```bash
# Regenerate navigation links for a section
python3 add_nav_links.py flask

# Update TOC links for all handbooks
python3 update_toc_links.py

# Run quality fixes across all notebooks
python3 scripts/fix_handbook_quality.py

# Target one section
python3 scripts/fix_handbook_quality.py --section python
```

---

## 📄 License

This repository is for educational purposes.

---

*This is a living document — content grows as new topics are explored and existing chapters are improved.*
