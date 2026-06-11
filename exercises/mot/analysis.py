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

    return Path, duckdb, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # MOT Cymru — Data Pipeline

    This notebook implements a simple **bronze → silver → gold** pipeline
    for MOT test data across Wales.

    - **Bronze:** raw data loaded from CSV files
    - **Silver:** cleaned and standardised tables registered in DuckDB
    - **Gold:** analyst-ready views and exports

    The transport analytics team will consume the gold layer outputs.
    """)
    return


@app.cell
def _(Path):
    _data_files = sorted(f.name for f in Path("data").iterdir() if f.is_file())
    for _f in _data_files:
        print(_f)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bronze Layer — Raw Data Loading

    Load all source CSV files into DataFrames. These are the raw inputs
    before any cleaning or transformation.
    """)
    return


@app.cell
def _(Path, pd):
    _data_dir = Path("data")

    mot_results = pd.read_csv(_data_dir / "mot_results.csv")
    mot_results
    return (mot_results,)


@app.cell
def _(pd):
    stations = pd.read_csv("stations_sample.csv")
    stations
    return (stations,)


@app.cell
def _(pd):
    inspections = pd.DataFrame()
    try:
        inspections = pd.read_csv("data/StationInspections.csv")
    except:
        pass
    inspections
    return (inspections,)


@app.cell
def _(Path, pd):
    _data_dir = Path("data")

    profiles = pd.read_csv(_data_dir / "vehicle_profiles.csv")

    # in case we need year by year analysis
    profiles["LastUpdated"] = pd.to_datetime(profiles["LastUpdated"])
    profiles
    return (profiles,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Silver Layer — Cleaning & Standardisation

    Apply data quality rules, standardise formats, and register
    cleaned tables in DuckDB for SQL access.
    """)
    return


@app.cell
def _(duckdb, mot_results):
    duckdb.sql("DROP TABLE IF EXISTS silver_mot_results")
    duckdb.sql("""
        CREATE TABLE silver_mot_results AS
        SELECT
            Year,
            Region,
            VehicleType,
            TestCount,
            PassCount,
            FailCount,
            ROUND(FailCount * 100.0 / TestCount, 1) AS FailureRate,
            FailCategory_Brakes,
            FailCategory_Lights,
            FailCategory_Tyres,
            FailCategory_Emissions,
            FailCategory_Suspension,
            FailCategory_Other
        FROM mot_results
    """)
    duckdb.sql("SELECT * FROM silver_mot_results LIMIT 5").df()
    return


@app.cell
def _(duckdb, stations):
    duckdb.sql("DROP TABLE IF EXISTS silver_stations")
    duckdb.sql("""
        CREATE TABLE silver_stations AS
        SELECT
            StationId,
            StationName,
            Address,
            UPPER(REPLACE(Postcode, ' ', '')) AS Postcode,
            OwnerName,
            OwnerPhone,
            Capacity,
            CAST(OpenedDate AS DATE) AS OpenedDate
        FROM stations
    """)
    duckdb.sql("SELECT * FROM silver_stations LIMIT 5").df()
    return


@app.cell
def _(duckdb, profiles):
    duckdb.sql("DROP TABLE IF EXISTS silver_profiles")
    duckdb.sql("""
        CREATE TABLE silver_profiles AS
        SELECT
            PostcodeArea,
            VehicleType,
            AverageAge,
            Count,
            LastUpdated
        FROM profiles
    """)
    duckdb.sql("SELECT * FROM silver_profiles LIMIT 5").df()
    return


@app.cell
def _(duckdb, inspections):
    duckdb.sql("DROP TABLE IF EXISTS silver_inspections")
    duckdb.sql("""
        CREATE TABLE silver_inspections AS
        SELECT
            StationId,
            CAST(InspectionDate AS DATE) AS InspectionDate,
            Result,
            Inspector,
            Notes
        FROM inspections
    """)
    duckdb.sql("SELECT * FROM silver_inspections LIMIT 5").df()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gold Layer — Analyst-Ready Output

    Final dataset for the transport analytics team, combining station data
    with MOT results and inspection status.
    """)
    return


@app.cell
def _(duckdb, silver_inspections, silver_stations):
    duckdb.sql("DROP VIEW IF EXISTS gold_station_summary")
    duckdb.sql("""
        CREATE VIEW gold_station_summary AS
        SELECT
            s.StationId,
            s.StationName,
            s.Address,
            s.Postcode,
            s.OwnerName,
            s.OwnerPhone,
            s.Capacity,
            s.OpenedDate,
            i.InspectionDate AS LastInspectionDate,
            i.Result AS LastInspectionResult
        FROM silver_stations s
        LEFT JOIN (
            SELECT StationId, InspectionDate, Result,
                   ROW_NUMBER() OVER (PARTITION BY StationId ORDER BY InspectionDate DESC) AS rn
            FROM silver_inspections
        ) i ON s.StationId = i.StationId AND i.rn = 1
    """)
    gold_stations = duckdb.sql("SELECT * FROM gold_station_summary").df()
    gold_stations
    return


@app.cell
def _(duckdb, silver_mot_results):
    gold_output = duckdb.sql("""
        SELECT
            r.Year,
            r.Region,
            r.VehicleType,
            r.TestCount,
            r.PassCount,
            r.FailCount,
            r.FailureRate,
            r.FailCategory_Brakes,
            r.FailCategory_Lights,
            r.FailCategory_Tyres,
            r.FailCategory_Emissions,
            r.FailCategory_Suspension,
            r.FailCategory_Other
        FROM silver_mot_results r
    """).df()
    gold_output.to_parquet("data/mot_analysis_output.parquet", index=False)
    gold_output
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    **Pipeline complete.** The output parquet file is at `data/mot_analysis_output.parquet`.
    """)
    return


if __name__ == "__main__":
    app.run()
