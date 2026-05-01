import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # MOT Cymru: Mostly OK, Technically

    This is an introduction to the exercise to ensure everything is set up correctly.

    It is also an opportunity to learn about [DuckDB](https://duckdb.org )
    or explore [Marimo](https://marimo.io) notebooks which might be unfamiliar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The imports

    Run the cell below to ensure all the necessary libraries are imported.

    The `marimo` library has to be loaded first (it is in the first cell above, make sure to run it) for markdown cells to work. Generally it is best to execute all the cells one after the other, or run them all by clicking the play symbol in the bottom right.
    """)
    return


@app.cell
def _():
    import duckdb        
    import pandas as pd 
    from pathlib import Path

    return Path, duckdb, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The check

    Run the below cell. It will print a message with a verification code. Tell the recruiters the code.
    If you don't see the verification code you may see an error. You will have to follow the documentation and make it work so you get the code.
    """)
    return


@app.cell
def _(Path, mo):
    mo.stop(
        not str(Path.cwd()).endswith("mot"),
        "⚠️ For the exercise to work you should be in ./experiments/mot/ directory.⚠️"
    )

    with open(".code") as _f:
        _code = _f.read().strip()
        _message = ''.join(chr(int(_code[i:i+2], 16) ^ ord("Pontypandy"[(i//2) % 10])) for i in range(0, min(148, len(_code)), 2))
    mo.md(f"**{_message}!**")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That's it, however, if you want to learn more about how you can work with data in a Marimo notebook, continue reading.

    ## The data

    The data for the exercise is in `./data/` directory and consists mostly of CSV files. You can explore it in any way you want, but here is how it is possible to work with the data in the notebook.
    """)
    return


@app.cell
def _(Path):
    # You can list the files iterating over contents of the directory. 
    _files = [_f for _f in Path("data").iterdir() if _f.is_file()]
    for _file in sorted(_files):
        print(_file)
    return


@app.cell
def _():
    # You can read the file as text
    with open("data/sample.csv") as _sample_file:
        # print is rendered below the cell
        print(_sample_file.read())
    return


@app.cell
def _(pd):
    # the data can be read into a dataframe
    _df = pd.read_csv("data/sample.csv")

    # the output of the last statement may be rendered if it is of a supported type
    # otherwise it's string representation will be presented. 
    _df
    return


@app.cell(hide_code=True)
def _(mo):
    _df = mo.sql(
        f"""
        -- SQL cells can use SQL to query the files
        select * from read_csv("data/sample.csv")
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    _df = mo.sql(
        f"""
        select * from read_csv("data/sample.csv")
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Data Loading

    The pipeline loads data from four sources:
    1. **MOT Results** — national test outcome statistics (public data)
    2. **Testing Stations** — local station details
    3. **Vehicle Profiles** — vehicle age distributions by area
    4. **Station Inspections** — quality audit records
    """)
    return


@app.cell
def _(duckdb, pd):
    mot_results = pd.read_csv("data/mot_results.csv")
    conn = duckdb.connect()
    conn.execute("CREATE TABLE mot_results AS SELECT * FROM mot_results").df()
    return conn, mot_results


@app.cell(hide_code=True)
def _(mo, mot_results):
    _df = mo.sql(
        f"""
        select * from mot_results
        """
    )
    return


@app.cell
def _(conn, pd):
    stations = pd.read_csv(_data_dir / "TestingStations.csv")
    conn.execute("CREATE TABLE testing_stations AS SELECT * FROM stations")
    return (stations,)


@app.cell
def _(conn, pd):
    profiles = pd.read_csv(_data_dir / "vehicle_profiles.csv")
    profiles["LastUpdated"] = pd.to_datetime(profiles["LastUpdated"])
    conn.execute("CREATE TABLE vehicle_profiles AS SELECT * FROM profiles")
    return (profiles,)


@app.cell
def _(conn, pd):
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
    mo.md("""
    ## Data Summary

    Quick look at what we have loaded.
    """)
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
    mo.md("""
    ## Analysis

    Use the cells below for your work.
    """)
    return


@app.cell
def _(conn):
    conn.sql("SELECT Region, VehicleType, SUM(TestCount) as TotalTests FROM mot_results GROUP BY Region, VehicleType").df()
    return


if __name__ == "__main__":
    app.run()
