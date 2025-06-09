import duckdb
import vehicles 


def _example_of_querying_duckdb():
    results = duckdb.sql("""
        select * from Countries
    """)

    print(results.fetchall())