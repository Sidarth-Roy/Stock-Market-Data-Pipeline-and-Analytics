-- models/bronze/stock_prices_bronze.sql
{{ config(materialized='view') }}

SELECT *,
    MD5(
            TO_VARCHAR(DATE) || UPPER(SYMBOL) || INITCAP(COMPANY_NAME) ||
            TO_VARCHAR(OPEN) || TO_VARCHAR(HIGH) || TO_VARCHAR(LOW) || TO_VARCHAR(CLOSE) || 
            TO_VARCHAR(VOLUME) || TO_VARCHAR(CREATED_AT) || TO_VARCHAR(UPDATED_AT) || TO_VARCHAR(ACTIVE)
        ) AS row_hash
FROM {{ source('bronze', 'stock_prices') }}
{# SELECT * FROM {{ ref('stock_prices') }} #}
