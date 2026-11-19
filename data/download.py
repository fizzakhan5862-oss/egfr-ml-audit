#!/usr/bin/env python3
"""Download scripts for source data used in the EGFR ML audit.

Raw data files are intentionally NOT committed to this repository. Run this
script to fetch them locally before running the analysis. Add source-specific
downloaders below as the audit corpus is defined.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("data/raw"),
        help="Directory to write downloaded raw data into (default: data/raw)",
    )
    args = parser.parse_args()

    out: Path = args.out
    out.mkdir(parents=True, exist_ok=True)
    print(f"Raw data directory ready: {out.resolve()}")
    print("No downloaders configured yet. Add source-specific logic here.")


if __name__ == "__main__":
    main()
