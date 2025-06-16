import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind, f_oneway

def run_statistical_tests(df, binary_columns=None, verbose=True):
    """
    Run Chi-squared, T-test, and ANOVA tests between variables in a DataFrame.

    Parameters:
        df (pd.DataFrame): The dataset
        binary_columns (list): List of known binary columns (optional)
        verbose (bool): If True, prints the top 15 results

    Returns:
        results_df (pd.DataFrame): Sorted table of all test results
    """

    df = df.copy()
    df = df.dropna(how='all')  # Remove empty rows
    df.columns = df.columns.str.strip().str.replace(" ", "_")  # Standardize column names

    # Capitalize Yes/No in binary columns
    if binary_columns is not None:
        for col in binary_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.capitalize()

    # Detect column types
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    binary_cols = [col for col in df.columns if df[col].nunique() == 2 and df[col].dtype == 'object']
    categorical_cols = [col for col in df.columns if df[col].dtype == 'object' and df[col].nunique() > 2]

    results = []

    # Chi-squared tests (binary vs binary)
    for col1 in binary_cols:
        for col2 in binary_cols:
            if col1 != col2:
                contingency = pd.crosstab(df[col1], df[col2])
                chi2, p, _, _ = chi2_contingency(contingency)
                results.append({
                    "Test": "Chi-squared",
                    "Variable 1": col1,
                    "Variable 2": col2,
                    "p-value": p
                })

    # T-tests (numeric vs binary)
    for num_col in numeric_cols:
        for bin_col in binary_cols:
            groups = df[[num_col, bin_col]].dropna().groupby(bin_col)[num_col]
            if len(groups) == 2:
                group1, group2 = [g[1] for g in groups]
                t_stat, p = ttest_ind(group1, group2)
                results.append({
                    "Test": "T-test",
                    "Variable 1": num_col,
                    "Variable 2": bin_col,
                    "p-value": p
                })

    # ANOVA (numeric vs categorical)
    for num_col in numeric_cols:
        for cat_col in categorical_cols:
            groups = [g.dropna() for _, g in df[[num_col, cat_col]].dropna().groupby(cat_col)[num_col]]
            if len(groups) > 1:
                f_stat, p = f_oneway(*groups)
                results.append({
                    "Test": "ANOVA",
                    "Variable 1": num_col,
                    "Variable 2": cat_col,
                    "p-value": p
                })

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="p-value").reset_index(drop=True)

    if verbose:
        print("Top 15 statistically significant tests:")
        print(results_df.head(15))

    return results_df
