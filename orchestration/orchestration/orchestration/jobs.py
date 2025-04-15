from dagster import job,define_asset_job # type: ignore
from orchestration.assets import (
    stock_symbols,
    economic_indicators,
    extract_stock_prices,
    extract_company_fundamentals,
    extract_news_sentiment,
    extract_economic_indicators,
    load_data
)


dbt_transformation_job = define_asset_job(
    name="dbt_transformation_job",
    selection="*"  # Or filter using asset key prefixes like "stg_", "fact_", etc.
)

@job
def data_ingestion_pipeline():
    # EL assets
    stock_symbols_data = stock_symbols()
    economic_indicators_data = economic_indicators()
    stock_prices = extract_stock_prices(stock_symbols_data)
    company_fundamentals = extract_company_fundamentals(stock_symbols_data)
    news_sentiment = extract_news_sentiment(stock_symbols_data)
    extracted_economic_indicators_data = extract_economic_indicators(economic_indicators_data)
    load_output = load_data(stock_prices, company_fundamentals, news_sentiment, extracted_economic_indicators_data)

