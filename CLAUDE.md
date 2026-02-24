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

Then run the main script:

```bash
python eva_data_analysis.py
```

External dependencies: `pandas`, `matplotlib`. All dependencies are pinned in `requirements.txt`.

There are no tests, linting, or CI configured.

## Architecture

- **`eva_data_analysis.py`** — Main script with three functions:
  - `read_json_to_dataframe(input_file)` — reads JSON, converts types, drops rows missing duration/date
  - `write_dataframe_to_csv(df, output_file)` — writes DataFrame to CSV
  - `plot_cumulative_time_in_space(df, graph_file)` — computes cumulative hours, plots and saves graph
- **`eva-data.json`** — NASA EVA dataset (375 records). Each record has: `eva`, `country`, `crew`, `vehicle`, `date`, `duration`, `purpose`.

## Key Details

- Duration format in the data is `H:MM`. The script converts this to decimal hours using pandas string operations.
- Dates are parsed automatically by pandas via `convert_dates`.
- Output graph is saved to `cumulative_eva_graph.png` in the working directory.
