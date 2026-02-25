# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python data analysis project that processes NASA Extra-Vehicular Activity (EVA/spacewalk) data. It reads JSON spacewalk records into a pandas DataFrame, cleans missing values, writes CSV output, and generates a cumulative time plot of hours spent in space over time.

## Running

Set up a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Then run the main script with defaults:

```bash
python eva_data_analysis.py
```

Or specify input and output files via command-line arguments:

```bash
python eva_data_analysis.py data/eva-data.json results/eva-data.csv
```

External dependencies: `pandas`, `matplotlib`, `mkdocs`, `mkdocstrings[python]`, `mkdocs-material`. All dependencies are pinned in `requirements.txt`.

## Testing

Tests use `pytest` and `pytest-cov`. Run from the project root:

```bash
python -m pytest                # run all tests
python -m pytest --cov          # with coverage report
python -m pytest --cov --cov-report=html  # with HTML coverage report
```

Test file: `tests/test_eva_analysis.py` — covers `text_to_duration`, `calculate_crew_size`, and `summarise_categorical` with unit tests for typical values, edge cases, and invalid inputs.

CI runs automatically on push via GitHub Actions (`.github/workflows/main.yml`).

## Architecture

- **`eva_data_analysis.py`** — Main script with entry point `main(input_file, output_file, graph_file)`, guarded by `if __name__ == "__main__":`. Accepts optional `sys.argv` arguments for input/output file paths. Contains eight functions:
  - `read_json_to_dataframe(input_file)` — reads JSON, converts types, drops rows missing duration/date
  - `write_dataframe_to_csv(df, output_file)` — writes DataFrame to CSV
  - `text_to_duration(duration)` — converts `"H:MM"` string to float hours
  - `add_duration_hours(df)` — applies `text_to_duration` to add a `duration_hours` column
  - `calculate_crew_size(crew)` — parses crew string to count crew members
  - `add_crew_size_variable(df_)` — applies `calculate_crew_size` to add `crew_size` column
  - `summarise_categorical(df_, varname_)` — tabulates count/percentage distribution of a categorical variable
  - `plot_cumulative_time_in_space(df, graph_file)` — computes cumulative hours, plots and saves graph
- **`data/eva-data.json`** — NASA EVA dataset (375 records). Each record has: `eva`, `country`, `crew`, `vehicle`, `date`, `duration`, `purpose`.
- **`results/`** — Output directory (gitignored) for `eva-data.csv` and `cumulative_eva_graph.png`.
- **`tests/test_eva_analysis.py`** — pytest test suite.
- **`.github/workflows/main.yml`** — GitHub Actions CI workflow (pytest with coverage on push).
- **`README.md`** — Project overview, installation, usage, and license info.
- **`LICENSE`** — MIT License.
- **`CITATION.cff`** — Citation metadata in CFF format.
- **`mkdocs.yml`** — MkDocs configuration with Material theme and mkdocstrings plugin.
- **`docs/`** — Documentation source files:
  - `index.md` — landing page
  - `tutorials.md` — step-by-step tutorial
  - `how-to-guides.md` — practical how-to recipes
  - `reference.md` — auto-generated API reference via mkdocstrings
  - `explanation.md` — background and design decisions
- **`site/`** — Built documentation output (gitignored).

## Documentation

Build and serve docs locally:

```bash
mkdocs serve
```

Deploy to GitHub Pages:

```bash
mkdocs gh-deploy
```

Docs are published at: https://thatgardnerone.github.io/spacewalks/

## Key Details

- Duration format in the data is `H:MM`. The `text_to_duration` function converts this to decimal hours.
- Dates are parsed automatically by pandas via `convert_dates`.
- Default output graph is saved to `results/cumulative_eva_graph.png`.
- Default CSV output is saved to `results/eva-data.csv`.
