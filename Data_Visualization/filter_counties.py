import pandas as pd

# Read the CSV file
df = pd.read_csv('Data_Visualization/combined_dataset.csv')

# Filter rows where CountyID is less than 54000
df = df[df['CountyID'] < 56000]

# Save the filtered data to a new CSV file
df.to_csv('Data_Visualization/filtered_dataset.csv', index=False)
