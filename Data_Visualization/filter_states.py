import pandas as pd

# Read the CSV file
df = pd.read_csv('/C:/Users/biehl/CovidDataVis/Data_Visualization/filter_states.csv')

# Filter rows where CountyID is less than 54000
df = df[df['CountyID'] < 54000]

# Save the filtered data to a new CSV file
df.to_csv('/C:/Users/biehl/CovidDataVis/Data_Visualization/filtered_data.csv', index=False)
