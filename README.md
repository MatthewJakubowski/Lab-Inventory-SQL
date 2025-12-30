<div align="center">
  <img src="https://raw.githubusercontent.com/MatthewJakubowski/Universal-Lab-Converter/main/going_dark_cover.jpg" width="100%" alt="System Status: Going Dark. Deep Work Protocol.">
</div>

# 🧪 Smart Reagent Manager (SQL)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![AI Assisted](https://img.shields.io/badge/AI_Co--Pilot-Google_Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white)
![Status](https://img.shields.io/badge/Status-Educational_Demo-orange?style=for-the-badge)

> **Inventory Management System for Clinical Laboratories.**
> Solves the problem of expired reagents using a persistent SQLite database.

---

## 🤖 AI & Learning Transparency
**This project is part of my transition from Medical Analysis to Software Engineering (#FromPipetteToPython).**

The database architecture and SQL query logic were designed with the mentorship of **Google Gemini**. I focused on understanding **CRUD operations** (Create, Read, Update, Delete) and implementing them in a clean, functional CLI application.

---

## 📋 Overview
Managing reagent lots and expiration dates in a busy laboratory is often done manually or in Excel, leading to waste and errors. **Smart Reagent Manager** is a Python-based tool that replaces spreadsheets with a structured **Relational Database (SQL)**.

It allows laboratory staff to:
* **Track** current inventory levels.
* **Monitor** expiration dates automatically.
* **Remove** used or expired kits from the system.

This project demonstrates my ability to integrate Python with **SQLite**, perform **CRUD operations**, and handle date logic.

---

## ⚡ Key Features
* **💾 Persistent Storage (SQLite3):** Data is stored in a local `magazyn.db` file, ensuring inventory persists between sessions (unlike RAM-based variables).
* **🔍 Auto-Expiry Detection:** Automatically queries the database for items where `expiration_date < today` and triggers an alarm 🚨.
* **🛠️ Full CRUD Functionality:**
    * **Create:** Add new reagent lots (`INSERT`).
    * **Read:** View full inventory status (`SELECT`).
    * **Delete:** Remove used/expired reagents (`DELETE`).
* **🛡️ Input Validation:** Prevents crashes by validating numerical inputs (e.g., quantity, ID).

---

## 🚀 How to Run

### Prerequisites
* Python 3.x (Standard library, no `pip install` required).

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
    * `[2]` **Add New Reagent** (Dodaj nowy odczynnik)
    * `[3]` **Check Expiry Dates** (Sprawdź terminy ważności)
    * `[4]` **Remove Reagent** (Usuń odczynnik / Zużycie)
    * `[5]` **Exit** (Wyjście)

---

## 👨‍🔬 About the Author

**Mateusz Jakubowski**
*Medical Analyst (15y exp) ➡️ Aspiring AI Engineer & Python Developer.*

I am building tools that bridge the gap between Medical Diagnostics and IT. This project was developed entirely on a mobile environment (**Samsung DeX** + **Pydroid 3**).

* **Connect with me:** [LinkedIn](https://www.linkedin.com/in/mateuszjakubowski)
* **Portfolio:** #FromPipetteToPython

---

### ⚠️ Disclaimer
*This software is for educational purposes only. It is not a validated Laboratory Information System (LIS) and should not be used as the sole method for managing critical clinical inventory.*
