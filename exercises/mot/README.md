# MOT Cymru: Mostly OK, Technically

The *MOT* exercise consists of a data pipeline implemented as a [marimo](https://marimo.io/) notebook 
using Python and SQL (DuckDB). The code pretends to be a data pipeline for analysing 
MOT test outcomes across Wales, combining public test data with local station records.

## Prerequisites

To complete the exercise you will need:
* [Python](https://www.python.org/downloads/) 3.13+
* [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)
* [git](https://git-scm.com/downloads) optionally with your favourite git client.

All the required software is free, and will run on any major, up-to-date operating systems
including Linux, MacOS, Windows. If you don't have it, go and install it.

## Preparation

To prepare for the exercise:
1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Navigate to ./exercises/mot/
1. Install the dependencies by executing `uv sync`
1. Start the notebook by executing `uv run marimo edit notebook.py`
1. Run the verification cell (the one that reads from `.code`). It should display a message starting with 'Congratulations!'. You will need to send the full message to the recruiters to proceed to the next step.

If you see the message, take some time to review the code. If not, below are some troubleshooting ideas.

## Troubleshooting

If you have cloned the repository and have problems starting:
* Check you are inside the exercises/mot/ directory.
* Check you have installed the dependencies with `uv sync`.
* If `uv run marimo edit notebook.py` doesn't work, try `uv run marimo run notebook.py` to verify the setup without the editor UI.
* Make sure you are using Python 3.13 or later.
* If uv is not found, check the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

## Code Layout

* `notebook.py` is the marimo notebook containing the data pipeline.
* `data/mot_results.csv` contains MOT test outcome statistics — this is based on publicly available data.
* `data/testing_stations.csv` contains local testing station details.
* `data/vehicle_profiles.csv` contains vehicle age distributions by postcode area.
* `data/station_inspections.csv` contains quality audit records for testing stations.
