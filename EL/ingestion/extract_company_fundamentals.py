# File: extract_fundamentals.py

import requests
import pandas as pd
from datetime import datetime
import uuid
import os
from dotenv import load_dotenv
from ..utils.snowflake_connector import load_to_snowflake

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
FMP_BASE_URL = os.getenv("FMP_BASE_URL")


def extract_and_load_company_fundamentals(symbol: str, table_name: str, stage: str):
    url = f"{FMP_BASE_URL}/profile/{symbol}?apikey={FMP_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if not data or not isinstance(data, list):
        raise Exception(f"No data returned for {symbol} from FMP API")

    profile = data[0]
    df = pd.DataFrame([{
        "symbol": profile.get("symbol"),
        "company_name": profile.get("companyName"),
        "industry": profile.get("industry"),
        "sector": profile.get("sector"),
        "ceo": profile.get("ceo"),
        "exchange": profile.get("exchange"),
        "website": profile.get("website"),
        "description": profile.get("description"),
        "price": profile.get("price"),
        "beta": profile.get("beta"),
        "vol_avg": profile.get("volAvg"),
        "mkt_cap": profile.get("mktCap"),
        "last_div": profile.get("lastDiv"),
        "range": profile.get("range"),
        "ipo_date": profile.get("ipoDate"),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "active": True
    }])

    local_file = f"tmp/fundamentals_{symbol.lower()}_{uuid.uuid4().hex[:8]}.csv"
    df.to_csv(local_file, index=False)

    # load_to_snowflake(local_file, table_name, stage)
    return local_file, table_name, stage
