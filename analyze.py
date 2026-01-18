import pandas as pd
import os
from sqlalchemy import create_engine

db_path = os.path.join('data', 'competitor_data.db')
output_csv_path = os.path.join('output', 'hidden_gems_report.csv')

engine = create_engine(f'sqlite:///{db_path}')

print("--- FULL MARKET ANALYSIS (1000 BOOKS) ---\n")

# MARKET OVERVIEW
sql_overview = """
SELECT 
    COUNT(*) as Total_Books,
    AVG(Price) as Avg_Price,
    MIN(Price) as Cheapest,
    MAX(Price) as Most_Expensive
FROM books;
"""
print("1. MARKET OVERVIEW:")
print(pd.read_sql(sql_overview, engine))
print("-" * 30)

# PRICE BY RATING
sql_rating = """
SELECT 
    Rating,
    COUNT(*) as Book_Count,
    ROUND(AVG(Price), 2) as Avg_Price
FROM books
GROUP BY Rating
ORDER BY Rating_Num DESC;
"""
print("2. PRICE VS RATING:")
print(pd.read_sql(sql_rating, engine))
print("-" * 30)

# EXPORT ALL HIDDEN GEMS
print("3. GENERATING 'HIDDEN GEMS' REPORT...")

sql_gems = """
SELECT Title, Price, Availability, Rating
FROM books
WHERE Rating = 'Five' AND Price < 20
ORDER BY Price ASC;
"""

# Execute and save to output folder
df_gems = pd.read_sql(sql_gems, engine)
df_gems.to_csv(output_csv_path, index=False)

print(f"--> SUCCESS! Found {len(df_gems)} books that are 5-Stars & Under £20.")
print(f"--> Saved full list to: '{output_csv_path}'")