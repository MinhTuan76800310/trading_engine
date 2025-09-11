import os

class Config:
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    MARKETDATA_TOPIC = "streams.marketdata"
    SYMBOLS = os.getenv("SYMBOLS", "BTC/USDT").split(",")
    BINANCE_WS_URL = "wss://stream.binance.com:9443/ws"
    COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
    COINBASE_API_SECRET = os.getenv("COINBASE_API_SECRET")
    POLL_INTERVAL = float(os.getenv("POLL_INTERVAL", "5"))  # Seconds