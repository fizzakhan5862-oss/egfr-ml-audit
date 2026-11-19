#!/usr/bin/env python3
"""Generate figures for the EGFR ML audit.

Produces bar charts summarising the coded corpus. Figures are written to
results/figures/ and are generated from the audit table only.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import pandas as pd  # noqa: E402

from audit import BOOL_COLUMNS, load_audit  # noqa: E402


def barplot(series: pd.Series, title: str, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    series.plot(kind="bar", ax=ax, color="#4C72B0")
    ax.set_title(title)
    ax.set_ylabel("Number of studies")
    ax.set_xlabel("")
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"Wrote {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, default=Path("literature/audit_table.csv"))
    parser.add_argument("--out", type=Path, default=Path("results/figures"))
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    df = load_audit(args.audit)

    if df.empty:
        print("Audit table is empty - no figures to generate yet.")
        return

    for col in ["task", "modality", "validation", "data_leakage"]:
        if col in df.columns:
            barplot(
                df[col].value_counts(dropna=False),
                f"Studies by {col.replace('_', ' ')}",
                args.out / f"{col}.png",
            )

    repro = {c: int(df[c].sum()) for c in BOOL_COLUMNS if c in df.columns}
    if repro:
        barplot(
            pd.Series(repro),
            "Reproducibility indicators",
            args.out / "reproducibility.png",
        )


if __name__ == "__main__":
    main()
