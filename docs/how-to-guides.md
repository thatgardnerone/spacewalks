# How-To Guides

## How to change the output file path

By default, the analysis script writes its CSV output to `results/eva-data.csv`. To change this, pass custom file paths as command-line arguments:

```bash
python eva_data_analysis.py data/eva-data.json path/to/custom-output.csv
```

Both arguments must be provided together — the first is the input JSON file and the second is the output CSV path.

## How to run tests

Run the full test suite with:

```bash
python -m pytest
```

To include a coverage report:

```bash
python -m pytest --cov
```

To generate an HTML coverage report:

```bash
python -m pytest --cov --cov-report=html
```

The HTML report will be available in the `htmlcov/` directory.

## How to build the documentation locally

Install the documentation dependencies:

```bash
pip install zensical mkdocs mkdocstrings[python] mkdocs-material
```

Build and serve the docs locally:

```bash
zensical serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

Documentation is automatically deployed to GitHub Pages when changes are pushed to `main`.
