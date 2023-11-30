import pandas as pd

# File paths of the two CSV datasets
file_path1 = r"Data_Visualization\cases_pivoted.csv"
file_path2 = r"Data_Visualization\deaths_pivoted.csv"

# Read the CSV datasets into pandas DataFrames
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Get the common columns between the two datasets
common_columns = list(set(df1.columns) & set(df2.columns))

# Drop the common columns from df2 to avoid duplication
df2 = df2.drop(common_columns, axis=1)

# Combine the datasets, preserving columns with the same name
combined_df = pd.concat([df1, df2], axis=1)

# Save the combined dataset to a new CSV file
combined_df.to_csv("Data_Visualization/combined_dataset.csv", index=False)
