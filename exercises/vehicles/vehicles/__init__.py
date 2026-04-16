import duckdb


duckdb.sql("""
create table Brands(
     Id         int primary key
    ,CountryId  int
    ,Name       varchar
);
           
copy Brands
from 'vehicles/data/Brands.csv'
(auto_detect true)
""")


duckdb.sql("""
create table Countries(
     Id     int primary key
    ,Name   varchar
);
           
copy Countries
from 'vehicles/data/Countries.csv'
(auto_detect true)
""")


duckdb.sql("""
create table ImportVolumes (
     Id         int primary key
    ,CountryId  int
    ,Year       int
    ,Value      int
);

copy ImportVolumes
from 'vehicles/data/ImportVolumes.csv'
(auto_detect true)
""")


duckdb.sql("""
create table Registrations (
     Number                     varchar primary key
    ,CountryOfManufacturing     int
    ,Brand                      varchar
);         

copy Registrations
from 'vehicles/data/Registrations.csv'
(auto_detect true)
""")
