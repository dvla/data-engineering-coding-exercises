# Data Engineering Coding Exercises

## Vehicles

The *Vehicles* exercise consists of a sample command line application written 
using Python (3.13) and SQL (duckdb). The code pretends to be a command line utility
which can be used to query the data about vehicle registrations. 

### Prerequisits

To execute the exercise code you will need:
* [Python](https://www.python.org/downloads/) 3.13+
* [Poetry package manager](https://python-poetry.org/docs/) 2.1+
* [git](https://git-scm.com/downloads) optionally with your favourite git client.

All the required software is free, and will run on any major, up-to-date operating systems
including Linux, MacOS, Windows. If you don't have it, go and install it.

### Preparation

To prepare for the exercise:
1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. [Activate poetry environment](https://python-poetry.org/docs/managing-environments/)
1. [install the dependencies](https://python-poetry.org/docs/cli/#sync) by executing `poetry sync` or `poetry install`
1. Execute `python vehicles` to test if you are ready to start the exercise. It should return a line of text starting with 'Congratulations!'. You will need to send the full line to the recruiters to go to the next step. 

If you see the text, consider reviewing the code. If not, below are some troubleshooting ideas.

### Troubleshooting

If you have cloned the repository and have problems starting:
* Check you are inside the cloned repository.
* Check you have activated the poetry environment.
* Check you have installed the dependencies.
* If the `python vehicles` doesn't work, try `python3 vehicles`.

### Code layout

* `vehicles/__main__.py` is where the CLI behaviour is implemented.
The entry point, `main()` can be found there. 
* `vehicles/model.py` defines the domain model.
* `vehicles/data.py` offers functions to query the data.
* `vehicles/data/*.csv` test data in CSV format - this is made up, not real data.
* `vehicles/__init__.py` loads the data from the CSV files into duckdb memory.

### Tasks

The tasks are currently not public as they are used during interviews. 
If you have been sent this repository because you are going through the interview
familiarise yourself with the code as you will be asked to work with it. 

Once the exercise is no longer used for interviewing, we will publish the tasks
so that the exercise can be used independently to practice your coding skills. 
