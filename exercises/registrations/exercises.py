import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import duckdb
    import pandas as pd

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Vehicle Licensing Statistics — Coding Exercise

    Data from DfT/DVLA Vehicle Licensing Statistics (Open Government Licence v3.0).

    You have **15 minutes** and **three tasks**. They get progressively harder — don't worry if you don't finish all three. Talk us through your thinking as you go.

    You can use **SQL**, **Python**, or both — whichever you're most comfortable with.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Data

    Three tables are loaded below:

    | Table | Description | Columns |
    |-------|-------------|---------|
    | `registrations` | Quarterly new vehicle registrations (2023–2025) | year, quarter, region, body_type, fuel_type, count |
    | `licensed_vehicles` | Licensed vehicle stock at end of year (2023–2025) | year, region, body_type, fuel_type, count |
    | `fuel_types` | Fuel type lookup with ULEV classification | fuel_code, fuel_description, is_ulev |
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        CREATE OR REPLACE TABLE registrations AS
        SELECT * FROM read_csv('data/registrations.csv');

        CREATE OR REPLACE TABLE licensed_vehicles AS
        SELECT * FROM read_csv('data/licensed_vehicles.csv');

        CREATE OR REPLACE TABLE fuel_types AS
        SELECT * FROM read_csv('data/fuel_types.csv');

        SELECT 'Tables loaded' as status;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Quick look at the data
    """)
    return


@app.cell
def _(mo, registrations):
    _df = mo.sql(
        f"""
        SELECT * FROM registrations LIMIT 5;
        """
    )
    return


@app.cell
def _(licensed_vehicles, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM licensed_vehicles LIMIT 5;
        """
    )
    return


@app.cell
def _(fuel_types, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM fuel_types;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Task 1 — Filter and aggregate

    > How many battery electric **cars** (BEV) were registered in **Wales** across all quarters of **2025**?
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        -- Task 1: write your query here
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Task 2 — Join and aggregate

    > How many licensed **ultra-low emission vehicles (ULEVs)** were there in each region at the end of **2025**?
    >
    > Use the `fuel_types` table to determine which fuel types are ULEVs. Order by the total descending.
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        -- Task 2: write your query here
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Task 3 — Data quality investigation

    > A colleague wrote the query below to produce registration totals by region for Q3 2025, but a stakeholder says the numbers look too high compared to other quarters.
    >
    > Investigate why the totals are wrong and fix the query.
    """)
    return


@app.cell
def _(mo, registrations):
    _df = mo.sql(
        f"""
        -- This query produces incorrect results. Why?
        SELECT region, SUM(count) AS total_registrations
        FROM registrations
        WHERE year = 2025 AND quarter = 3
        GROUP BY region
        ORDER BY total_registrations DESC
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        -- Task 3: write your corrected query here
        """
    )
    return


if __name__ == "__main__":
    app.run()
