"""Setup shared by the heart-disease notebooks.

Every notebook starts with the same three lines:

    import helpers
    helpers.setup()
    data = helpers.load_data()
"""

import os
import random
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns

# Relative to this file, so it works from WSL, Windows and any working directory.
DATA_PATH = Path(__file__).resolve().parents[1] / 'data' / 'heart.csv'

SEED = 42

CAT_COLS = ['sex', 'chestpaintype', 'fastingbs', 'restingecg',
            'exerciseangina', 'st_slope', 'heartdisease']
NUM_COLS = ['age', 'restingbp', 'cholesterol', 'maxhr', 'oldpeak']

# A cholesterol or resting blood pressure of 0 is not a measurement,
# it is a missing value that was written down as a zero.
ZERO_AS_MISSING = ['cholesterol', 'restingbp']


def set_seed(seed=SEED):
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)


def set_theme():
    """Paper-style plots: serif fonts, colourblind palette, no top/right spines."""
    sns.set_theme(
        context='paper',
        style='whitegrid',
        palette='colorblind',
        rc={
            'figure.figsize': (12, 10),
            'font.family': 'serif',
            'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif'],
            'mathtext.fontset': 'dejavuserif',
            'axes.labelsize': 12,
            'axes.titlesize': 14,
            'xtick.labelsize': 10,
            'ytick.labelsize': 10,
            'legend.fontsize': 10,
            'legend.title_fontsize': 12,
            'axes.spines.top': False,
            'axes.spines.right': False,
            'axes.grid': True,
            'grid.alpha': 0.3,
            'axes.linewidth': 1.2,
            'xtick.major.width': 1.2,
            'ytick.major.width': 1.2,
            'figure.dpi': 100,
            'savefig.dpi': 300,
            'savefig.bbox': 'tight',
        },
    )


def setup():
    """Seed the random number generators and apply the plot theme."""
    set_seed()
    set_theme()


def load_data(path=DATA_PATH, zeros_as_missing=False):
    """Read heart.csv with lower-cased column names.

    With zeros_as_missing=True the placeholder zeros in cholesterol and
    resting blood pressure become NaN.
    """
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()
    if zeros_as_missing:
        df[ZERO_AS_MISSING] = df[ZERO_AS_MISSING].replace(0, np.nan)
    return df


def overview(df):
    """Print the usual first-look summary of a dataframe."""
    rule = '-' * 100

    print(f'Shape: {df.shape[0]} rows, {df.shape[1]} columns')
    print(f'Duplicated rows: {df.duplicated().sum()}')
    print(rule)

    print('Head:')
    print(df.head().to_string())
    print('\nTail:')
    print(df.tail().to_string())
    print(rule)

    df.info()
    print(rule)

    print('Numeric summary:')
    print(df.describe().T.to_string())
    print(rule)

    print('Category counts:')
    for col in df.select_dtypes(include='object').columns:
        counts = df[col].value_counts()
        share = (counts / len(df) * 100).round(2)
        print(f'\n{col}')
        print(pd.DataFrame({'count': counts, 'percent': share}).to_string())
