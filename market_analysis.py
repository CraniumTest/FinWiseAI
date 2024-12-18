import requests
from bs4 import BeautifulSoup

def get_market_data(ticker: str) -> dict:
    response = requests.get(f"https://somefinancesite.com/{ticker}")
    soup = BeautifulSoup(response.content, "html.parser")
    # Parse the market data
    price = soup.find('span', {'class': 'price'}).text
    return {"ticker": ticker, "price": price}
