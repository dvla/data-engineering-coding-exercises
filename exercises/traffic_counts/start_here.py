import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Road Traffic Cymru

    Run the cell below. If everything is set up correctly it prints a short word.
    Send that word to the recruiters.
    """)
    return


@app.cell
def _(mo):
    from pathlib import Path

    mo.stop(
        not (Path("data") / "annual_traffic_flows.csv").exists(),
        "⚠ Start the notebook from the ./exercises/traffic_counts/ directory. ⚠",
    )

    with open(".code") as _f:
        _code = _f.read().strip()
    _key = "Llanishen"
    _message = "".join(
        chr(int(_code[i : i + 2], 16) ^ ord(_key[(i // 2) % len(_key)]))
        for i in range(0, len(_code), 2)
    )
    mo.md(f"**{_message}**")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Data

    Load the tables and take a quick look.
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        CREATE OR REPLACE TABLE count_points AS
        SELECT * FROM read_csv('data/count_points.csv');

        CREATE OR REPLACE TABLE local_authorities AS
        SELECT * FROM read_csv('data/local_authorities.csv');

        CREATE OR REPLACE TABLE road_categories AS
        SELECT * FROM read_csv('data/road_categories.csv');

        CREATE OR REPLACE TABLE annual_traffic_flows AS
        SELECT * FROM read_csv('data/annual_traffic_flows.csv');

        CREATE OR REPLACE TABLE hourly_traffic_counts AS
        SELECT * FROM read_csv('data/hourly_traffic_counts.csv');

        SELECT 'Tables loaded' AS status;
        """
    )
    return


@app.cell
def _(count_points, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM count_points LIMIT 5;
        """
    )
    return


@app.cell
def _(local_authorities, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM local_authorities;
        """
    )
    return


@app.cell
def _(mo, road_categories):
    _df = mo.sql(
        f"""
        SELECT * FROM road_categories;
        """
    )
    return


@app.cell
def _(annual_traffic_flows, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM annual_traffic_flows LIMIT 5;
        """
    )
    return


@app.cell
def _(mo, hourly_traffic_counts):
    _df = mo.sql(
        f"""
        SELECT * FROM hourly_traffic_counts LIMIT 5;
        """
    )
    return


if __name__ == "__main__":
    app.run()
