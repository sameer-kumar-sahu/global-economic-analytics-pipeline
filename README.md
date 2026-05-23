# Global Economic Analytics Pipeline

## Overview

An end-to-end ETL and analytics pipeline that extracts global economic indicators from the World Bank API, transforms and stores data in MySQL, applies machine learning forecasting models, and visualizes insights through interactive Power BI dashboards.

---

## Project Objectives

- Build a scalable ETL pipeline
- Perform economic trend analysis
- Implement dimensional modeling using a star schema
- Apply machine learning forecasting
- Create interactive business intelligence dashboards
- Demonstrate SQL analytics and reporting workflows

---

## Tech Stack

| Layer | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Database | MySQL |
| ORM(Object-Relational Mapping) | SQLAlchemy |
| BI & Visualization | Power BI |
| Machine Learning | Scikit-learn |
| Version Control | Git + GitHub |
| CI/CD | GitHub Actions |

---

## Pipeline Architecture

```text
World Bank API
        ↓
Extract Layer
        ↓
Transformation Layer
        ↓
Forecasting Layer
        ↓
MySQL Database
        ↓
Star Schema Modeling
        ↓
Power BI Dashboard
```

---

## Features

- Automated ETL pipeline using Python
- Multi-country economic data extraction
- GDP, Inflation, and Population analysis
- Star schema dimensional modeling
- SQL analytics and reporting queries
- Machine learning forecasting
- Interactive Power BI dashboard
- Row-Level Security (RLS)
- GitHub Actions CI workflow

---

## Database Design

### Dimension Tables

- dim_country
- dim_indicator

### Fact Tables

- fact_economic_data

### Additional Tables

- economic_data
- economic_forecast

---

## Machine Learning

Implemented Linear Regression forecasting for:

- GDP prediction
- Population forecasting

---

## Power BI Dashboard

### Dashboard Features

- KPI Cards
- Economic trend analysis
- Forecast insights
- Dynamic slicers
- Country comparison
- Row-Level Security (RLS)

---

## SQL Analytics


Implemented advanced SQL queries, including

- Window functions
- Ranking analysis
- Forecast comparison
- Aggregate reporting
- Star schema joins
- CTE-based analytics

---

## Screenshots

### Dashboard Overview

(Add image here)

### SQL Analytics

(Add image here)

### Star Schema

(Add image here)

---

## How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=economic_analytics
DB_USER=root
DB_PASSWORD=your_password
```

### 5. Run Pipeline

```bash
python Scripts/main.py
```

---

## Future Improvements

- Apache Airflow orchestration
- Cloud deployment
- Advanced forecasting models
- Incremental loading
- Docker containerization
