# Outlier detection using z-scores
# This function will calculate z-scores for a column in a dataframe, and output the count of outliers.
import pandas as pd
import numpy as np
from scipy import stats

def count_and_print_extreme_z_scores(df, column_name):
    # Calculate the z-scores for the specified column
    z_scores = np.abs(stats.zscore(df[column_name]))

    # Count how many z-scores are greater than 3 or less than -3
    extreme_count = np.sum((z_scores > 3) | (z_scores < -3))

    print(f"Column '{column_name}': {extreme_count} z-scores are greater than 3 or less than -3")

# How to use this function:
# Assuming you have a DataFrame named 'data' and want to analyze the 'column_to_analyze'
# count_and_print_extreme_z_scores(data, 'column_to_analyze')
