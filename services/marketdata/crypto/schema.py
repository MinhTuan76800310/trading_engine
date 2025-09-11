def get_unified_schema(symbol, timestamp, open_price, close_price, high, low, volume, source):
    """Return a dict in unified schema."""
    return {
        "symbol": symbol,          # e.g., "BTC/USDT"
        "timestamp": timestamp,    # Unix timestamp in ms
        "open": open_price,       # Open price for the Kline
        "close": close_price,     # Close price
        "high": high,             # High price
        "low": low,               # Low price
        "volume": volume,         # Volume
        "source": source          # e.g., "binance", "coinbase", "simulator", "replayer"
    }