import os
import json
import requests

api_key = os.getenv("CMC_API_KEY")

url = "https://pro-api.coinmarketcap.com/v3/cryptocurrency/quotes/latest"

headers = {
    "X-CMC_PRO_API_KEY": api_key
}

params = {
    "symbol": "TRX",
    "convert": "USD"
}

res = requests.get(url, headers=headers, params=params)
data = res.json()

trx = data["data"]["TRX"]["quote"]["USD"]

output = {
    "price": trx["price"],
    "percent_change_24h": trx["percent_change_24h"],
    "market_cap": trx["market_cap"],
    "last_updated": trx["last_updated"]
}

with open("data.json", "w") as f:
    json.dump(output, f)
