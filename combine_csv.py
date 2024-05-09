import pandas as pd

# Paths to the CSV files
csv_file_path1 = 'dataset.csv'
csv_file_path2 = 'score_3.csv'

# Reading the CSV files
df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)

df1.fillna('N/A', inplace=True)
df2.fillna('N/A', inplace=True)

# Concatenating the DataFrames
# Use axis=0 to concatenate vertically (stack them on top of each other)
# Use axis=1 to concatenate horizontally (align them side by side)
combined_df = pd.concat([df1, df2], axis=1)

# Saving the combined DataFrame to a new CSV file
combined_df.to_csv('../ds3.csv', index=False)
