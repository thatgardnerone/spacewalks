# Spacewalks

Analysis of NASA Extra-Vehicular Activity (EVA) data. This project reads JSON spacewalk records, cleans and processes the data, outputs a CSV summary, and generates a cumulative time plot of hours spent in space over time.

## Features

- Reads and cleans NASA EVA JSON data (375 records)
- Exports processed data to CSV
- Calculates crew sizes from crew strings
- Summarises categorical variable distributions (counts and percentages)
- Generates a cumulative duration plot of spacewalk hours over time

## Pre-requisites

- Python >= 3.12
- pandas >= 3.0
- matplotlib >= 3.10
- numpy >= 2.4
- pytest (for running tests)

## Installation

```bash
git clone https://github.com/thatgardnerone/spacewalks.git
cd spacewalks
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Verify the installation by running the test suite:

```bash
python -m pytest
```

## Usage

Run with default input/output paths:

```bash
python eva_data_analysis.py
```

Or specify custom input and output files:

```bash
python eva_data_analysis.py data/eva-data.json results/eva-data.csv
```

Output files are saved to the `results/` directory by default:
- `results/eva-data.csv` — cleaned data in CSV format
- `results/cumulative_eva_graph.png` — cumulative spacewalk hours plot

## Documentation

Full documentation is available at [https://thatgardnerone.github.io/spacewalks/](https://thatgardnerone.github.io/spacewalks/).

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Citation

If you use this software in your research, please cite it using the metadata in [CITATION.cff](CITATION.cff).
