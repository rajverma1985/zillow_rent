import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

header = {
    "User-Agent": "my user agent info",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(os.environ.get("scrape_url"), headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all(class_="list-card-info")
print(data)
