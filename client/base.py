import requests

headers = {'Accept': 'application/json'}

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', headers=headers)

print(f"Response: {r.json()}")