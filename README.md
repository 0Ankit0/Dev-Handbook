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

When adding new content:
1. Create/update the TOC.md file with chapter structure
2. Run `create_folders.py` to generate folder structure and notebooks
3. Fill in the content in the generated notebooks
4. Run `add_nav_links.py` to add navigation links between notebooks

## 📄 License

This repository is for educational purposes.

---

**Note**: This is a living document that grows with continuous learning and exploration of new technologies.
