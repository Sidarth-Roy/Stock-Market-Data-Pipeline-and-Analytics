-- stock_sentiment_kpi.sql
select
    s.DATE,
    s.SYMBOL,
    s.COMPANY_NAME,
    s.CLOSE as STOCK_CLOSE,
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
    end as DESC_SENTIMENT_CLASS,
    current_timestamp() as GENERATED_AT
{# from FINANCE_ANALYTICS.DBT_GOLD.stock_daily_analytics s #}
from {{ ref('stock_daily_analytics') }} s
{# left join FINANCE_ANALYTICS.DBT_GOLD.stock_news_sentiment_summary ns #}
left join {{ ref('stock_news_sentiment_summary') }} ns
    on s.SYMBOL = ns.SYMBOL and s.DATE = ns.NEWS_DATE