# EGFR ML Audit

A reproducible audit of machine-learning studies that predict EGFR mutation status
(and related clinical endpoints) from clinical, genomic, or imaging data.

> **Status:** scaffold in progress. Findings are placeholders until the audit is run.

---

## Research question

How well do published machine-learning models for EGFR-related prediction tasks
generalise, and are their reported results reproducible and free of common
methodological pitfalls (e.g. data leakage, lack of external validation,
insufficient reporting)?

## Findings

_Fill in once the audit is complete._

- **Corpus:** N studies screened, M included (see `literature/audit_table.csv`).
- **Key result:** pending.
- **Reproducibility:** pending — proportion of studies with public code/data.

See `results/` for generated tables and `results/figures/` for plots.

## How to reproduce

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download source data (scripts only; raw files are not versioned)
python data/download.py --out data/raw

# 3. Run the analysis
python src/audit.py --audit literature/audit_table.csv --out results/

# 4. Generate figures
python src/figures.py --audit literature/audit_table.csv --out results/figures/
```

See `protocol.md` for the search strategy, inclusion criteria, and coding sheet.

## Repository layout

| Path | Purpose |
|------|---------|
| `protocol.md` | Search strategy, inclusion criteria, coding sheet |
| `literature/` | Search results (CSV) and the coded audit table |
| `data/` | Download scripts only — raw data are **not** committed |
| `src/` | Analysis code |
| `results/` | Generated tables and `figures/` |
| `logs/` | Experiment logs (from `nature-experiment-log`) |

## Licence

Code is MIT licensed; data tables are CC BY 4.0. See `LICENSE`.
