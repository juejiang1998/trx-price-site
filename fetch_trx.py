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

# v3 文档里 data 是数组，先取第一个资产
trx_info = data["data"][0]

# 有些返回里 quote 可能直接是对象，也可能被包成列表，做兼容处理
quote = trx_info["quote"]
if isinstance(quote, list):
    quote = quote[0]

usd = quote["USD"]
if isinstance(usd, list):
    usd = usd[0]

output = {
    "price": usd["price"],
    "percent_change_24h": usd["percent_change_24h"],
    "market_cap": usd["market_cap"],
    "volume_24h": usd["volume_24h"],
    "last_updated": usd["last_updated"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("TRX 数据更新成功")
