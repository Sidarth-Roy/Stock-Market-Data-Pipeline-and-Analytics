-- fact_news_sentiment.sql
select
    date(PUBLISHED_AT) as NEWS_DATE,
    SYMBOL,
    count(*) as ARTICLE_COUNT,
    avg(TITLE_SENTIMENT) as AVG_TITLE_SENTIMENT,
    stddev(TITLE_SENTIMENT) as TITLE_SENTIMENT_VOLATILITY,
    avg(DESC_SENTIMENT) as AVG_DESC_SENTIMENT,
    stddev(DESC_SENTIMENT) as DESC_SENTIMENT_VOLATILITY
FROM {{ ref('stock_news_sentiment_cleaned') }}
{# from FINANCE_ANALYTICS.DBT_SILVER.stock_news_sentiment_cleaned #}
group by 1, 2