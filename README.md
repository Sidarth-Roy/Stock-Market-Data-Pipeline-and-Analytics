# 📊 Stock Market Data Pipeline and Analytics

A complete end-to-end Data Engineering and Analytics project that collects, transforms, models, and visualizes stock market-related data using modern tools like **Snowflake**, **Python**, **dbt**, **Dagster**, and **Power BI**.  

---

## 🚀 Features

- Ingests data from multiple APIs (stock prices, news sentiment, company fundamentals, economic indicators).
- Implements ELT architecture in Snowflake using Bronze → Silver → Gold data layering.
- Uses **dbt** for data modeling and transformation.
- Automates workflows using **Dagster** with sensors and scheduling.
- Forecasts stock prices using **Snowflake Cortex ML** (stored procedures).
- Visualizes insights using **Power BI** dashboards.

---

## 🗂️ Project Structure

```
📦 Stock-Market-Data-Pipeline-and-Analytics/
├── orchestration/             # Dagster jobs, schedules, sensors
├── dbt/                       # dbt project for modeling
│   ├── models/
│   └── seeds/
├── notebooks/                 # Exploratory data analysis notebooks
├── pipelines/                # Python scripts for data ingestion
├── utils/                    # Helper scripts and configurations
├── assets/                   # Images, architecture diagram
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧱 Data Flow Architecture

The pipeline follows a layered data architecture in Snowflake and utilizes automation, transformation, and forecasting as shown below:

### 📌 Architecture Diagram

![Architecture](https://github.com/Sidarth-Roy/Stock-Market-Data-Pipeline-and-Analytics/blob/main/assets/architecture.png)

---

## 📥 Data Sources

| Source | Description |
|--------|-------------|
| Alpha Vantage API | Stock prices and company fundamentals |
| Financial Modeling Prep | Economic indicators |
| NewsCatcher API | News sentiment data |

---

## 🧠 Forecasting

Utilizes **Snowflake Cortex**'s pre-built ML forecasting models with stored procedures to forecast future stock prices based on historical data.

---

## ⚙️ Tools & Technologies

- **Snowflake** (Data Warehouse, Cortex Forecasting)
- **Python** (Ingestion, Automation)
- **dbt** (Transformations and Modeling)
- **Dagster** (Orchestration and Scheduling)
- **Power BI** (Data Visualization)

---

## 📈 Dashboards

Final gold-layer datasets are connected to Power BI to generate interactive, insightful dashboards for:

- Stock performance trends
- Company-level KPIs
- Economic sentiment impact
- Price forecasts with confidence intervals

---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Sidarth-Roy/Stock-Market-Data-Pipeline-and-Analytics.git
cd Stock-Market-Data-Pipeline-and-Analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Ensure you configure environment variables and Snowflake credentials before running.

---

## 📅 Orchestration Flow

- Dagster sensors trigger **dbt models** after ingestion.
- Scheduled jobs for daily ingestion and 2 AM dbt transformations.
- ML forecasts generated daily and saved to the Gold layer.

---

## 🤝 Contributing

Feel free to fork and contribute with pull requests, bug fixes, or new ideas!

---

## 📬 Contact

**Sidarth Roy**  
📧 [LinkedIn](https://www.linkedin.com/in/sidarth-roy-bb77571b8/)  
🌐 [GitHub](https://github.com/Sidarth-Roy)
