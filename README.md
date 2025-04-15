# 📊 Stock Market Data Pipeline and Analytics

A complete end-to-end **Data Engineering + Data Analytics** project that ingests stock market data, processes it using a modern data stack (Snowflake, dbt, Dagster), and visualizes insights using Power BI.

---

## 🚀 Overview

This project simulates a production-grade stock market data pipeline that integrates data extraction, transformation, orchestration, and reporting.

- 📥 **Ingestion**: Raw stock data from APIs is extracted and loaded into Snowflake.
- 🔄 **Transformation**: dbt models are used to clean, enrich, and structure data into analytics-ready tables.
- 📅 **Orchestration**: Dagster handles job scheduling and dependencies between ingestion and transformation tasks.
- 📊 **Analytics**: Power BI dashboards provide actionable insights on stock performance.

---

## 🧱 Tech Stack

| Layer            | Tools/Tech                                |
|------------------|--------------------------------------------|
| Ingestion        | Python, Requests, Pandas                   |
| Data Warehouse   | ❄️ Snowflake                                |
| Transformation   | dbt (Data Build Tool)                      |
| Orchestration    | Dagster                                    |
| Visualization    | Power BI                                   |
| Others           | Git, Virtualenv, SQL, Jinja                |

---

## 🗂️ Folder Structure

```
📁 Stock-Market-Data-Pipeline-and-Analytics/
├── EL/
│   └── ...               # Scripts for data extraction and loading into Snowflake
├── Reports/
│   └── ...               # Power BI reports and visualizations
├── SnowflakeScripts/
│   └── ...               # SQL DDL scripts for Snowflake schemas and tables
├── T/
│   └── finance_analytics/
│       └── ...           # dbt project with models, seeds, snapshots
├── orchestration/
│   ├── assets/           # Dagster Python assets for ingestion
│   ├── dbt_assets/       # Dagster-wrapped dbt assets
│   ├── jobs.py           # Dagster job definitions
│   ├── dbt_sensor.py     # Sensor to trigger dbt after ingestion
│   └── definitions.py    # Dagster Definitions, Schedules, Sensors
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

1. **Ingestion (EL/)**
   - Scripts fetch historical and live stock data using APIs.
   - Data is cleaned and loaded into Snowflake.

2. **Transformation (T/finance_analytics)**
   - dbt models transform raw data into analytics-ready datasets (e.g. `stg_`, `fct_`, and `dim_` models).
   - Supports incremental loading and modular SQL.

3. **Orchestration (Dagster)**
   - `data_ingestion_pipeline`: Fetches and loads raw data into Snowflake.
   - `dbt_transformation_job`: Executes dbt models post ingestion.
   - Schedule:
     - Ingestion at **12 AM**
     - Transformation at **2 AM**
   - Sensors ensure dependency management.

4. **Reporting (Reports/)**
   - Power BI dashboards visualize:
     - Daily stock performance
     - Volume and price trends
     - Technical indicators

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sidarth-Roy/Stock-Market-Data-Pipeline-and-Analytics.git
cd Stock-Market-Data-Pipeline-and-Analytics
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Snowflake & dbt

- Update `profiles.yml` and `dbt_project.yml` inside the `T/finance_analytics` directory.
- Ensure Snowflake credentials are securely set.

### 5. Run Dagster UI

```bash
dagster dev -f orchestration/definitions.py
```

---

## 📈 Power BI Insights

The dashboard provides:

- Historical price trends (Open, High, Low, Close)
- Volume spikes
- Sector-wise analysis
- Moving averages and volatility metrics

> Power BI reports are available in the `Reports/` folder.

---

## 📅 Schedule and Sensor Logic

- **Daily Ingestion**: `0 0 * * *`
- **dbt Transformation**: `0 2 * * *`
- **Sensor**: Triggers transformation only if ingestion succeeds

---

## 🧠 Learning Outcomes

- Hands-on experience with modern data stack
- Automated pipelines with Dagster
- dbt transformations and incremental models
- Building analytical reports using Power BI
- Real-world data engineering project structure

---

## 📌 Future Enhancements

- Add CI/CD pipeline for dbt
- Integrate Apache Kafka for streaming data
- Deploy Dagster on cloud (e.g., ECS or GCP Composer)
- Schedule alerts for anomalies in stock prices

---

## 🙋‍♂️ Author

**Sidarth Roy**  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/sidarth-roy-bb77571b8/)

---

## ⭐️ If you found this project helpful...

Give it a ⭐️ and share it with your network!
