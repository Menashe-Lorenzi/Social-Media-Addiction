import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from IPython.display import display
from sklearn.preprocessing import StandardScaler

def analyze_dataframe(df, exclude_cols, threshold=0.05):
    n_rows = df.shape[0]

    # Remove excluded columns
    df = df.drop(columns=[col for col in exclude_cols if col in df.columns])

    # Step 1: Create summary table
    unique_counts = df.nunique()
    unique_ratio = unique_counts / n_rows

    summary = pd.DataFrame({
        'Unique Values': unique_counts,
        'Missing Values': df.isnull().sum(),
        'Unique Ratio': unique_ratio
    })

    summary['Suggested Type'] = np.where(
        (df.dtypes == 'object') | (df.dtypes == 'category') | (unique_ratio < threshold),
        'Categorical',
        'Numeric'
    )

    # Show summary table
    display(summary)

    # Step 2: Separate columns
    categorical_cols = summary[summary['Suggested Type'] == 'Categorical'].index.tolist()
    numeric_cols = summary[summary['Suggested Type'] == 'Numeric'].index.tolist()

    # Step 3: Plot categorical
    if categorical_cols:
        n = len(categorical_cols)
        ncols = 3
        nrows = math.ceil(n / ncols)

        fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4 * nrows))
        axes = axes.flatten()
        fig.suptitle('Categorical Variables Distribution', fontsize=16)

        for i, col in enumerate(categorical_cols):
            df[col].value_counts().plot(kind='bar', ax=axes[i])
            axes[i].set_title(col)
            axes[i].set_xlabel('')
            axes[i].set_ylabel('Frequency')
            axes[i].grid(axis='y', linestyle='--', alpha=0.7)
            axes[i].tick_params(axis='x', rotation=45)

        # Remove empty plots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    # Step 4: Plot numeric
    if numeric_cols:
        n = len(numeric_cols)
        ncols = 3
        nrows = math.ceil(n / ncols)

        fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4 * nrows))
        axes = axes.flatten()
        fig.suptitle('Numeric Variables Distribution', fontsize=16)

        for i, col in enumerate(numeric_cols):
            df[col].hist(bins=20, edgecolor='black', ax=axes[i])
            axes[i].set_title(col)
            axes[i].set_xlabel('')
            axes[i].set_ylabel('Frequency')
            axes[i].grid(axis='y', linestyle='--', alpha=0.7)

        # Remove empty plots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    # ✅ Step 5: Return summary and column lists
    return summary, categorical_cols, numeric_cols


def plot_boxplots_before_outliers(df, exclude_cols):
    """
    Plots boxplots for all numeric columns before outlier handling.

    Parameters:
    - df: pandas DataFrame
    - exclude_cols: list of columns to exclude (default ['id'])
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]

    n = len(numeric_cols)
    ncols = 3
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4 * nrows))
    axes = axes.flatten()
    fig.suptitle('Boxplots Before Outlier Handling', fontsize=16)

    for i, column in enumerate(numeric_cols):
        axes[i].boxplot(df[column].dropna())
        axes[i].set_title(column)
        axes[i].grid(axis='y', linestyle='--', alpha=0.7)


    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

def standardize_numeric_columns(df):
    df_std = df.copy()

    numeric_cols = ['Avg_Daily_Usage_Hours','Sleep_Hours_Per_Night']

    scaler = StandardScaler()
    df_std[numeric_cols] = scaler.fit_transform(df_std[numeric_cols])

    print(f'Standardized columns: {numeric_cols}')
    return df_std