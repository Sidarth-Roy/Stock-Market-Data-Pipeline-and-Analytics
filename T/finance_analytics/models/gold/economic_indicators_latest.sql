-- economic_indicators_latest.sql
with latest_values as (
    select
        SERIES_ID,
        SERIES_NAME,
        DATE,
        VALUE,
        first_value(VALUE) ignore nulls over (
            partition by SERIES_ID order by DATE desc
        ) as LATEST_VALUE
    FROM {{ ref('economic_indicators_cleaned') }}
    {# from FINANCE_ANALYTICS.DBT_SILVER.economic_indicators_cleaned #}
)
select
    SERIES_ID,
    SERIES_NAME,
    max(DATE) as LATEST_DATE,
    max(LATEST_VALUE) as LATEST_VALUE,
    current_timestamp() as GENERATED_AT
from latest_values
group by SERIES_ID, SERIES_NAME