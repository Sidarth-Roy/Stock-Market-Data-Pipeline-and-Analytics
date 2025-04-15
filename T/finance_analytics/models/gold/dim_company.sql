-- dim_company.sql
select distinct
    SYMBOL,
    COMPANY_NAME,
    INDUSTRY,
    SECTOR,
    CEO,
    EXCHANGE,
    WEBSITE,
    IPO_DATE
FROM {{ ref('company_fundamentals_cleaned') }}
{# from FINANCE_ANALYTICS.DBT_SILVER.company_fundamentals_cleaned #}