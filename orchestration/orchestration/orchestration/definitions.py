# orchestration/definitions.py
from dagster import Definitions, load_assets_from_modules, ScheduleDefinition # type: ignore
from dagster_dbt import DbtCliResource # type: ignore
from orchestration import assets  # noqa: TID252
from orchestration.jobs import data_ingestion_pipeline,dbt_transformation_job  # Import your job from jobs.py
from orchestration.dbt_assets import finance_analytics_assets
from orchestration.dbt_sensor import run_dbt_after_ingestion
from pathlib import Path
DBT_PROJECT_DIR = Path("../../T/finance_analytics")
# DBT_PROFILES_DIR = DBT_PROJECT_DIR / "config"

# Define the schedule to run the job every 24 hours (midnight)
daily_data_ingestion_schedule = ScheduleDefinition(
    job=data_ingestion_pipeline,  # Your job to run
    cron_schedule="0 0 * * *",  # This runs every day at midnight
    name="daily_data_ingestion_schedule",  # Optional: Name for your schedule
)

# Schedule: DBT Transformation at 2:00 AM
daily_dbt_transformation_schedule = ScheduleDefinition(
    job=dbt_transformation_job,
    cron_schedule="0 2 * * *",
    name="daily_dbt_transformation_schedule",
)

# Load all assets from your modules (if applicable)
all_assets = load_assets_from_modules([assets]) + [finance_analytics_assets]

# Define your Dagster definitions (includes job and schedules)
defs = Definitions(
    assets= all_assets,
    jobs=[data_ingestion_pipeline, dbt_transformation_job],  # Add the job to the Definitions
    schedules=[daily_data_ingestion_schedule, daily_dbt_transformation_schedule],  # Add the schedule to the definitions
    resources={
        "dbt": DbtCliResource(
            project_dir=str(DBT_PROJECT_DIR),
            # profiles_dir=str(DBT_PROFILES_DIR),
        )
    },
    sensors=[  # 👈 Add the sensor here
        run_dbt_after_ingestion
    ]
)