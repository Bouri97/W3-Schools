import ccxt

exchange_id = "Bybit"
exchange_class = (getattr(ccxt, exchange_id))
exchange = exchange_class({
    "apikey" = "mGgNwDLzmzgNz75y7J"
    "apisecret" = "JJEKR9RSg2acYL7ZUndfZaAA2y4LY4vNhDA5"})
