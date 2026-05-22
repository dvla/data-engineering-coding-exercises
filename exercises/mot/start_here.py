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
    ## The verification step

    Run the below cell. It will print a message with a verification code.
    Give the recruiters the code to progress to the next stage of the recruitment process.

    If you don't see the verification code you may see an error.
    You will have to make it work so you get the code.
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
    **That's it!** Send the **validation code above** to the recruiters. **Good luck** in your application process.

    However, if you want to learn more about how you can work with data in a Marimo notebooks, continue reading. Basic knowledge of Marimo notebooks will be helpful during the interview.


    .

    .

    .


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
    # otherwise its string representation will be presented. 
    _df
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        -- In SQL cells you can use SQL to query the files, too. 
        -- While some understanding of python is helpful, many things can be done using SQL
        select * from read_csv("data/sample.csv")
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Data Loading

    Marimo has three types of cells: Markdown (like this one), Python and SQL. They types are indicated in the bottom right corner next to the red bin icon, and they can be changed in the options menu in the top right corner of the cell - the (...) button.

    Data can be loaded with either Python or SQL. Data loaded with Python is accessible (as long as it is in public variables) and data loaded by SQL can be accessed in Python.
    """)
    return


@app.cell
def _(pd):
    # read data from sample.csv and save it to df1
    df1 = pd.read_csv('data/sample.csv')
    # filter the data to show only rows with Alice keeping the same name
    df1 = df1[df1['name']=='Alice']
    # display df1
    df1
    return (df1,)


@app.cell
def _(df1, mo):
    bobs = mo.sql(
        f"""
        -- df1 is also, automatically, available as a table so
        -- so it can be queried with SQL statements
        select * from df1;

        -- but it is also possible to query the source files directly in SQL
        select * 
        from read_csv('data/sample.csv')
        where name = 'Bob'
        -- the last query becomes available by variable / table name 
        -- as defined below in the 'Output variable', as long as the variable does not start with an underscore.
        """
    )
    return (bobs,)


@app.cell
def _(bobs, mo):
    _df = mo.sql(
        f"""
        -- using output of the last query in the earlier cell
        -- by using the variable name specify in the cell 'Output variable' property
        select * from bobs;

        -- but it is also possible to create tables and naming them explicitly in SQL code
        create table carols 
        as
        select * 
        from read_csv('data/sample.csv')
        where name = 'Carol'
        -- there is no output, because the last statement doens't return anything.
        """
    )
    return


@app.cell
def _(carols, mo):
    _df = mo.sql(
        f"""
        -- carols table is available for querying from 
        select * from carols;
        """
    )
    return


@app.cell
def _(bobs):
    # in python, when you use 'Output variable' option, you can just use the variable
    print(f'bobs is a regular variable of type {type(bobs)}')
    bobs
    return


@app.cell
def _(carols, duckdb):
    # but carols is not available as a variable. 
    # to use it in Python, we need to query it as a SQL table
    df2 = duckdb.sql("select * from carols").df()
    # the .df() is important to get to pandas dataframe. 
    df2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Exercise

    The exercise will be about working with data not about proficiency with Marimo notebooks.
    We use Marimo to ensure everybody has the same modern interface with access to both python and SQL, and without any unnecessary dependencies.

    During the interview we will provide you with a laptop with everything set up, and a notebook running. The tasks can be solved with either SQL or Python, or with a mixture of both.
    """)
    return


if __name__ == "__main__":
    app.run()
