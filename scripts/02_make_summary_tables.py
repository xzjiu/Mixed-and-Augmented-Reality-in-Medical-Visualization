"""Compute headline counts used by the dashboard value boxes.

Run after 01_clean_data.py:  python3 scripts/02_make_summary_tables.py
"""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"


def main():
    studies = pd.read_csv(PROCESSED / "studies.csv")
    modality = pd.read_csv(PROCESSED / "modality_long.csv")

    summary = {
        "n_studies": int(len(studies)),
        "year_min": int(studies["publication_year"].min()),
        "year_max": int(studies["publication_year"].max()),
        "n_specialties": int(studies["specialty"].nunique()),
        "n_devices": int(studies["device"].nunique()),
        "n_modalities": int(modality["image_modalities"].nunique()),
        "n_journals": int(studies["journal"].nunique()),
    }

    with open(PROCESSED / "summary_counts.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("summary_counts.json:", summary)


if __name__ == "__main__":
    main()
