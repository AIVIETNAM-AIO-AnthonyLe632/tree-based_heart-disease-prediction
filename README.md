# Tree-based heart disease prediction

Predicting heart disease from the UCI heart failure dataset (918 patients, 11 features),
mostly with tree ensembles.

```
data/         heart.csv
notebooks/    the analysis, plus helpers.py
images/       exported figures
dictionary.md what the clinical variables mean
summary-statistics.md
```

## Notebooks

| Notebook | What is in it |
| --- | --- |
| `1_eda_univariate.ipynb` | One variable at a time: distributions, skew, category counts |
| `2_eda_bivariate.ipynb` | Every feature against the target, correlation, VIF, feature ranking |
| `3_eda_multivariate.ipynb` | Pairwise structure, Mahalanobis outliers, PCA |
| `4_eda_zero-data.ipynb` | The placeholder zeros in `cholesterol` and `restingbp`, and whether they are missing at random |
| `models.ipynb` | Split, MICE imputation, encoding, feature engineering, tree models, tuning, MLP |

`notebooks/helpers.py` holds what all five share: the plot theme, the seed, the column
groups and the loader. It sits next to the notebooks so a plain `import helpers` works.

## Data

`heart.csv` has 918 rows. A `cholesterol` or `restingbp` of 0 is not a measurement, it is
a missing value written down as a zero — 172 rows for cholesterol, 1 for resting blood
pressure — so `helpers.load_data(zeros_as_missing=True)` turns those into `NaN`.

The path is resolved relative to `helpers.py`, so it works from WSL, Windows and any
working directory. Pass a path to `load_data()` to read from somewhere else.

## Requirements

`numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`, `seaborn`, `xgboost`, `catboost`.
