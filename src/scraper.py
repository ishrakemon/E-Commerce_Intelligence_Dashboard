import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# --- CONFIGURATION ---
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGES = 50 
DATA_FOLDER = 'data'

def get_books():
    all_books = []
    
    for page in range(1, MAX_PAGES + 1):
        url = BASE_URL.format(page)
        print(f"Scraping Page {page}...")
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            books = soup.find_all("article", class_="product_pod")
            
            for book in books:
                item = {}
                
                # 1. Title
                image_tag = book.find("img")
                item['Title'] = image_tag['alt'] if image_tag else "Unknown"
                
                # 2. Price
                price_tag = book.find("p", class_="price_color")
                item['Price'] = price_tag.text.replace('£', '') if price_tag else "0.00"
                
                # 3. Rating
                star_tag = book.find("p", class_="star-rating")
                if star_tag:
                    item['Rating'] = star_tag['class'][1] 
                else:
                    item['Rating'] = "None"
                    
                # 4. Availability
                stock_tag = book.find("p", class_="instock availability")
                item['Availability'] = stock_tag.text.strip() if stock_tag else "Unknown"
                
                all_books.append(item)
                
            print(f"--> Found {len(books)} books on this page.")
            
        except Exception as e:
            print(f"Error on page {page}: {e}")
            
    return all_books

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("Starting Book Scraper...")
    data = get_books()
    
    if data:
        df = pd.DataFrame(data)
        
        # Save to 'data' folder
        filename = os.path.join(DATA_FOLDER, "books_data.csv")
        df.to_csv(filename, index=False)
        
        print(f"\nSUCCESS! Scraped {len(df)} books.")
        print(f"Data saved to: {filename}")
    else:
        print("Failed to scrape data.")