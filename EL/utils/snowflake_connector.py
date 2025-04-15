# utils/snowflake_connector.py

import snowflake.connector
import os
from dotenv import load_dotenv
import csv
load_dotenv()

def get_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        role=os.getenv("SNOWFLAKE_ROLE"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

def load_to_snowflake(local_file: str, table_name: str, stage_name: str):
    conn = get_connection()
    cursor = conn.cursor()
    stage_file = local_file.split("tmp/")[1]
    try:

        # Upload to internal stage
        put_stmt = f"PUT file://{local_file} @{stage_name} AUTO_COMPRESS=TRUE"
        cursor.execute(put_stmt)

        # Copy data into target table
        cursor.execute(f"""
        COPY INTO {table_name}
        FROM @{stage_name}/{stage_file}.gz
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='\"' SKIP_HEADER = 1)
        ;
        """)

        # Remove file from stage
        cursor.execute(f"REMOVE @{stage_name}/{stage_file}.gz")

        # Delete local file
        os.remove(local_file)

        print(f"✅ Data from {local_file} successfully loaded into {table_name}")

    except Exception as e:
        print(f"❌ Snowflake Load Error: {e}")

    finally:
        cursor.close()
        conn.close()
