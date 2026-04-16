import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # MOT Cymru: Mostly OK, Technically

        A data pipeline for analysing MOT test outcomes across Wales.

        This notebook loads data from multiple sources, combines them,
        and produces analysis-ready datasets for the transport analytics team.
        """
    )
    return


@app.cell
def _():
    import duckdb
    import pandas as pd
    import base64
    from pathlib import Path
    return base64, duckdb, pd, Path


@app.cell
def _(mo, base64, Path):
    _code_path = Path("exercises/mot/.code")
    if not _code_path.exists():
        _code_path = Path(".code")
    with open(_code_path, "r") as _f:
        _encoded = _f.read().strip()
    _message = base64.b64decode(_encoded).decode("utf-8")
    mo.md(f"**{_message}**")
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Data Loading

        The pipeline loads data from four sources:
        1. **MOT Results** — national test outcome statistics (public data)
        2. **Testing Stations** — local station details
        3. **Vehicle Profiles** — vehicle age distributions by area
        4. **Station Inspections** — quality audit records
        """
    )
    return


@app.cell
def _(duckdb, pd, Path):
    _data_dir = Path("exercises/mot/data")
    if not _data_dir.exists():
        _data_dir = Path("data")

    mot_results = pd.read_csv(_data_dir / "mot_results.csv")
    conn = duckdb.connect()
    conn.execute("CREATE TABLE mot_results AS SELECT * FROM mot_results")
    return conn, mot_results, _data_dir


@app.cell
def _(pd, _data_dir, conn):
    stations = pd.read_csv(_data_dir / "TestingStations.csv")
    conn.execute("CREATE TABLE testing_stations AS SELECT * FROM stations")
    return (stations,)


@app.cell
def _(pd, _data_dir, conn):
    profiles = pd.read_csv(_data_dir / "vehicle_profiles.csv")
    profiles["LastUpdated"] = pd.to_datetime(profiles["LastUpdated"])
    conn.execute("CREATE TABLE vehicle_profiles AS SELECT * FROM profiles")
    return (profiles,)


@app.cell
def _(pd, _data_dir, conn):
    try:
        inspections = pd.read_csv(_data_dir / "station_inspections.csv")
        inspections["StationId"] = inspections["StationId"].astype(int)
        conn.execute(
            "CREATE TABLE station_inspections AS SELECT * FROM inspections"
        )
    except:
        pass
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Data Summary

        Quick look at what we have loaded.
        """
    )
    return


@app.cell
def _(mot_results):
    mot_results.head(10)
    return


@app.cell
def _(stations):
    stations.head(10)
    return


@app.cell
def _(profiles):
    profiles.describe()
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Analysis

        Use the cells below for your work.
        """
    )
    return


@app.cell
def _(conn):
    conn.sql("SELECT Region, VehicleType, SUM(TestCount) as TotalTests FROM mot_results GROUP BY Region, VehicleType").df()
    return


if __name__ == "__main__":
    app.run()
