import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

header = {
    "User-Agent": "my user agent info",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.zillow.com/oxford-ms/apartments/1-bedrooms/", headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all(class_="list-card-info")

