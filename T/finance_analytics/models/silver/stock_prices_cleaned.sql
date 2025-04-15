{{ config(materialized='incremental', unique_key='row_hash') }}

SELECT
    DATE,
    UPPER(SYMBOL) AS SYMBOL,
    INITCAP(COMPANY_NAME) AS COMPANY_NAME,
    OPEN,
    HIGH,
    LOW,
    CLOSE,
    VOLUME,
    CAST(CREATED_AT AS TIMESTAMP_NTZ) AS CREATED_AT,
    CAST(UPDATED_AT AS TIMESTAMP_NTZ) AS UPDATED_AT,
    ACTIVE,
    row_hash
FROM {{ ref('vw_stock_prices') }}
WHERE ACTIVE = TRUE
