# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python data analysis project that processes NASA Extra-Vehicular Activity (EVA/spacewalk) data. It converts JSON spacewalk records into CSV, parses durations and dates, and generates a cumulative time plot of hours spent in space over time.

## Running

No build system or package manager is configured. Run the main script directly:

```bash
python "my code v2.py"
```

The script requires `matplotlib` (only external dependency). Standard library modules used: `json`, `csv`, `datetime`.

There are no tests, linting, or CI configured.

## Architecture

- **`my code v2.py`** — Main script. Reads `data.json`, writes `data.csv`, and generates `myplot.png` (cumulative EVA hours over time).
- **`data.json`** — NASA EVA dataset (375 records). Each record has: `eva`, `country`, `crew`, `vehicle`, `date`, `duration`, `purpose`.
- **`astronaut-data-analysis-old/`** — Archived older version of the analysis script and its CSV source data.

## Key Details

- Data paths in the script are hardcoded to `/home/sarah/Projects/astronaut-analysis/` and need updating to work locally.
- Duration format in the data is `H:MM`. The script converts this to decimal hours.
- Dates are ISO 8601 timestamps; only the `YYYY-MM-DD` portion is used.
- Output graph is saved to `myplot.png` in the working directory.
