"""Clean the raw review CSV and write tidy tables to data/processed/.

Run from the project root:  python3 scripts/01_clean_data.py
Re-run whenever data/raw/review_dataset.csv changes (Quarto does this
automatically via the pre-render hook in _quarto.yml).
"""

from pathlib import Path

import pandas as pd

import labels as L

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "review_dataset.csv"
OUT = ROOT / "data" / "processed"


def explode_pipe_column(df, id_col, col):
    """Split a pipe-separated multi-label column into a long table."""
    out = (
        df[[id_col, col]]
        .dropna()
        .assign(**{col: lambda x: x[col].astype(str).str.split("|")})
        .explode(col)
    )
    out[col] = out[col].str.strip()
    out = out[out[col] != ""]
    out[col + "_label"] = L.label_series(out[col], col)
    return out.reset_index(drop=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(RAW)

    # -- basic cleaning ----------------------------------------------------
    df["publication_year"] = pd.to_numeric(df["publication_year"], errors="coerce")
    df = df.dropna(subset=["publication_year"])
    df["publication_year"] = df["publication_year"].astype(int)

    for col in ["case_report", "perception_support"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.upper()
            .map({"TRUE": True, "FALSE": False})
        )

    # display labels for single-valued coded columns
    for col in [
        "specialty",
        "device",
        "dimensionality",
        "rendering_type",
        "registration_method",
    ]:
        df[col + "_label"] = L.label_series(df[col], col)

    # readable multi-label display strings for the article explorer
    for col in L.MULTI_LABEL_COLUMNS:
        df[col + "_label"] = df[col].map(
            lambda v: (
                None
                if pd.isna(v)
                else ", ".join(L.label(col, p) for p in str(v).split("|") if p.strip())
            )
        )

    df.to_csv(OUT / "studies.csv", index=False)

    # -- long tables for multi-label columns -------------------------------
    long_tables = {
        "workflow_long.csv": "workflow_stage",
        "modality_long.csv": "image_modalities",
        "target_long.csv": "evaluation_target",
        "anchoring_long.csv": "anchoring_context",
        "perception_cues_long.csv": "perception_cues",
    }
    for fname, col in long_tables.items():
        explode_pipe_column(df, "record_id", col).to_csv(OUT / fname, index=False)

    print(f"Cleaned {len(df)} studies -> {OUT}")


if __name__ == "__main__":
    main()
