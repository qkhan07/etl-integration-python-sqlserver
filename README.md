# 🧩 ETL Integration — Python to SQL Server

## 🧠 Overview
This project demonstrates an automated **ETL (Extract, Transform, Load)** pipeline built with **Python**, **SQL Server**, and **Windows Task Scheduler**. It simulates loading Salesforce-style data (Accounts, Contacts, Opportunities) into a SQL Data Mart using CSV files as the data source.

---

## ⚙️ Phase 1–4 Summary
- Created database `SalesforceDataMart` in SQL Server.  
- Defined tables: `Accounts`, `Contacts`, and `Opportunities` with primary and foreign keys.  
- Designed relationships and constraints for referential integrity.  
- Built stored procedures and validation logic to handle schema consistency.  

---

## 🚀 Phase 5 — Python → SQL Server ETL Integration

### Description
A Python script (`etl_load_csv_to_sql.py`) reads CSV files from `/ETL/PY/Data/` and loads them into the SQL Server database **SalesforceDataMart** using `pandas`, `pyodbc`, and `python-dotenv`.

### Tech Stack
- Python 3.13  
- pandas  
- pyodbc  
- python-dotenv  
- SQL Server 2022  
- Windows Task Scheduler (for daily automation)

---

### 📁 Folder Structure
```
ETL-Integration-Python-SQLServer/
│
├── ETL/
│   └── PY/
│       ├── Data/
│       │   ├── Accounts.csv
│       │   ├── Contacts.csv
│       │   └── Opportunities.csv
│       ├── etl_load_csv_to_sql.py
│       ├── .env
│       ├── requirements.txt
│       └── etl_log.txt (auto-created after run)
│
└── README.md
```

---

### ⚙️ Environment Setup
Open Command Prompt in your `/ETL/PY/` folder and run:
```bash
python -m pip install -r requirements.txt
```

---

### ▶️ Running the ETL
Manual run:
```bash
python etl_load_csv_to_sql.py
```

Automated run via **Windows Task Scheduler**:

**Program/script:**
```
C:\Users\linkq\AppData\Local\Programs\Python\Python313\python.exe
```

**Add arguments:**
```
etl_load_csv_to_sql.py >> etl_log.txt 2>&1
```

**Start in:**
```
C:\Users\linkq\OneDrive\Documents\GitHub Folder\ETL-Integration-Python-SQLServer\ETL\PY
```

---

### ✅ Verification in SQL Server
Open SQL Server Management Studio (SSMS) and run:
```sql
USE SalesforceDataMart;
SELECT COUNT(*) AS Accounts FROM dbo.Accounts;
SELECT COUNT(*) AS Contacts FROM dbo.Contacts;
SELECT COUNT(*) AS Opportunities FROM dbo.Opportunities;
```

**Sample Output**
| Table | Count |
|--------|--------|
| Accounts | 2 |
| Contacts | 2 |
| Opportunities | 3 |

---

### 🧩 Key Features
- **Upsert (MERGE)** logic to update or insert data without duplicates.  
- **.env configuration** for secure connection strings.  
- **Automated scheduling** with Task Scheduler.  
- **Lightweight CSV-to-SQL ingestion** using `pandas` and `pyodbc`.  
- **Audit-ready folder structure** for production scalability.

---

### 🔒 Example `.env` File
```
SQLSERVER_CNXN=Driver={ODBC Driver 18 for SQL Server};Server=localhost;Database=SalesforceDataMart;Trusted_Connection=yes;Encrypt=no;
```

---

### 🧾 Example Log Output (`etl_log.txt`)
```
Loading Accounts...
Loading Contacts...
Loading Opportunities...
✅ ETL completed successfully!
```

---

### 📊 Business Value
- Demonstrates real-world **data ingestion automation**.  
- Builds a foundation for **data warehousing** or **Salesforce CRM analytics**.  
- Highlights skills in **Python ETL development, SQL design, and system integration.**

---

### 🧩 Troubleshooting Notes & Lessons Learned
- Resolved **Python PATH** and **PowerShell permission issues** by using the full executable path (`python.exe`).  
- Fixed **ODBC driver errors** by installing the correct `x64` Microsoft ODBC Driver 18 for SQL Server.  
- Verified **Windows Authentication** connection through `.env` and confirmed with `CONNECTED` test.  
- Successfully automated with **Windows Task Scheduler**, ensuring it runs even if the user is logged off.  
- Validated record counts and `MERGE` upsert logic in SSMS.  

---

### 🧩 Improvements (Optional Next Steps)
- Add incremental load logic (based on CreatedDate).  
- Include logging table inside SQL Server for audit tracking.  
- Create Power BI dashboard to visualize loaded data trends.  
- Deploy to Azure Data Factory or AWS Glue for cloud-based orchestration.

---

### ✨ Author
**Qasim Khan**  
ETL & Salesforce Integration Developer  
📧 [qkhan.tech@gmail.com](mailto:qkhan.tech@gmail.com)
