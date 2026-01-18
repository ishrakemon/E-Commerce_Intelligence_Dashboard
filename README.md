# E-Commerce_Intelligence_Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

This project is a full-stack data engineering pipeline designed to track competitor pricing and inventory. It automates the extraction of 1,000+ products from a competitor website, cleans and normalizes the data, stores it in a relational database, and generates actionable business intelligence reports.

The goal was to answer: *"Do higher-rated products actually cost more?"* and *"Where are the underpriced 'hidden gems' in the market?"*

---

### Architecture & Tech Stack**

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Extraction** | `Requests`, `BeautifulSoup` | Automated scraper handling pagination (50 pages) and HTML parsing. |
| **Transformation** | `Pandas` | Data cleaning, currency conversion, and type casting. |
| **Storage** | `SQLite`, `SQLAlchemy` | Relational database modeling and persistent storage. |
| **Analysis** | `SQL` | Aggregation queries to calculate average market price and rating distributions. |
| **Visualization** | `Matplotlib`, `Power BI` | Static dashboards (Python) and interactive reporting (Power BI). |

---

### Project Structure**
```text
├── src/                    
│   ├── scraper.py          
│   ├── load_db.py          
│   └── visualization.py    
│
├── data/                   
│   ├── books_data.csv      # Raw scraped data
│   ├── competitor_data.db  # SQLite Database
│   └── powerbi_data.csv    # Processed data for Power BI
│
├── output/                 # Final Visuals
│   └── project_dashboard.png  
│
├── analyze.py              
├── export_for_bi.py        
├── hidden_gems_report.csv  # Generated List of Best Deals
└── README.md                         
