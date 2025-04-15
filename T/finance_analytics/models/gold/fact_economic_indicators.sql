-- fact_economic_indicators.sql
select
    DATE,
    SERIES_ID,
    VALUE
FROM {{ ref('economic_indicators_cleaned') }}
{# from FINANCE_ANALYTICS.DBT_SILVER.economic_indicators_cleaned #}