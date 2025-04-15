-- sentiment_classification.sql
select
    *,
    case 
        when TITLE_SENTIMENT > 0.2 then 'POSITIVE'
        when TITLE_SENTIMENT < -0.2 then 'NEGATIVE'
        else 'NEUTRAL'
    end as TITLE_SENTIMENT_CLASS,
    case 
        when DESC_SENTIMENT > 0.2 then 'POSITIVE'
        when DESC_SENTIMENT < -0.2 then 'NEGATIVE'
        else 'NEUTRAL'
    end as DESC_SENTIMENT_CLASS
{# from FINANCE_ANALYTICS.DBT_SILVER.stock_news_sentiment_cleaned #}
FROM {{ ref('stock_news_sentiment_cleaned') }}