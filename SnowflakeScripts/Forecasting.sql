-- This is your Cortex Project.
-----------------------------------------------------------
-- SETUP
-----------------------------------------------------------
use role ACCOUNTADMIN;
use warehouse COMPUTE_WH;
use database FINANCE_ANALYTICS;
use schema SILVER;

-- Prepare your training data. Timestamp_ntz is a required format. Also, only include select columns.
CREATE VIEW STOCK_PRICES_CLEANED_FOR_FORECAST AS SELECT
    to_timestamp_ntz(DATE) as DATE_v1,
    CLOSE,
    SYMBOL
FROM STOCK_PRICES_CLEANED;



-----------------------------------------------------------
-- CREATE PREDICTIONS
-----------------------------------------------------------
-- Create your model.
CREATE SNOWFLAKE.ML.FORECAST STOCK_PRICE_FORECAST(
    INPUT_DATA => SYSTEM$REFERENCE('VIEW', 'STOCK_PRICES_CLEANED_FOR_FORECAST'),
    SERIES_COLNAME => 'SYMBOL',
    TIMESTAMP_COLNAME => 'DATE_v1',
    TARGET_COLNAME => 'CLOSE',
    CONFIG_OBJECT => { 'ON_ERROR': 'SKIP' }
);

-- Generate predictions and store the results to a table.
BEGIN
    -- This is the step that creates your predictions.
    CALL STOCK_PRICE_FORECAST!FORECAST(
        FORECASTING_PERIODS => 7,
        -- Here we set your prediction interval.
        CONFIG_OBJECT => {'prediction_interval': 0.95}
    );
    -- These steps store your predictions to a table.
    LET x := SQLID;
    CREATE TABLE STOCK_PRICE_FORECAST_MODEL AS SELECT * FROM TABLE(RESULT_SCAN(:x));
END;

-- View your predictions.
SELECT * FROM STOCK_PRICE_FORECAST_MODEL;

-- Union your predictions with your historical data, then view the results in a chart.
SELECT SYMBOL, DATE, CLOSE AS actual, NULL AS forecast, NULL AS lower_bound, NULL AS upper_bound
    FROM STOCK_PRICES_CLEANED
UNION ALL
SELECT replace(series, '"', '') as SYMBOL, ts as DATE, NULL AS actual, forecast, lower_bound, upper_bound
    FROM STOCK_PRICE_FORECAST_MODEL;

-----------------------------------------------------------
-- INSPECT RESULTS
-----------------------------------------------------------

-- Inspect the accuracy metrics of your model. 
CALL STOCK_PRICE_FORECAST!SHOW_EVALUATION_METRICS();

-- Inspect the relative importance of your features, including auto-generated features. 
CALL STOCK_PRICE_FORECAST!EXPLAIN_FEATURE_IMPORTANCE();
