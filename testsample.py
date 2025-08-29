import requests

url = "http://127.0.0.1:5000/bfhl"
payload = {"data": ["M","25","226","78","Y","*"]}
res = requests.post(url, json=payload)

print(res.json())
