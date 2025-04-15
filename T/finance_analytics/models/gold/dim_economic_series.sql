-- dim_economic_series.sql
select distinct
    SERIES_ID,
    SERIES_NAME
FROM {{ ref('economic_indicators_cleaned') }}
{# from FINANCE_ANALYTICS.DBT_SILVER.economic_indicators_cleaned #}