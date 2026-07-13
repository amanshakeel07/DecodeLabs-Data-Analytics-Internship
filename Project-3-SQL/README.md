# Project 3: Relational SQL Data Analysis

## 📌 Project Overview
Welcome to the **Project-3-SQL** module. This folder contains a fully self-contained, production-ready relational data pipeline designed for the **DecodeLabs Data Analytics Internship**. 

The goal of this project is to move away from spreadsheet constraints and utilize a programmatic **SQL Relational Database Engine** (`SQLite3`) inside Python to interrogate clean transaction records, aggregate key performance benchmarks, and isolate high-value market outliers.

---

## 📁 Folder Contents & Architecture
The folder is structured to run efficiently with zero-dependency path configurations:

* **`Cleaned_Data_Project1.csv`**: The curated corporate transaction dataset built during your Week 1 pipeline.
* **`Project-3-SQL.py`**: The complete automated Python automation script that sets up an in-memory SQL server, mounts the dataset, and runs relational analytical queries.
* **`Project-3-SQL-Report.pdf`**: The formal executive submission report compiling our exact database results and analytical conclusions.

---

## ⚙️ How the Relational Pipeline Works
When you execute the Python script, it performs the following lifecycle tasks automatically:
1.  **Engine Initialization**: Spins up an in-memory `sqlite3` database engine server instantly.
2.  **Schema Generation**: Reads the clean `.csv` rows and ports them directly into a formal SQL table named `transactions`.
3.  **Relational Querying**: Dispatches standard relational SQL syntax queries down to the engine.
4.  **Terminal Viewport**: Renders structured, tabular business analytics frames instantly into your terminal.

---

## 📊 Executed SQL Core Milestones

### Task 1: The Funnel (`WHERE` Clause)
* **Objective**: Filters rows based on a categorical string match combined with numeric thresholds.
* **Business Target**: Isolates bulk-order patterns for high-ticket home office items (`Product = 'Chair'` where `Quantity >= 3`).

### Task 2: The Bucket & Aggregate (`GROUP BY`)
* **Objective**: Group individual transactions into macro product performance categories.
* **Calculated Metrics**: Evaluates performance matrix benchmarks using structural mathematical functions: `COUNT(OrderID)`, `SUM(Quantity)`, `AVG(UnitPrice)`, and `SUM(TotalPrice)`.

### Task 3: Pattern & Search (`LIKE` Wildcards)
* **Objective**: Runs string pattern matching to identify broad trends across product substrings.
* **Business Target**: Tracks combined tech hardware behaviors (`Product LIKE 'Phone%'` or `'%Laptop%'`).

### Task 4: Advanced High-Value Slicing (`HAVING` Clause)
* **Objective**: Filters aggregated grouped buckets that cross over a specific global value threshold.
* **Business Target**: Uncovers elite category revenue vectors generating over `$160,000` in gross revenue.

---

## 🚀 Execution Instructions

### 1. Prerequisites
Ensure you have Python 3 and the required data dependencies installed in your workspace terminal:
```bash
pip install pandas
