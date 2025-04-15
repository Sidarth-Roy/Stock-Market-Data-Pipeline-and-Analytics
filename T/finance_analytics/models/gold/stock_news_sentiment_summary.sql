-- stock_news_sentiment_summary.sql
select
    date(PUBLISHED_AT) as NEWS_DATE,
    SYMBOL,
    COMPANY_NAME,
    count(*) as ARTICLE_COUNT,
    round(avg(TITLE_SENTIMENT), 3) as AVG_TITLE_SENTIMENT,
    round(min(TITLE_SENTIMENT), 3) as MIN_TITLE_SENTIMENT,
    round(max(TITLE_SENTIMENT), 3) as MAX_TITLE_SENTIMENT,
    round(avg(DESC_SENTIMENT), 3) as AVG_DESC_SENTIMENT,
    round(min(DESC_SENTIMENT), 3) as MIN_DESC_SENTIMENT,
    round(max(DESC_SENTIMENT), 3) as MAX_DESC_SENTIMENT,
    current_timestamp() as GENERATED_AT
FROM {{ ref('stock_news_sentiment_cleaned') }}
{# from FINANCE_ANALYTICS.DBT_SILVER.stock_news_sentiment_cleaned #}
group by 1, 2, 3