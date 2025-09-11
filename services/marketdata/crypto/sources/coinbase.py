import ccxt
from .base import MarketDataSource
from ..schema import get_unified_schema
from ..config import Config

class CoinbaseSource(MarketDataSource):
    def __init__(self):
        self.exchange = ccxt.coinbasepro({
            'apiKey': Config.COINBASE_API_KEY,
            'secret': Config.COINBASE_API_SECRET
        })

    def start(self):
        pass  # No-op for polling-based source

    def stop(self):
        pass  # No-op

    def fetch_data(self, symbols):
        data = []
        for symbol in symbols:
            try:
                ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe='5m', limit=1)[0]
                timestamp, open_price, high, low, close_price, volume = ohlcv
                data.append(get_unified_schema(
                    symbol=symbol,
                    timestamp=int(timestamp),
                    open_price=float(open_price),
                    close_price=float(close_price),
                    high=float(high),
                    low=float(low),
                    volume=float(volume),
                    source="coinbase"
                ))
            except Exception as e:
                print(f"Coinbase error for {symbol}: {e}")
        return data