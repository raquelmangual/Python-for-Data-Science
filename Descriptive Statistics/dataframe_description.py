import pandas as pd

# Replace 'df' with the name of your dataframe

# Get a summary of the dataframe, including data types for the columns and the number of rows
print(df.info())

# Display the first five rows of the dataframe
print(df.head())

# Get descriptive statistics for the dataframe such as min, max, quartiles, etc.
print(df.describe())

# Get the column labels
print(df.columns)