import pandas as pd

def convert_county_to_state(county_fips):
    # Extract the first two digits to get the state FIPS code
    state_fip = str(county_fips)[:-5]
    state_fip = int(state_fip)

    return state_fip

# Read the CSV file into a DataFrame
file_path = 'Data_Visualization/combined_dataset.csv'  # Replace with the path to your CSV file
output_file_path = 'Data_Visualization/combined_dataset_wStates.csv'  # Replace with the desired output path

df = pd.read_csv(file_path)

# Add a new column 'StateName' based on 'CountyID' column
df['StateID'] = df['CountyID'].apply(convert_county_to_state)

# Save the DataFrame with the added column to a new CSV file
df.to_csv(output_file_path, index=False)

print(f'DataFrame with StateName column saved to {output_file_path}')