# ingestion/extract_news_sentiment.py

import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from ..utils.snowflake_connector import load_to_snowflake
import uuid

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Use a free source like NewsData.io or NewsAPI
NEWS_API_URL = os.getenv("NEWS_BASE_URL") 

def extract_and_load_news_sentiment(symbol: str, company_name: str, table_name: str, stage: str):
    try:
        params = {
            "q": company_name,
            "apiKey": NEWS_API_KEY,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 100,
        }

        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])

        if not articles:
            print(f"No news articles found for {company_name}")
            return

        df = pd.DataFrame(articles)
        df["symbol"] = symbol
        df["company_name"] = company_name
        df["fetched_at"] = datetime.now()

        df = df[["publishedAt", "title", "description", "url", "source", "symbol", "company_name", "fetched_at"]]
        df["source"] = df["source"].apply(lambda s: s["name"] if isinstance(s, dict) else s)

        local_file = f"tmp/news_{symbol.lower()}_{uuid.uuid4().hex[:8]}.csv"
        df.to_csv(local_file, index=False)

        # load_to_snowflake(local_file, table_name, stage)
        return local_file, table_name, stage

    except Exception as e:
        print(f"❌ Error fetching news for {symbol}: {e}")
