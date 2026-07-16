# Mixed and Augmented Reality in Medical Visualization — Data & Dashboard

**Live site: https://xzjiu.github.io/Mixed-and-Augmented-Reality-in-Medical-Visualization/**

This repository is the companion data page for a systematic review of
augmented reality (AR) and mixed reality (MR) visualization in medicine. It
hosts the study-level review dataset (313 studies, 1996–2026) and an
interactive dashboard for exploring it.

## What's here

- **Interactive evidence map** — publication trends, clinical specialties,
  workflow stages, display devices, imaging modalities, rendering and
  registration methods, and perception cues, all as interactive charts.
- **Article explorer** — a searchable, filterable table of every included
  study, exportable to CSV.
- **Dataset** — the raw study-level CSV
  ([data/raw/review_dataset.csv](data/raw/review_dataset.csv)), also
  downloadable from the site.

## Citation

If you use this dataset or dashboard, please cite the accompanying review
(citation will be added upon publication).

## How the site is built

Quarto Dashboards + Python (pandas, Plotly, itables), published to GitHub
Pages by GitHub Actions:

```
data/raw/review_dataset.csv
  → scripts/01_clean_data.py           clean + split multi-label fields
  → scripts/02_make_summary_tables.py  headline counts
  → *.qmd pages                        interactive charts + article table
  → quarto render                      static site → gh-pages branch
```

The processing scripts run automatically before every render, so updating
the CSV and pushing to `main` refreshes the entire site.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

quarto render .    # build into _site/
quarto preview .   # live preview
```

Requires [Quarto](https://quarto.org). If Quarto picks the wrong Python, set
`QUARTO_PYTHON=.venv/bin/python`.

## Updating the data

1. Replace `data/raw/review_dataset.csv` (keep the same column layout).
2. Commit and push to `main` — GitHub Actions re-renders and republishes the
   site automatically.
