# File: ingestion/extract_economic_indicators.py

import requests
import pandas as pd
from datetime import datetime
import uuid
import os
from dotenv import load_dotenv
from ..utils.snowflake_connector import load_to_snowflake

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")
FRED_BASE_URL = os.getenv("FRED_BASE_URL")

def extract_and_load_economic_indicator(series_id: str, series_name: str, table_name: str = "ECONOMIC_INDICATORS", stage: str = "ECONOMIC_INDICATORS"):
    """Fetch and load FRED economic indicator into Snowflake."""
    try:
        url = FRED_BASE_URL
        params = {
            "series_id": series_id,
            "api_key": FRED_API_KEY,
            "file_type": "json"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        observations = response.json().get("observations", [])

        if not observations:
            raise Exception(f"No data returned for {series_id}")

        df = pd.DataFrame(observations)
        df["value"] = pd.to_numeric(df["value"].replace(".", 0.0), errors="coerce").fillna(0.0)
        df["series_id"] = series_id
        df["series_name"] = series_name
        df["created_at"] = datetime.now()
        df["updated_at"] = datetime.now()
        df["active"] = True

        df = df[["date", "value", "series_id", "series_name", "created_at", "updated_at", "active"]]
        df.columns = ["date", "value", "series_id", "series_name", "created_at", "updated_at", "active"]

        local_file = f"tmp/econ_{series_id.lower()}_{uuid.uuid4().hex[:8]}.csv"
        df.to_csv(local_file, index=False)

        # load_to_snowflake(local_file, table_name, stage)
        # print(f"✅ Loaded indicator: {series_id}")
        return local_file, table_name, stage

    except Exception as e:
        print(f"❌ Failed to load indicator {series_id}: {e}")
