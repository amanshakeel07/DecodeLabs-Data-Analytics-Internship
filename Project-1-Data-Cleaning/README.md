# Project 1: Data Cleaning, Preparation, and Integrity Audit

## 📌 Project Overview
This project serves as the foundational phase of the DecodeLabs Data Analytics Track, focusing entirely on Data Integrity and Quality Assurance. The primary objective was to engineer a robust data-cleaning pipeline to transform a raw, unstructured transactional dataset containing 1,200 noisy records into a production-ready, "Gold Standard" source of truth.

---

## 🛠️ Technical Implementation & Methodology
Rather than employing destructive data deletions that compromise statistical validity, precise algorithmic parameters were executed via Python's `pandas` library:

* **Strategic Imputation:** Successfully resolved 309 missing values in marketing logs (`CouponCode`) using categorical mode imputation (`FREESHIP`), preserving full statistical volume.
* **Integrity Audit:** Implemented a deduplication algorithm tracking primary keys (`OrderID`) to drop conflicting duplicate records and enforce an absolute 0% structural error rate.
* **Language Standardization:** 
  * Coerced erratic timeline vectors into uniform global **ISO 8601 (`YYYY-MM-DD`) format**.
  * Applied string trimming functions to strip leading/trailing whitespace and mapped variables to title case.
  * Imposed `float64` currency rounding rules to enforce standard two-decimal constraints across monetary fields (`UnitPrice`, `TotalPrice`).

---

## 📈 Core Business Insights (EDA Baseline)
With data integrity securely verified at a 100% success threshold, preliminary exploratory data analysis yielded immediate operational intelligence:

### A. Product Portfolio Performance
* **Top Revenue Drivers:** **Chairs** ($195,620.11 across 562 units) and **Printers** ($195,612.61 across 542 units) represent the core financial engines.
* **Underperformer:** **Phones** lag significantly behind in customer acquisition volume ($151,722.39 across 411 units).

### B. Marketing Channel Efficiency
* Acquisition metrics reveal that social media funnels via **Instagram** ($275,285.45 across 259 orders) and target audience nurturing via **Email** ($261,808.55 across 250 orders) deliver the most potent conversion pathways.

### C. Operational Supply Chain Health
* **Logistics Bottleneck:** Evaluated metrics highlight a major systemic risk—combined **Cancelled (20.83%)** and **Returned (20.58%)** order statuses account for over **41% of total transaction volume**. This strongly recommends an immediate structural audit of fulfillment workflows, delivery times, or product descriptions.

---

## 📁 Deliverables Checklist
* `Data Analytics Project 1.py`: The reproducible Python data wrangling pipeline.
* `Cleaned_Data_Project1.csv`: The verified, audited, clean data matrix.
* `Data Analytics Project 1 Report.pdf`: The complete, executive-ready engineering audit report.

---
**Intern Name:** Muhammad Aman Shakeel  
**Track:** Data Analytics (Batch 2026) | DecodeLabs Industrial Training Simulation
