# Global Economic Analytics Pipeline

## Overview

End-to-end ETL and analytics pipeline that extracts global economic indicators from the World Bank API, transforms and stores data in MySQL, applies forecasting models, and visualizes insights in Power BI.

---

## Features

- Automated ETL pipeline using Python
- Multi-country economic data extraction
- GDP, Inflation, and Population analytics
- MySQL database integration
- Star schema dimensional modeling
- Machine Learning forecasting
- Power BI interactive dashboard
- Scheduled automation
- GitHub Actions CI workflow

---

## Tech Stack

- Python
- Pandas
- MySQL
- SQLAlchemy
- Power BI
- Scikit-learn
- GitHub Actions

---

## Pipeline Architecture

API → Extract → Transform → Forecast → Load → MySQL → Power BI

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

- GDP
- Population

---

## How to Run

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

```bash
venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file with:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=economic_analytics
DB_USER=root
DB_PASSWORD=your_password
```

### 5. Run pipeline

```bash
python Scripts/main.py
```

---

## Future Improvements

- Airflow orchestration
- Cloud deployment
- Advanced forecasting models
- Incremental loading
- Docker containerization