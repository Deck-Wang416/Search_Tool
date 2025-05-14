import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"

def crawl_website(delay=6):
    visited = set()
    pages = {}
    next_url = "/"
    
    while next_url:
        full_url = BASE_URL + next_url
        print(f"Crawling: {full_url}")
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Save text content of the page (for simplicity, we include visible text only)
        text = soup.get_text(separator=' ', strip=True)
        pages[full_url] = text
        visited.add(full_url)
        
        # Find the next page
        next_btn = soup.select_one("li.next > a")
        next_url = next_btn['href'] if next_btn else None

        if next_url:
            time.sleep(delay)
    
    return pages  # Dict: {url: full_text}
