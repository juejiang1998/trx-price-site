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

print("完整返回：")
print(json.dumps(data, ensure_ascii=False, indent=2))

# 先故意停在这里，先看真实结构
raise Exception("先看上面打印出来的数据结构")
