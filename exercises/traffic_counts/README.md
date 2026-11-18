# Road Traffic Cymru

A marimo notebook (Python and SQL via DuckDB) over road traffic counts for Wales.

## Preparation

1. Navigate to ./exercises/traffic_counts/
1. Install the dependencies by executing `uv sync`
1. Start the notebook by executing `uv run marimo edit start_here.py`
1. Run the verification cell. It should display a short word. Send it to the recruiters.

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).

## Data

Source: DfT [road traffic statistics](https://roadtraffic.dft.gov.uk/), downloads from data.gov.uk.
Welsh count points only, 2016 to 2025, reshaped into separate tables.
Contains public sector information licensed under the Open Government Licence v3.0.

| File | Grain | Key |
|------|-------|-----|
| `count_points.csv` | one row per count point: road, local authority, location, link length | `count_point_id` |
| `local_authorities.csv` | lookup | `local_authority_code` |
| `road_categories.csv` | lookup | `road_category` |
| `annual_traffic_flows.csv` | estimated annual average daily flow per count point per year, by vehicle type | `count_point_id`, `year` |
| `hourly_traffic_counts.csv` | manual hourly counts per count point, direction of travel and count date, by vehicle type | `count_point_id`, `count_date`, `hour`, `direction_of_travel` |

Empty values mean the figure was not available.
