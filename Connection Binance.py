# Connect Binance API into Python

from binance.client import Client
client = Client("v...j",
                "Y..y")

balance = client.get_asset_balance(asset="USDT")
print(balance)
