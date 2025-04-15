# main.py

import json
from .ingestion.extract_stocks  import extract_and_load_stocks
from .ingestion.extract_company_fundamentals import extract_and_load_company_fundamentals
from .ingestion.extract_economic_indicators import extract_and_load_economic_indicator
from .ingestion.extract_news_sentiment import extract_and_load_news_sentiment
from .utils.snowflake_connector import load_to_snowflake

STOCKS_FILE = "stock_symbols.json"
ECONOMIC_INDICATORS_FILE = "economic_indicator.json"

def main():
    # Load stock metadata
    with open(STOCKS_FILE, "r") as file:
        stocks = json.load(file)

    for stock in stocks:
        symbol = stock["SYMBOL"]
        company_name = stock["COMPANY"]

        print(f"\n🚀 Processing {symbol} - {company_name}...")

        try:
            print(f"\n📊 Fetching Stock Proces: {symbol} : {company_name} ...")

            local_file, table_name, stage = extract_and_load_stocks(symbol=symbol, company_name=company_name, table_name="STOCK_PRICES", stage="STOCKS")
            print(f"✅ Extracted stock price data for {symbol}")
            
            load_to_snowflake(local_file, table_name, stage)
            print(f"✅ Loaded stock price data for {symbol}")

        except Exception as e:
            print(f"❌ Failed to load stock price data for {symbol}: {e}")

        try:
            print(f"\n📊 Fetching Company Fundamentals: {symbol} : {company_name} ...")

            local_file, table_name, stage = extract_and_load_company_fundamentals(symbol=symbol, table_name="COMPANY_FUNDAMENTALS", stage="COMPANY_FUNDAMENTALS")
            print(f"✅ Extracted company fundamentals for {symbol}")
            
            load_to_snowflake(local_file, table_name, stage)
            print(f"✅ Loaded company fundamentals for {symbol}")

        except Exception as e:
            print(f"❌ Failed to load company fundamentals for {symbol}: {e}")
        
        try:
            print(f"\n📊 Fetching news/sentiment: {symbol} : {company_name} ...")

            local_file, table_name, stage = extract_and_load_news_sentiment(symbol=symbol, company_name=company_name, table_name="STOCK_NEWS_SENTIMENT", stage="STOCK_NEWS_SENTIMENT")
            print(f"✅ Extracted news/sentiment for {symbol}")
            
            load_to_snowflake(local_file, table_name, stage)
            print(f"✅ Loaded news/sentiment for {symbol}")

        except Exception as e:
            print(f"❌ Failed to load news/sentiment for {symbol}: {e}")

    # Fetch economic indicators from FRED
    with open(ECONOMIC_INDICATORS_FILE, "r") as file:
        ECONOMIC_INDICATORS = json.load(file)

    for indicator in ECONOMIC_INDICATORS:
        try:
            print(f"\n📊 Fetching Economic Indicator: {indicator['name']} ({indicator['series_id']})...")

            local_file, table_name, stage = extract_and_load_economic_indicator(series_id=indicator["series_id"], series_name=indicator["name"], table_name= "ECONOMIC_INDICATORS", stage= "ECONOMIC_INDICATORS")
            print(f"✅ Extracted economic indicator: {indicator['series_id']}")

            load_to_snowflake(local_file, table_name, stage)
            print(f"✅ Loaded economic indicator: {indicator['series_id']}")
            
        except Exception as e:
            print(f"❌ Failed to load indicator {indicator['series_id']}: {e}")

if __name__ == "__main__":
    main()
