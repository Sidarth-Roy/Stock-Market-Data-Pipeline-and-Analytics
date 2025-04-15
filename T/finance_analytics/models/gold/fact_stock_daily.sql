-- fact_stock_daily.sql
select
    s.DATE,
    s.SYMBOL,
    s.OPEN,
    s.HIGH,
    s.LOW,
    s.CLOSE,
    s.VOLUME,
    round(s.CLOSE - s.OPEN, 2) as PRICE_DIFF,
    round(((s.CLOSE - s.OPEN) / nullif(s.OPEN, 0)) * 100, 2) as PRICE_PCT_CHANGE
FROM {{ ref('stock_prices_cleaned') }} s
{# from FINANCE_ANALYTICS.DBT_SILVER.stock_prices_cleaned s #}