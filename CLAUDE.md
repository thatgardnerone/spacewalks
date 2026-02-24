# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python data analysis project that processes NASA Extra-Vehicular Activity (EVA/spacewalk) data. It converts JSON spacewalk records into CSV, parses durations and dates, and generates a cumulative time plot of hours spent in space over time.

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

The script requires `matplotlib` (only external dependency). Standard library modules used: `json`, `csv`, `datetime`. All dependencies are pinned in `requirements.txt`.

There are no tests, linting, or CI configured.

## Architecture

- **`eva_data_analysis.py`** — Main script. Reads `eva-data.json`, writes `eva-data.csv`, and generates `cumulative_eva_graph.png` (cumulative EVA hours over time).
- **`eva-data.json`** — NASA EVA dataset (375 records). Each record has: `eva`, `country`, `crew`, `vehicle`, `date`, `duration`, `purpose`.

## Key Details

- Duration format in the data is `H:MM`. The script converts this to decimal hours.
- Dates are ISO 8601 timestamps; only the `YYYY-MM-DD` portion is used.
- Output graph is saved to `cumulative_eva_graph.png` in the working directory.
