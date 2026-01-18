import pandas as pd
import os
from sqlalchemy import create_engine

# Define paths
db_path = os.path.join('data', 'competitor_data.db')
csv_path = os.path.join('data', 'books_data.csv')

# Connect to database
engine = create_engine(f'sqlite:///{db_path}')

try:
    print("--> Reading CSV file...")
    # This reads the file created by scraper.py
    df = pd.read_csv(csv_path)

    # Clean data
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    
    rating_map = {
        'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
        'None': 0
    }
    df['Rating_Num'] = df['Rating'].map(rating_map)

    # Save to SQL
    df.to_sql('books', engine, if_exists='replace', index=False)

    print(f"\nSUCCESS! Loaded {len(df)} rows into '{db_path}'.")

except Exception as e:
    print(f"Error: {e}")