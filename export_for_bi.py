import pandas as pd
import os
from sqlalchemy import create_engine

# Define paths
db_path = os.path.join('data', 'competitor_data.db')
output_csv_path = os.path.join('data', 'powerbi_data.csv')

# Connect to the database
engine = create_engine(f'sqlite:///{db_path}')

try:
    # Read the clean data
    df = pd.read_sql("SELECT * FROM books", engine)

    # Save to a new CSV in the data folder
    df.to_csv(output_csv_path, index=False)
    print(f"SUCCESS! Created '{output_csv_path}' for Power BI.")

except Exception as e:
    print(f"Error: {e}")