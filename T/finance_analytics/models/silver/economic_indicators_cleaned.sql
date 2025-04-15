{{ config(materialized='incremental', unique_key='row_hash') }}

SELECT
    DATE,
    TRY_CAST(VALUE AS FLOAT) AS VALUE,
    SERIES_ID,
    INITCAP(SERIES_NAME) AS SERIES_NAME,
    CAST(CREATED_AT AS TIMESTAMP_NTZ) AS CREATED_AT,
    CAST(UPDATED_AT AS TIMESTAMP_NTZ) AS UPDATED_AT,
    row_hash
FROM {{ ref('vw_economic_indicators') }}
WHERE ACTIVE = TRUE
