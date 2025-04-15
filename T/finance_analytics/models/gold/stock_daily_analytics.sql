-- stock_daily_analytics.sql
select
    s.DATE,
    s.SYMBOL,
    s.COMPANY_NAME,
    f.INDUSTRY,
    f.SECTOR,
    s.OPEN,
    s.HIGH,
    s.LOW,
    s.CLOSE,
    s.VOLUME,
    round(s.CLOSE - s.OPEN, 2) as DAILY_CHANGE,
    round(((s.CLOSE - s.OPEN) / nullif(s.OPEN, 0)) * 100, 2) as DAILY_PERCENT_CHANGE,
    current_timestamp() as GENERATED_AT
FROM {{ ref('stock_prices_cleaned') }} s
{# from FINANCE_ANALYTICS.DBT_SILVER.stock_prices_cleaned s #}
join {{ ref('company_fundamentals_cleaned') }} f
{# join FINANCE_ANALYTICS.DBT_SILVER.company_fundamentals_cleaned f #}
    on s.SYMBOL = f.SYMBOL