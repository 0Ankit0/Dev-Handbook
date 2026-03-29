# Developer Handbook

A comprehensive collection of learning materials, tutorials, and reference guides covering modern software development technologies and best practices.

## 📚 Topics Covered

This handbook contains structured content across 25+ technology domains:

### **Backend Development**
- [Python](./python/) - Core Python programming with Jupyter notebooks
- [Django](./django/) - Python web framework
- [FastAPI](./fastapi/) - Modern Python API framework
- [ASP.NET](./asp_net/) - .NET web framework
- [C#](./csharp/) - C# programming language
- [Aspire](./aspire/) - .NET cloud-native development

### **Frontend Development**
- [Frontend](./frontend/) - HTML, CSS, JavaScript fundamentals
- [TypeScript](./typescript/) - Typed JavaScript
- [Next.js](./nextjs/) - React framework
- [Flutter](./flutter/) - Cross-platform UI toolkit

### **Database & Data Management**
- [PostgreSQL](./postgres/) - Relational database
- [GraphQL](./graphql/) - Query language for APIs

### **Data Science & AI**
- [AI Engineering](./ai_engineering/) - AI and machine learning
- [Time Series Prediction](./time_series_prediction/) - Forecasting techniques
- [Share Analysis](./share_analysis/) - Financial data analysis

### **Computer Science Fundamentals**
- [Data Structures & Algorithms](./dsa/) - Core CS concepts
- [Design Patterns](./design_patterns/) - Software design patterns
- [System Design](./system_design/) - Architecture and scalability
- [Networking](./networking/) - Network protocols and concepts

### **DevOps & Cloud**
- [CI/CD](./ci_cd/) - Continuous integration and deployment
- [Cloud Computing](./cloud_computing/) - Cloud platforms and services

### **Security & Quality**
- [Cybersecurity](./cybersecurity/) - Security best practices
- [Software Testing](./software_testing/) - Testing methodologies

### **Other Topics**
- [Blockchain](./blockchain/) - Distributed ledger technology
- [Project Management](./project_management/) - PM methodologies

## 🛠️ Utilities

The repository includes Python utilities for content management:

- **`rewrite_handbooks_for_beginners.py`** - Deterministic rewrite orchestrator for auditing, intro cleanup, structural normalization, and relinking
  ```bash
  # Audit all handbooks and write report files
  python3 rewrite_handbooks_for_beginners.py --audit --report

  # Cleanup intro meta text only and regenerate links/navigation
  python3 rewrite_handbooks_for_beginners.py --cleanup-intros --regenerate-links

  # Run full pre-wave normalization plus Wave 1-4 maintenance sweep
  python3 rewrite_handbooks_for_beginners.py --run-full-sweep --audit --report
  ```

  ```bash
  # Target specific handbooks
  python3 rewrite_handbooks_for_beginners.py --audit --handbooks ai_engineering system_design
  python3 rewrite_handbooks_for_beginners.py --cleanup-intros --handbooks django ci_cd
  ```

- **`create_folders.py`** - Generates folder structure from Table of Contents (TOC.md) files
  ```bash
  python create_folders.py <folder_path>
  ```

- **`add_nav_links.py`** - Adds navigation links to Jupyter notebooks for easy traversal
  ```bash
  python add_nav_links.py <folder_path>
  ```

- **`update_toc_links.py`** - Converts chapter names in TOC.md files to clickable links
  ```bash
  python3 update_toc_links.py           # Update all TOC files
  python3 update_toc_links.py <folder>  # Update specific folder
  ```

## 📖 Structure

Each topic folder typically contains:
- **TOC.md** - Table of contents with organized chapters/sections
- **Numbered folders** - Organized by parts/modules (e.g., `1. fundamentals`)
- **Jupyter notebooks** (`.ipynb`) or markdown files with detailed content
- **Supporting materials** - Code examples, diagrams, appendices

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dev_handbook
   ```

2. **Browse topics** - Navigate to any topic folder of interest

3. **Open notebooks** - Use Jupyter Lab/Notebook to view `.ipynb` files
   ```bash
   jupyter lab
   ```

4. **Follow the TOC** - Each topic has a TOC.md for structured learning

## 📝 Usage Tips

- Start with the **TOC.md** in each topic folder to understand the content structure
- Notebooks include navigation links at the bottom for sequential learning
- Use search functionality to find specific concepts across topics
- Utilities help maintain consistent structure when adding new content

## 🤝 Contributing

When adding or revising content:
1. Update chapter content and TOC structure.
2. Run a focused audit and generate a report:
   ```bash
   python3 rewrite_handbooks_for_beginners.py --audit --handbooks <handbook_name> --report
   ```
3. Run intro cleanup only when banned meta framing is present:
   ```bash
   python3 rewrite_handbooks_for_beginners.py --cleanup-intros --handbooks <handbook_name>
   ```
4. Regenerate TOC links and notebook navigation:
   ```bash
   python3 update_toc_links.py <handbook_name>
   python3 add_nav_links.py <handbook_name>
   ```
5. Re-run the audit and confirm no missing links, broken links, malformed `.ipynb` directories, or orphan notebooks remain.

## 📄 License

This repository is for educational purposes.

---

**Note**: This is a living document that grows with continuous learning and exploration of new technologies.
