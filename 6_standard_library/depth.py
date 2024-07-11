import requests

url = 'https://api-cloud.bitmart.com/contract/public/depth?symbol=BTCUSDT'
response = requests.get(url).json()
print(response)
