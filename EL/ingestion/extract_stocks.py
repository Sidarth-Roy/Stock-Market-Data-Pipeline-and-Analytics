# extract_stock_data.py

import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
import uuid
from ..utils.snowflake_connector import load_to_snowflake

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
base_url = os.getenv("ALPHA_VANTAGE_BASE_URL")

def extract_and_load_stocks(symbol: str, company_name: str, table_name: str, stage: str):

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(f"Error fetching data for {symbol}: {data}")

    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index").reset_index()
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    df["symbol"] = symbol
    df["company_name"] = company_name
    df["created_at"] = datetime.now()
    df["updated_at"] = datetime.now()
    df["active"] = True

    # Reorder columns
    df = df[[
        "date", "symbol", "company_name", "open", "high", "low", "close", "volume",
        "created_at", "updated_at", "active"
    ]]

    # Save to local CSV
    os.makedirs("tmp", exist_ok=True)
    local_file = f"tmp/{symbol.lower()}_{uuid.uuid4().hex[:8]}.csv"
    df.to_csv(local_file, index=False)

    # Load into Snowflake
    # load_to_snowflake(local_file, table_name, stage)
    return local_file, table_name, stage
