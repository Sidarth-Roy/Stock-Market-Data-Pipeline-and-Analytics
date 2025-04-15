# orchestration/dbt_sensor.py

from dagster import RunRequest, sensor # type: ignore
from orchestration.jobs import data_ingestion_pipeline
from orchestration.jobs import dbt_transformation_job

@sensor(job=dbt_transformation_job)
def run_dbt_after_ingestion(context):
    # Check for the latest run of the ingestion job
    for run in context.instance.get_runs(
        job_name="data_ingestion_pipeline", limit=1
    ):
        if run.status == "SUCCESS":
            yield RunRequest(run_key=None)
        return  # avoid repeated triggering
