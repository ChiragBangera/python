import requests
import json
from bs4 import BeautifulSoup


url = "https://www.homedepot.com/p/Glacier-Bay-Builders-4-in-Centerset-Double-Handle-Low-Arc-Bathroom-Faucet-in-Brushed-Nickel-HD67091W-6B04/309237982"


r = requests.get(url)

print(r.status_code)
