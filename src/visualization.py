import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

DATA_FOLDER = 'data'
OUTPUT_FOLDER = 'output'

db_path = os.path.join(DATA_FOLDER, 'competitor_data.db')
engine = create_engine(f'sqlite:///{db_path}')

print("--> Fetching data for visualization...")

try:
    df_price = pd.read_sql("SELECT Rating, AVG(Price) as Avg_Price FROM books GROUP BY Rating", engine)

    rating_order = ['One', 'Two', 'Three', 'Four', 'Five']
    df_price['Rating'] = pd.Categorical(df_price['Rating'], categories=rating_order, ordered=True)
    df_price = df_price.sort_values('Rating')

    # Create the Dashboard (2 Charts)
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
    bars = plt.bar(df_price['Rating'], df_price['Avg_Price'], color=colors)
    plt.title('Average Price by Star Rating')
    plt.xlabel('Star Rating')
    plt.ylabel('Price (£)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add price labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'£{yval:.2f}', ha='center', va='bottom')

    df_stock = pd.read_sql("SELECT Availability, COUNT(*) as Count FROM books GROUP BY Availability", engine)

    plt.subplot(1, 2, 2)
    plt.pie(df_stock['Count'], labels=df_stock['Availability'], autopct='%1.1f%%', startangle=90, colors=['#ffcc99', '#66b3ff'])
    plt.title('Inventory Status')

    plt.tight_layout()
    
    # Save to 'output' folder
    save_path = os.path.join(OUTPUT_FOLDER, 'project_dashboard.png')
    plt.savefig(save_path, dpi=300)
    
    print(f"--> SUCCESS! Dashboard saved to '{save_path}'")
    plt.show()

except Exception as e:
    print(f"Error: {e}")