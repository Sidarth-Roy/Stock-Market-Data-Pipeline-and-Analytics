# orchestration/orchestration/dbt_assets.py

from dagster import AssetExecutionContext # type: ignore
from dagster_dbt import dbt_assets, DbtCliResource # type: ignore
from pathlib import Path

DBT_PROJECT_DIR = Path("../../T/finance_analytics")
# DBT_PROFILES_DIR = DBT_PROJECT_DIR / "config"

@dbt_assets(manifest=DBT_PROJECT_DIR / "target" / "manifest.json")
def finance_analytics_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
