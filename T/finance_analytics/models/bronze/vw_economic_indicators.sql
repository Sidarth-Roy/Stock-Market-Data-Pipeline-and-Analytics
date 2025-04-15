-- models/bronze/economic_indicators_bronze.sql
{{ config(materialized='view') }}

SELECT *,
    MD5(
        TO_VARCHAR(DATE) || TO_VARCHAR(VALUE) || SERIES_ID ||
        INITCAP(SERIES_NAME) || TO_VARCHAR(CREATED_AT) || TO_VARCHAR(UPDATED_AT)
    ) AS row_hash
 FROM {{ source('bronze', 'economic_indicators') }}
{# SELECT * FROM {{ ref('economic_indicators') }} #}
