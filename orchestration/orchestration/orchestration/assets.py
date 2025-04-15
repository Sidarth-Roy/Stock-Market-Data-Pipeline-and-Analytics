# orchestration/assets.py
import subprocess
from dagster import asset, op # type: ignore
import json
from pathlib import Path

from EL.ingestion.extract_stocks import extract_and_load_stocks
from EL.ingestion.extract_company_fundamentals import extract_and_load_company_fundamentals
from EL.ingestion.extract_news_sentiment import extract_and_load_news_sentiment
from EL.ingestion.extract_economic_indicators import extract_and_load_economic_indicator
from EL.utils.snowflake_connector import load_to_snowflake

STOCKS_FILE = Path("../../EL/stock_symbols.json")
ECONOMIC_INDICATORS_FILE = Path("../../EL/economic_indicator.json")


# ⬇️ Shared config assets

@asset
def stock_symbols():
    with open(STOCKS_FILE, "r") as file:
        return json.load(file)


@asset
def economic_indicators():
    with open(ECONOMIC_INDICATORS_FILE, "r") as file:
        return json.load(file)


# ⬇️ Modular data ingestion assets

@asset
def extract_stock_prices(stock_symbols):
    results = []
    for stock in stock_symbols:
        symbol = stock["SYMBOL"]
        company_name = stock["COMPANY"]
        
        try:
            print(f"\n📊 Fetching Stock Proces: {symbol} : {company_name} ...")

            local_file, table_name, stage = extract_and_load_stocks(symbol=symbol, company_name=company_name, table_name="STOCK_PRICES2", stage="STOCKS")
            print(f"✅ Extracted stock price data for {symbol}")
            
        # try:
        #     load_to_snowflake(local_file, table_name, stage)
        #     print(f"✅ Loaded file: {local_file} into {table_name} at {stage}")
        # except Exception as e:
        #     print(f"❌ Failed to load file {local_file} into {table_name}: {e}")
            results.append((local_file, table_name, stage))

        except Exception as e:
            print(f"❌ Failed to load stock price data for {symbol}: {e}")
    return results

@asset
def extract_company_fundamentals(stock_symbols):
    results = []
    for stock in stock_symbols:
        symbol = stock["SYMBOL"]
        company_name = stock["COMPANY"]

        try:
            print(f"\n📊 Fetching Company Fundamentals: {symbol} : {company_name} ...")

            local_file, table_name, stage = extract_and_load_company_fundamentals(symbol=symbol, table_name="COMPANY_FUNDAMENTALS2", stage="COMPANY_FUNDAMENTALS")
            print(f"✅ Extracted company fundamentals for {symbol}")
            
        # try:
        #     load_to_snowflake(local_file, table_name, stage)
        #     print(f"✅ Loaded file: {local_file} into {table_name} at {stage}")
        # except Exception as e:
        #     print(f"❌ Failed to load file {local_file} into {table_name}: {e}")
            results.append((local_file, table_name, stage))

        except Exception as e:
            print(f"❌ Failed to load fundamentals for {symbol}: {e}")
    return results

@asset
def extract_news_sentiment(stock_symbols):
    results = []
    for stock in stock_symbols:
        symbol = stock["SYMBOL"]
        company_name = stock["COMPANY"]

        try:
            print(f"\n📊 Fetching news/sentiment: {symbol} : {company_name} ...")

            local_file, table_name, stage = extract_and_load_news_sentiment(symbol=symbol, company_name=company_name, table_name="STOCK_NEWS_SENTIMENT2", stage="STOCK_NEWS_SENTIMENT")
            print(f"✅ Extracted news/sentiment for {symbol}")
            
        # try:
        #     load_to_snowflake(local_file, table_name, stage)
        #     print(f"✅ Loaded file: {local_file} into {table_name} at {stage}")
        # except Exception as e:
        #     print(f"❌ Failed to load file {local_file} into {table_name}: {e}")
            results.append((local_file, table_name, stage))
            
        except Exception as e:
            print(f"❌ Failed to load news/sentiment for {symbol}: {e}")
    return results

@asset
def extract_economic_indicators(economic_indicators):
    results = []
    for indicator in economic_indicators:

        try:
            print(f"\n📊 Fetching Economic Indicator: {indicator['name']} ({indicator['series_id']})...")

            local_file, table_name, stage = extract_and_load_economic_indicator(series_id=indicator["series_id"], series_name=indicator["name"], table_name= "ECONOMIC_INDICATORS2", stage= "ECONOMIC_INDICATORS")
            print(f"✅ Extracted economic indicator: {indicator['series_id']}")

        # try:
        #     load_to_snowflake(local_file, table_name, stage)
        #     print(f"✅ Loaded file: {local_file} into {table_name} at {stage}")
        # except Exception as e:
        #     print(f"❌ Failed to load file {local_file} into {table_name}: {e}")
            results.append((local_file, table_name, stage))

        except Exception as e:
            print(f"❌ Failed to load indicator {indicator['series_id']}: {e}")
    return results

@asset
def load_data( extract_stock_prices, extract_company_fundamentals, extract_news_sentiment, extract_economic_indicators):
    # Concatenate results from all assets correctly
    all_results = []

    # Unwrap and combine all the results from the extraction assets
    all_results.extend(extract_stock_prices)  # List of tuples from extract_stock_prices
    all_results.extend(extract_company_fundamentals)  # List of tuples from extract_company_fundamentals
    all_results.extend(extract_news_sentiment)  # List of tuples from extract_news_sentiment
    all_results.extend(extract_economic_indicators)  # List of tuples from extract_economic_indicators

    for local_file, table_name, stage in all_results:
        try:
            load_to_snowflake(local_file, table_name, stage)
            print(f"✅ Loaded file: {local_file} into {table_name} at {stage}")
        except Exception as e:
            print(f"❌ Failed to load file {local_file} into {table_name}: {e}")


