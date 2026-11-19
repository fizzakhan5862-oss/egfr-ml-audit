# Audit protocol

This document pre-registers the search strategy, inclusion criteria, and coding
sheet for the EGFR ML audit. Finalise before coding studies to reduce bias.

## 1. Search strategy

**Databases:** PubMed, Embase, Web of Science, IEEE Xplore, arXiv.

**Date range:** 2015-01-01 to present.

**Concepts (AND):**
1. EGFR (epidermal growth factor receptor) OR EGFR mutation OR EGFR-TKI
2. machine learning OR deep learning OR artificial intelligence OR radiomics OR classifier

**Example PubMed query:**
```
("EGFR"[Title/Abstract] OR "epidermal growth factor receptor"[Title/Abstract])
AND
("machine learning"[Title/Abstract] OR "deep learning"[Title/Abstract]
 OR "radiomics"[Title/Abstract] OR "artificial intelligence"[Title/Abstract])
AND ("2015/01/01"[Date - Publication] : "3000"[Date - Publication])
```

Search results are exported to `literature/search_results.csv`. Record the exact
query string, database, and date run in the `search_log` column.

## 2. Inclusion criteria

**Include if:**
- Peer-reviewed article or preprint reporting an original ML model
- Predicts EGFR mutation status, EGFR expression, or EGFR-TKI response
- Reports a quantitative performance metric (AUC, accuracy, F1, etc.)

**Exclude if:**
- Review, editorial, or meta-analysis with no original model
- No EGFR-related endpoint
- Purely descriptive statistics with no predictive model
- Non-English full text

Screening is two-stage: title/abstract, then full text. Record exclusions with reasons.

## 3. Coding sheet

Each included study is coded in `literature/audit_table.csv`. Columns:

| Column | Type | Description |
|--------|------|-------------|
| `study_id` | str | Unique ID, e.g. `S001` |
| `first_author` | str | First author surname |
| `year` | int | Publication year |
| `doi` | str | Digital Object Identifier |
| `task` | str | Prediction task (mutation / expression / TKI response) |
| `modality` | str | Data modality (clinical / genomic / imaging / multi) |
| `n_samples` | int | Cohort size |
| `n_features` | int | Number of input features |
| `model` | str | Model class (logistic / RF / SVM / NN / other) |
| `validation` | str | random split / k-fold / external / none |
| `external_validation` | bool | Whether an independent external cohort was used |
| `data_leakage` | str | none / suspected / confirmed / unclear |
| `baseline_comparison` | bool | Compared against a non-ML baseline |
| `metric` | str | Primary metric reported |
| `metric_value` | float | Primary metric value |
| `code_available` | bool | Code publicly available |
| `data_available` | bool | Data publicly available |
| `notes` | str | Free-text notes |

Booleans use `TRUE`/`FALSE`. Leave unknown fields blank rather than guessing.
Two reviewers code independently; disagreements are resolved by discussion.
