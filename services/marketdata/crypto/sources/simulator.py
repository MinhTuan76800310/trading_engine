import time
import numpy as np
from .base import MarketDataSource
from ..schema import get_unified_schema
from ..config import Config

class SimulatorSource(MarketDataSource):
    def __init__(self):
        self.base_prices = {s: 10000 for s in Config.SYMBOLS}  # Arbitrary starting prices
        self.last_timestamp = int(time.time() * 1000)

    def start(self):
        pass

    def stop(self):
        pass

    def fetch_data(self, symbols):
        data = []
        self.last_timestamp += 5 * 60 * 1000  # Simulate 5-minute intervals
        for symbol in symbols:
            price = self.base_prices[symbol] * (1 + np.random.normal(0, 0.01))
            self.base_prices[symbol] = price
            data.append(get_unified_schema(
                symbol=symbol,
                timestamp=self.last_timestamp,
                open_price=price * 0.99,
                close_price=price,
                high=price * 1.01,
                low=price * 0.98,
                volume=np.random.uniform(50, 200),
                source="simulator"
            ))
        return data