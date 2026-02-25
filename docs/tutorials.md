# Tutorials

## Analysing spacewalk data with custom output paths

This tutorial walks you through running the Spacewalks analysis pipeline with custom input and output file paths.

### Prerequisites

Make sure you have completed the [installation steps](index.md#quick-start).

### Step 1: Prepare your environment

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### Step 2: Run with default settings

Run the analysis with default input and output paths:

```bash
python eva_data_analysis.py
```

This reads from `data/eva-data.json` and writes output to `results/eva-data.csv` and `results/cumulative_eva_graph.png`.

### Step 3: Specify custom file paths

You can provide custom input and output file paths as command-line arguments:

```bash
python eva_data_analysis.py data/eva-data.json my-output.csv
```

The first argument is the path to the input JSON file, and the second is the path to the output CSV file. The graph is always saved to `results/cumulative_eva_graph.png`.

### Step 4: Check the output

Verify that the output CSV file was created and contains the expected data:

```bash
head my-output.csv
```

You should see a CSV file with columns including `eva`, `country`, `crew`, `vehicle`, `date`, `duration`, and `purpose`.
