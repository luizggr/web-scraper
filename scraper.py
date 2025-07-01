import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    # page url
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    
    # parse HTML
    soup = BeautifulSoup(response.text, "lxml")
    
    # extraction
    quotes = []
    authors = []
    
    for quote in soup.find_all("div", class_="quote"):
        quotes.append(quote.find("span", class_="text").text)
        authors.append(quote.find("small", class_="author").text)
        
    # Store data frame and save as CSV
    df = pd.DataFrame({"Quote": quotes, "Authors": authors})
    df.to_csv("quotes.csv", index=False)
    print("Scraping complete!\n Data saved to 'quotes.csv'.")
    
if __name__ == "__main__":
    scrape_quotes()