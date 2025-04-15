-- vw_company_performance_daily.sql
select
    f.DATE,
    f.SYMBOL,
    c.COMPANY_NAME,
    c.SECTOR,
    c.INDUSTRY,
    f.CLOSE,
    f.PRICE_PCT_CHANGE,
    ns.AVG_TITLE_SENTIMENT,
    case
        when ns.AVG_TITLE_SENTIMENT > 0.2 then 'POSITIVE'
        when ns.AVG_TITLE_SENTIMENT < -0.2 then 'NEGATIVE'
        else 'NEUTRAL'
    end as TITLE_SENTIMENT_CLASS,
    ns.AVG_DESC_SENTIMENT,
    case
        when ns.AVG_DESC_SENTIMENT > 0.2 then 'POSITIVE'
        when ns.AVG_DESC_SENTIMENT < -0.2 then 'NEGATIVE'
        else 'NEUTRAL'
    end as DESC_SENTIMENT_CLASS
from {{ ref('fact_stock_daily') }} f
{# from FINANCE_ANALYTICS.DBT_GOLD.fact_stock_daily f #}
join {{ ref('dim_company') }} c 
    on f.SYMBOL = c.SYMBOL
{# join FINANCE_ANALYTICS.DBT_GOLD.dim_company c on f.SYMBOL = c.SYMBOL #}
left join {{ ref('fact_news_sentiment') }} ns 
{# left join FINANCE_ANALYTICS.DBT_GOLD.fact_news_sentiment ns  #}
    on f.SYMBOL = ns.SYMBOL and f.DATE = ns.NEWS_DATE