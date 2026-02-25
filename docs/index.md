# Spacewalks

Analysis of NASA Extra-Vehicular Activity (EVA) data.

This project reads JSON spacewalk records, cleans and processes the data, outputs a CSV summary, and generates a cumulative time plot of hours spent in space over time.

## Quick Start

```bash
git clone https://github.com/thatgardnerone/spacewalks.git
cd spacewalks
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python eva_data_analysis.py
```

## Contents

- [Tutorials](tutorials.md) — step-by-step guides for getting started
- [How-To Guides](how-to-guides.md) — practical recipes for common tasks
- [Reference](reference.md) — API reference for all functions
- [Explanation](explanation.md) — background and design decisions
