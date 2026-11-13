# If you already have a dataframe and want to append new data to it from a CSV file, use the following script.
import pandas as pd

# Read the first CSV into a dataframe
existing_df = pd.read_csv('existing_data.csv')

# Read the CSV file you want to append
new_data = pd.read_csv('new_data.csv')

# Append the new data to the existing DataFrame
combined_df = pd.concat([existing_df, new_data], ignore_index=True)

# Optionally, you can save the combined dataframe to a new CSV file
combined_df.to_csv('combined_data.csv', index=False)