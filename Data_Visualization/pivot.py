import pandas as pd

file_name = 'Data_Visualization/Data/deaths.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_name)

# Specify the column name of the county IDs
county_id_column = 'CountyID'  # Change this to the actual column name in your CSV

# Use the `melt` function to reshape the DataFrame
melted_df = pd.melt(df, id_vars=county_id_column, var_name='Date', value_name='Deaths')

# Save the result DataFrame to a new CSV file
melted_df.to_csv('deaths_pivoted.csv', index=False)
