# 🚀 Project Structure Generator (CLI Utility)

A professional-grade Python CLI tool that automatically generates nested folder and file structures from a formatted text file.

Designed for developers who want fast, safe, and repeatable project scaffolding — without overwriting existing work.

---

## ✨ Key Features

- **📂 Deep Nesting:** Create complex folder structures instantly.
- **🔄 Smart Merge Mode:** Safely skips existing files; **never** overwrites your work.
- **🧪 Dry Run Mode:** Preview the exact folder tree before execution.
- **🛡 Robust Error Handling:** Gracefully handles invalid paths and permissions.
- **⚡ Lightweight:** Dependency-free (uses only standard library).
- **🖥 Cross-Platform:** Works on Windows (C:/, D:/), Linux, and macOS.

---

## 📌 Problem It Solves

Setting up a new project manually is repetitive and error-prone:
1. Manually creating folders.
2. Adding boilerplate files.
3. Maintaining structure consistency across teams.

This tool automates that entire process safely and efficiently.

🚀 Usage
▶ Normal Execution
python generate_structure.py

Creates the structure safely in the default drive.

▶ Custom Drive
python generate_structure.py --drive "C:\\Projects"
▶ Custom Structure File
python generate_structure.py --file custom_structure.txt
▶ Dry Run Mode (Recommended Before First Run)
python generate_structure.py --dry-run
