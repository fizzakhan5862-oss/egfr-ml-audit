#!/usr/bin/env python3
"""Core analysis for the EGFR ML audit.

Reads the coded audit table and emits summary tables describing the corpus:
counts by task, modality, validation strategy, and reproducibility indicators.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


BOOL_COLUMNS = [
    "external_validation",
    "baseline_comparison",
    "code_available",
    "data_available",
]


def load_audit(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    for col in BOOL_COLUMNS:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper().eq("TRUE")
    return df


def summarise(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    n = len(df)
    summaries: dict[str, pd.DataFrame] = {}

    for col in ["task", "modality", "model", "validation", "data_leakage"]:
        if col in df.columns:
            summaries[f"by_{col}"] = (
                df[col].value_counts(dropna=False).rename("n").to_frame()
            )

    repro = pd.DataFrame(
        {
            "n": [n],
            "n_external_validation": [int(df.get("external_validation", pd.Series(dtype=bool)).sum())],
            "n_code_available": [int(df.get("code_available", pd.Series(dtype=bool)).sum())],
            "n_data_available": [int(df.get("data_available", pd.Series(dtype=bool)).sum())],
            "n_baseline_comparison": [int(df.get("baseline_comparison", pd.Series(dtype=bool)).sum())],
        }
    )
    summaries["reproducibility"] = repro
    return summaries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, default=Path("literature/audit_table.csv"))
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    df = load_audit(args.audit)

    if df.empty:
        print("Audit table is empty - nothing to summarise yet.")

    for name, table in summarise(df).items():
        dest = args.out / f"{name}.csv"
        table.to_csv(dest, index_label="category")
        print(f"Wrote {dest}")


if __name__ == "__main__":
    main()
