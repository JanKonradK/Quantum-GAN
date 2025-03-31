import pandas as pd
import pyreadstat

# Specify the path to your XPT file
xpt_file_path = r'C:\\Users\\Konra\\Documents\\Projects\\QGAN Python 3.13.2\\BIX.xpt'

# Specify the path where you want to save the CSV file
csv_file_path = r'C:\\Users\Konra\\Documents\\Projects\\QGAN Python 3.13.2\\BIX.csv'

# Read the XPT file
df, meta = pyreadstat.read_xport(xpt_file_path)

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Data has been successfully converted to {csv_file_path}")