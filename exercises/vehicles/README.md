# Vehicles Exercise

The *Vehicles* exercise consists of a sample command line application written 
using Python (3.13) and SQL (duckdb). The code pretends to be a command line utility
which can be used to query the data about vehicle registrations.

## Prerequisites

To execute the exercise code you will need:
* [Python](https://www.python.org/downloads/) 3.13+
* [Poetry package manager](https://python-poetry.org/docs/) 2.1+
* [git](https://git-scm.com/downloads) optionally with your favourite git client.

All the required software is free, and will run on any major, up-to-date operating systems
including Linux, MacOS, Windows. If you don't have it, go and install it.

## Preparation

To prepare for the exercise:
1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Navigate to ./exercises/vehicles/
1. [Activate poetry environment](https://python-poetry.org/docs/managing-environments/)
1. [Install the dependencies](https://python-poetry.org/docs/cli/#sync) by executing `poetry sync` or `poetry install`
1. Execute `python vehicles` to test if you are ready to start the exercise. You should see a line starting with 'OK'. If you do, consider reviewing the code before starting the tasks.

If you see the text, consider reviewing the code. If not, below are some troubleshooting ideas.

## Troubleshooting

If you have cloned the repository and have problems starting:
* Check you are inside the cloned repository.
* Check you have activated the poetry environment.
* Check you have installed the dependencies.
* If the `python vehicles` doesn't work, try `python3 vehicles`.

## Code layout

* `vehicles/__main__.py` is where the CLI behaviour is implemented.
The entry point, `main()` can be found there. 
* `vehicles/model.py` defines the domain model.
* `vehicles/data.py` offers functions to query the data.
* `vehicles/data/*.csv` test data in CSV format - this is made up, not real data.
* `vehicles/__init__.py` loads the data from the CSV files into duckdb memory.

## Tasks

### 1 - order the output ⭐

A user complains that the countries are not ordered alphabetically when they execute `python vehicles show imports`. 

### 2 - countries with no imports ⭐⭐

Now that the countries are ordered alphabetically, the user notices that Russia is not showing up. 
Due to sanctions, there should be no new vehicle registrations from it, so that is probably OK.
However, the user would like to see the country in the list even if there are no registrations of cars built there, 
just to make sure that there are none. 
Can you make sure that `python vehicles show imports` shows records for countries with no registrations?

### 3 - data quality ⭐⭐

A user notices that the output of `python vehicles show top` doesn't look right. 
Some brands appear multiple times under the same country when they probably shouldn't. 
Can you investigate and fix the issue?

### 4 - performance issues ⭐⭐⭐

Another user complains that `python vehicles show top` is slow in production.
It is fast enough in development, the only data you have access to, so you will have to investigate the code
and implement changes you think are likely to help with the issue. 

### 5 - data export function ⭐⭐⭐

Implement an export functionality which allows the users to produce a data file instead of displaying the results to the screen. 

