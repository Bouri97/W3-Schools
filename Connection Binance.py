# Connect Binance API into Python

from binance.client import Client
client = Client("vP795eN3zGvFcT9iE30mDACus7Qa8TLHKQ51JxPbn4u7CtEkmCzinRal0bQAYxOj",
                "YsHJqtrb0eMadgr1Y8qI3Fq2ZjxSwNqmZZXk2qWi8RncNBF5X0DbWGGTX3buQKgy")

balance = client.get_asset_balance(asset="USDT")
print(balance)
