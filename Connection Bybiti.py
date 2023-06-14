import ccxt

exchange_id = "Bybit"
exchange_class = (getattr(ccxt, exchange_id))
exchange = exchange_class({
    "apikey" = "..."
    "apisecret" = "..."})
