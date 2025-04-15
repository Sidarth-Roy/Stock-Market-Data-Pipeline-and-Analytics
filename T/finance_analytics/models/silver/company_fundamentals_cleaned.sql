{{ config(materialized='incremental', unique_key='SYMBOL') }}

SELECT
    SYMBOL,
    COMPANY_NAME,
    INDUSTRY,
    SECTOR,
    CEO,
    EXCHANGE,
    WEBSITE,
    DESCRIPTION,
    PRICE,
    BETA,
    VOL_AVG,
    MKT_CAP,
    LAST_DIV,
    RANGE,
    IPO_DATE,
    CAST(CREATED_AT AS TIMESTAMP_NTZ) AS CREATED_AT,
    CAST(UPDATED_AT AS TIMESTAMP_NTZ) AS UPDATED_AT,
    ACTIVE
FROM {{ ref('vw_company_fundamentals') }}
WHERE ACTIVE = TRUE
