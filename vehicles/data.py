import duckdb
from model import *


def get_brands():
    records = duckdb.sql("""
        select Id, Name from Brands
""").fetchall()

    return [Brand(r) for r in records]


def get_brand_by_name(name):
    return next((b for b in get_brands() if b.Name == name), Brand((0, name)))


def get_countries():
    records = duckdb.sql("""
        select distinct c.Id, c.Name, im.Value
        from Countries c
        inner join (
            select 
                 CountryId
                ,Value
                ,row_number() over(partition by CountryId order by Year desc) rn
            from ImportVolumes
        ) im on c.Id = im.CountryId
        where im.rn = 1
    """).fetchall()

    return [Country(r) for r in records]


def get_country_by_name(name):
    return [c for c in get_countries() if c.Name == name][0]


def get_brands_by_country_of_manufacturing():
    records = duckdb.sql("""
        select 
             r.Number
            ,c.Name
            ,r.Brand
        from Registrations r
        inner join Countries c 
            on r.CountryOfManufacturing = c.Id
    """).fetchall()

    countries = {}
    registrations = [Registration(r) for r in records]

    for record in records:
        if not record[1] in countries.keys():
            countries[record[1]] = get_country_by_name(record[1])
        
        countries[record[1]].add(Registration(record), get_brand_by_name)

    return countries.values()