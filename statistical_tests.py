import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind, f_oneway

def run_statistical_tests(df, binary_columns=None, alpha=0.05, verbose=True):
    """
    Run Chi-squared, T-test, and ANOVA tests, and print interpretations for statistically significant results.
    """
    df = df.copy()
    df = df.dropna(how='all')
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    if binary_columns is not None:
        for col in binary_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.capitalize()

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    binary_cols = [col for col in df.columns if df[col].nunique() == 2 and df[col].dtype == 'object']
    categorical_cols = [col for col in df.columns if df[col].dtype == 'object' and df[col].nunique() > 2]

    results = []

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
        print("🔍 תוצאות מובהקות סטטיסטית (p < {:.3f}):\n".format(alpha))
        for _, row in results_df.iterrows():
            if row['p-value'] < alpha:
                explanation = ""
                if row['Test'] == 'Chi-squared':
                    explanation = f"קיים קשר מובהק בין המשתנים הבינאריים '{row['Variable 1']}' ו-'{row['Variable 2']}'"
                elif row['Test'] == 'T-test':
                    explanation = f"הממוצע של '{row['Variable 1']}' שונה באופן מובהק בין קבוצות '{row['Variable 2']}'"
                elif row['Test'] == 'ANOVA':
                    explanation = f"הממוצע של '{row['Variable 1']}' שונה בין רמות שונות של '{row['Variable 2']}'"
                print(f"- {row['Test']}: {explanation} (p = {row['p-value']:.3e})")

    return results_df
