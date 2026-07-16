# Medical AR/MR Visualization — Interactive Evidence Map

Interactive dashboard for a study-level systematic review of AR/MR
visualization in medicine (313 studies, 1996–2026).

Built with **Quarto Dashboards + Python + pandas + Plotly + itables**,
published as a static site on **GitHub Pages**.

## How it works

```
data/raw/review_dataset.csv
  → scripts/01_clean_data.py        (clean + explode multi-label columns)
  → scripts/02_make_summary_tables.py (headline counts)
  → *.qmd pages                     (Plotly charts + searchable table)
  → quarto render                   (static site in _site/)
```

The two scripts run automatically before every render (`pre-render` hook in
`_quarto.yml`), so **updating the CSV and re-rendering refreshes the whole
site**.

## Local development

```bash
# one-time setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# preview with live reload
quarto preview

# build the static site into _site/
quarto render
```

Quarto must be installed (https://quarto.org/docs/get-started/). If it is not
on your PATH, point Quarto at the venv Python with
`export QUARTO_PYTHON=.venv/bin/python`.

## Updating the data

1. Replace `data/raw/review_dataset.csv` (same column layout).
2. `quarto render` locally, or just commit + push — GitHub Actions rebuilds
   and republishes the site automatically.

## Publishing on GitHub Pages

1. Create a GitHub repo and push this folder to the `main` branch.
2. The included workflow (`.github/workflows/publish.yml`) renders the site
   and pushes it to the `gh-pages` branch on every push to `main`.
3. In the repo settings → Pages, set the source to the `gh-pages` branch
   (root). The site appears at `https://<username>.github.io/<repo>/`.

## Pages

| Page | Content |
|---|---|
| Home | Headline counts + publication trend |
| Overview | Trend, analysis periods, workflow → device → rendering Sankey |
| Clinical Areas | Specialty, workflow stage, evaluation target, specialty × workflow heatmap |
| Technology | Device, dimensionality, image modality, device × modality heatmap |
| Visualization Methods | Rendering, registration, anchoring, perception support & cues |
| Article Explorer | Searchable, filterable, exportable table of all included studies |
| About | Variable descriptions and citation info |
