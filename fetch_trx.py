import os
import json
import requests

api_key = os.getenv("CMC_API_KEY")

url = "https://pro-api.coinmarketcap.com/v3/cryptocurrency/quotes/latest"

headers = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": api_key
}

params = {
    "symbol": "TRX",
    "convert": "USD"
}

res = requests.get(url, headers=headers, params=params, timeout=30)
res.raise_for_status()

data = res.json()

trx_info = data["data"][0]
usd = trx_info["quote"]["USD"]

output = {
    "price": usd["price"],
    "percent_change_24h": usd["percent_change_24h"],
    "market_cap": usd["market_cap"],
    "last_updated": usd["last_updated"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("TRX 数据更新成功")
