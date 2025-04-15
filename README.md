# 📊 Stock Market Data Pipeline and Analytics

An end-to-end **Data Engineering and Analytics** project that simulates a real-world stock market analysis workflow. This project demonstrates how to automate data ingestion, transformation, orchestration, and dashboarding using modern tools like **Dagster**, **dbt**, and **Snowflake**.

---

## 🔍 Project Objective

To build a robust and scalable pipeline that:
- 📥 Ingests stock market data from Yahoo Finance
- 🛠️ Transforms raw data into analytics-ready models using `dbt`
- 🎯 Orchestrates workflows using `Dagster` (with scheduled and event-driven jobs)
- ❄️ Stores curated data in `Snowflake` warehouse
- 📈 Visualizes key insights using Power BI dashboards

This project is ideal for:
- 🚀 Showcasing data engineering & analytics skills
- 📚 Learning the modern data stack
- 📊 Creating analytical dashboards for stock market insights

---

## 🧱 Tech Stack

| Layer             | Toolset                            |
|------------------|-------------------------------------|
| Data Ingestion    | `pandas`, `Snowflake Connector`, `Dagster` |
| Data Transformation | `dbt Core`, `SQL`, `Jinja`       |
| Orchestration     | `Dagster` (jobs, sensors, schedules)|
| Data Warehouse    | `Snowflake`                        |
| Visualization     | `Power BI`, `Matplotlib`           |
| Dev Environment   | `venv`, `requirements.txt`, `Git`  |

---

## 🗂️ Folder Structure

```
📁 Stock-Market-Data-Pipeline-and-Analytics/
├── EL/
│   └── ...               # Scripts for data extraction and loading
├── Reports/
│   └── ...               # Power BI reports and visualizations
├── SnowflakeScripts/
│   └── ...               # SQL scripts for Snowflake schema and table creation
├── T/
│   └── finance_analytics/
│       └── ...           # dbt project: models, seeds, and configurations
├── orchestration/
│   ├── assets/
│   │   └── ...           # Python scripts for data ingestion
│   ├── dbt_assets/
│   │   └── ...           # dbt asset wrappers for Dagster
│   ├── jobs.py           # Dagster job definitions
│   ├── dbt_sensor.py     # Dagster sensor for triggering dbt
│   └── definitions.py    # Dagster schedules, jobs, and sensors
├── .gitignore
├── README.md
└── requirements.txt

```

---

## 🔄 Workflow Overview

1. **Ingestion**  
   - Stock symbols are defined and passed to the pipeline.
   - A Dagster job (`data_ingestion_pipeline`) uses Python and the Snowflake connector to:
     - Create necessary schemas and tables (if they don’t exist).
     - Pull historical data via Yahoo Finance’s API using `yfinance` or a Python script.
     - Process and load the data into Snowflake (raw zone).
   - Data includes: Open, Close, High, Low, Volume, and Date for each stock.

2. **Transformation**  
   - dbt models clean, join, and enhance the raw data into analytical layers (staging, marts).
   - Models calculate KPIs like moving averages, daily changes, and volatility scores.

3. **Orchestration**  
   - `Dagster` manages orchestration using:
     - ✅ A daily ingestion schedule at midnight
     - ✅ A scheduled dbt transformation job at 2 AM
     - ✅ A sensor that triggers dbt after successful ingestion

4. **Visualization**  
   - Final Snowflake tables are connected to Power BI.
   - Dashboards show price trends, comparisons, financial KPIs, and change analysis.

---

## 📊 Dashboard Preview

Power BI Dashboard includes:
- Stock price trends (daily, monthly)
- Moving averages (SMA, EMA)
- Volume analysis
- Price volatility and return analysis
- Company-wise comparisons

> *(See the `dashboards/` folder for Power BI file)*

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sidarth-Roy/Stock-Market-Data-Pipeline-and-Analytics.git
cd Stock-Market-Data-Pipeline-and-Analytics
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Snowflake & dbt

- Create a `.dbt/profiles.yml` file in your user directory.
- Add Snowflake connection details.
- Example config available [here](https://docs.getdbt.com/docs/core/connect-data-platform/snowflake).

### 5. Run Dagster UI

```bash
dagster dev
```

Visit `http://localhost:3000` to view and run pipelines.

### 6. Run dbt Models

```bash
cd dbt/finance_analytics
dbt build
```

---

## ✅ Key Features

- ✅ Automated stock data pipeline using modern DE tools
- ✅ dbt for structured, version-controlled transformations
- ✅ Dagster sensors and schedules for orchestration
- ✅ Clean, cloud-based warehouse with Snowflake
- ✅ Business-ready Power BI dashboards

---

## 🚀 Roadmap

- [ ] Stream real-time data (WebSocket or Kafka)
- [ ] Add data quality checks (dbt tests + Great Expectations)
- [ ] Deploy Power BI dashboard online
- [ ] Add ML-driven price prediction
- [ ] Build CI/CD workflow for data pipeline

---

## 👨‍💻 Author

**Sidarth Roy**  
💼 Data Engineer | Intern @ CG Infinity  
🌐 [LinkedIn](https://www.linkedin.com/in/sidarth-roy-bb77571b8)  
📂 [GitHub](https://github.com/Sidarth-Roy)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) for details.

---

> 💡 *“Automating insights from Wall Street to your screen — one pipeline at a time.”*
```

---

Let me know if you'd like:
- A visual pipeline diagram (I can generate one!)
- Help creating a `LICENSE`, `CONTRIBUTING.md`, or GitHub Actions CI/CD
- Turning this into a portfolio website or blog post!

You've built an awesome project — let's showcase it like one. 🚀
