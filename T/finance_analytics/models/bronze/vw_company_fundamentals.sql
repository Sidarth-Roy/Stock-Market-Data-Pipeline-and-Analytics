-- models/bronze/company_fundamentals_bronze.sql
{{ config(materialized='view') }}

SELECT * FROM {{ source('bronze', 'company_fundamentals') }}
