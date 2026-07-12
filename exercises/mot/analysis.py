import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import duckdb
    import pandas as pd
    from pathlib import Path

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # MOT Cymru: Production Engineering

    You are picking up ownership of the MOT Cymru analysis pipeline from a previous
    engineer. The data is loaded and ready. Your job is to build on top of it.

    Work through the three tasks below. You do not need to finish every sub-question —
    **depth and reasoning matter more than coverage**. As you work, talk through what
    you are doing, what you are choosing not to do, and anything in the data that
    concerns you.

    > Stack: Python 3.13 · DuckDB · pandas · marimo
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Setup — Data is ready below, run this cell first
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        create table raw_mot 
        as
        select * from read_csv('data/mot_results.csv');

        create table raw_stations
        as
        select * from read_csv('data/testing_stations.csv');

        create table raw_inspections
        as
        select * from read_csv('data/station_inspections.csv');

        create table raw_profiles
        as
        select * from read_csv('data/vehicle_profiles.csv');
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Warmup task

    You have seen at the earlier stage the data. One obvious table is missing - regions.

    Create `silver_stations` table and a `regions` dimension table by taking the last word from the stations' address
    """)
    return


@app.cell
def _(mo, raw_stations):
    _df = mo.sql(
        f"""
        create or replace view silver_stations
        as
          select * 
        	, null as region 
          from raw_stations;

        create or replace view dim_regions
        as
        ...
        """
    )
    return


@app.cell
def _(mo, silver_stations):
    _df = mo.sql(
        f"""
        select * from silver_stations 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Task 1 — Regional Failure Rate Trends

    The transport analytics team wants to understand how MOT failure rates vary
    across Welsh regions and whether they are getting better or worse over time.

    Using the `mot_results` table:

    **1a.** Calculate the overall failure rate per region (across all years combined),
    ordered from highest to lowest.

    **1b.** Extend the query to show failure rate **per region per year**, and add a
    column with the **year-on-year change** in failure rate for each region.

    **1c.** Identify regions that are **statistical outliers**. Quantify how unusual
    each region is — not just that it looks different.

    Call out anything in the data that concerns you as you go.
    Think carefully about which columns belong in an analyst-facing output
    and which do not.
    """)
    return


@app.cell
def _(mo, raw_stations):
    # Task 1 — your SQL goes here.
    _df = mo.sql(
        f"""
        -- task 1 — your SQL goes here.
        select * 
        from raw_mot
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Task 2 — Station Risk Profile

    The compliance team needs a single table that brings together each testing
    station with its most recent inspection outcome and the failure rate of its region.

    Using `stations`, `inspections`, and your results from Task 1:

    **2a.** For each station, find its **most recent** inspection date and result.
    Stations that have never been inspected must still appear in the output.

    **2b.** Join with regional failure rates from Task 1 to produce a station risk
    profile.

    **2c.** Add a column that flags stations you consider high-risk, and explain
    your criteria.
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        -- Task 2 — your SQL goes here.
        select 'implement here'
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Task 3 — Production Output

    The data science team runs a nightly job that calls this notebook and expects
    the station risk profile to be written to `data/station_risk.parquet`.

    The job may run more than once on the same day (reruns after failures are common).
    **Running it twice on the same day must not corrupt the output or log duplicate runs.**

    **3a.** Write the station risk profile to `data/station_risk.parquet`.

    **3b.** Create a `pipeline_runs` table in DuckDB that records each run:
    at minimum — a timestamp, record count, and whether the output was written or skipped.

    **3c.** Make the export idempotent: if a successful run has already completed
    today, skip writing the file and record the skip in the log instead.
    """)
    return


@app.cell
def _(con):
    # Task 3 — skeleton to get you started.
    # The log table structure is yours to define.

    con.execute("""
        CREATE TABLE IF NOT EXISTS pipeline_runs (
            run_id        INTEGER PRIMARY KEY,
            run_timestamp TIMESTAMP,
            records_written INTEGER,
            status        VARCHAR,   -- 'written' | 'skipped'
        )
    """)

    # Your idempotent export logic here
    pass
    return


if __name__ == "__main__":
    app.run()
