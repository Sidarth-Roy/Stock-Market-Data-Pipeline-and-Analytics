-- models/bronze/stock_news_sentiment_bronze.sql
{{ config(materialized='view') }}

SELECT *,
    MD5(
            TO_VARCHAR(PUBLISHEDAT) || INITCAP(TITLE) || DESCRIPTION || URL || SOURCE ||
            UPPER(SYMBOL) || INITCAP(COMPANY_NAME) || TO_VARCHAR(FETCHED_AT)
        ) AS row_hash
 FROM {{ source('bronze', 'stock_news_sentiment') }}
{# SELECT * FROM {{ ref('stock_news_sentiment') }} #}
