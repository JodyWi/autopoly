import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("POLY_API_KEY")
BASE_URL = "https://api.polymarket.com"

headers = {
    "Authorization": f"Bearer {API_KEY}",
}

r = requests.get(f"{BASE_URL}/markets", headers=headers, timeout=10)
r.raise_for_status()

markets = r.json()
print(f"Fetched {len(markets)} markets")
print(markets[0])
