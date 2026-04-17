import os
import json
import requests

api_key = os.getenv("CMC_API_KEY")

if not api_key:
    raise Exception("没有读取到 CMC_API_KEY，请检查 GitHub Secrets")

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
quote = trx_info["quote"][0]

output = {
    "price": quote["price"],
    "percent_change_24h": quote["percent_change_24h"],
    "market_cap": quote["market_cap"],
    "volume_24h": quote["volume_24h"],
    "last_updated": quote["last_updated"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("TRX 数据更新成功")
