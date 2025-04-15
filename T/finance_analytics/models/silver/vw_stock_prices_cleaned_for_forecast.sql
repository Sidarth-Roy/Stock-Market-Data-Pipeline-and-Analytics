{{ config(
    materialized='view',
    schema='silver',
    post_hook="
    use role ACCOUNTADMIN;
    use warehouse COMPUTE_WH;
    use database FINANCE_ANALYTICS;
    use schema DBT_SILVER;
    CALL FINANCE_ANALYTICS.DBT_SILVER.RUN_FORECAST_PROC();"
) }}

SELECT
    TO_TIMESTAMP_NTZ(DATE) AS DATE_v1,
    CLOSE,
    SYMBOL
FROM {{ ref('stock_prices_cleaned') }}
