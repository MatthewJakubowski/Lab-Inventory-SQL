<div align="center">
  <img src="https://raw.githubusercontent.com/MatthewJakubowski/Universal-Lab-Converter/main/going_dark_cover.jpg" width="100%" alt="System Status: Going Dark. Deep Work Protocol.">
</div>

# 🧪 Smart Reagent Manager (SQL)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![AI Assisted](https://img.shields.io/badge/AI_Co--Pilot-Google_Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white)
![Status](https://img.shields.io/badge/Status-v1.2_Active-success?style=for-the-badge)

> **Inventory Management System for Clinical Laboratories.**
> Solves the problem of expired reagents using a persistent SQLite database.

---

## 🤖 AI & Learning Transparency
**This project is part of my transition from Medical Analysis to Software Engineering (#FromPipetteToPython).**

The database architecture and SQL query logic were designed with the mentorship of **Google Gemini**. I focused on understanding **CRUD operations** and **File Parsing** (importing data from external text files).

---

## 📋 Overview
Managing reagent lots and expiration dates in a busy laboratory is often done manually. **Smart Reagent Manager** is a Python-based tool that replaces spreadsheets with a structured **Relational Database (SQL)**.

It allows laboratory staff to:
* **Track** inventory levels.
* **Monitor** expiration dates automatically.
* **Import** bulk deliveries from electronic invoices (simulated via `.txt` files).

---

## ⚡ Key Features (v1.3)
* **🧠 Smart Import Logic:** The system intelligently detects input files (`dostawa.csv` takes priority over `dostawa.txt`) and automatically adjusts to the delimiter used (commas `,` or semicolons `;`), making it compatible with both standard text files and regional Excel exports.
* **💾 Persistent Storage (SQLite3):** Data is stored in a local `magazyn.db` file.
* **🔍 Auto-Expiry Detection:** Automatically queries the database for items where `expiration_date < today`.
* **🛠️ Full CRUD Functionality:** Create, Read, Delete, and Batch Insert.

---

## 🚀 How to Run

### Prerequisites
* Python 3.x (Standard library).

### Usage
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MatthewJakubowski/Lab-Inventory-SQL.git](https://github.com/MatthewJakubowski/Lab-Inventory-SQL.git)
    ```
2.  **Run the application:**
    ```bash
    python main.py
    ```
3.  **Navigate the Menu:**
    * `[1]` **View Inventory** (Pokaż stan magazynu)
    * `[2]` **Add New Reagent** (Ręcznie)
    * `[3]` **Check Expiry Dates** (Sprawdź terminy)
    * `[4]` **Remove Reagent** (Zużycie)
    * `[5]` **Import Delivery** (Auto-Detect CSV/TXT)
    * `[6]` **Exit**

## 📂 Supported Import Formats
To use the **Smart Import** feature (Option 5), place one of the following files in the project folder:

**Option A: Standard CSV/TXT (Comma Separated)**
*Filename: `dostawa.txt` or `dostawa.csv`*
```text
Magnesium R1,2025-12-31,5
Calcium Arsenazo,2024-06-30,2
```
**Option B: Regional/Excel CSV (Semicolon Separated)**
*Filename: `dostawa.csv` (Priority File)*
```text
Sodium;2025-05-20;20
Potassium;2024-12-12;15
```
## 👨‍🔬 About the Author

**Mateusz Jakubowski**
*Medical Analyst (15y exp) ➡️ Aspiring AI Engineer & Python Developer.*

I am building tools that bridge the gap between Medical Diagnostics and IT. This project was developed entirely on a mobile environment (**Samsung DeX** + **Pydroid 3**).

* **Connect with me:** [LinkedIn](https://www.linkedin.com/in/mateuszjakubowski)
* **Portfolio:** #FromPipetteToPython

---

### ⚠️ Disclaimer
*This software is for educational purposes only. It is not a validated Laboratory Information System (LIS) and should not be used as the sole method for managing critical clinical inventory.*
