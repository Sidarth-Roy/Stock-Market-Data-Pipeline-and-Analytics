-- models/gold/stock_price_forecast_summary.sql

SELECT
    SERIES::STRING AS SYMBOL,
    TS AS FORECAST_DATE,
    FORECAST,
    LOWER_BOUND,
    UPPER_BOUND
 {# FROM {{ source('bronze', 'economic_indicators') }} #}
FROM {{ source('DBT_SILVER', 'STOCK_PRICE_FORECAST') }}
WHERE SERIES IS NOT NULL