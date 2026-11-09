import pandas as pd

# Create the sample DataFrame (replace this with your own DataFrame)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Salary': [50000, 60000, 75000, 80000, 90000, 95000, 100000, 110000, 120000, 130000]
}

df = pd.DataFrame(data)

# Display summary statistics for the "Age" column
print(df['Age'].describe())

# Display individual summary statistics directly
print(df['Age'].mean())    # Mean
print(df['Age'].median())  # Median
print(df['Age'].std())     # Standard deviation
print(df['Age'].min())     # Minimum
print(df['Age'].max())     # Maximum
print(df['Age'].mode())    # Mode
