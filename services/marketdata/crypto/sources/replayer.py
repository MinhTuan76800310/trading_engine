import pandas as pd
import time
from .base import MarketDataSource
from ..schema import get_unified_schema

class ReplayerSource(MarketDataSource):
    def __init__(self, file_path, speed=1.0):
        self.data = pd.read_csv(file_path).sort_values('timestamp')
        self.index = 0
        self.speed = speed

    def start(self):
        pass

    def stop(self):
        pass

    def fetch_data(self, symbols):
        if self.index >= len(self.data):
            return []
        batch = self.data[self.data['symbol'].isin(symbols)].iloc[self.index:self.index+10]
        self.index += len(batch)
        data = []
        for _, row in batch.iterrows():
            data.append(get_unified_schema(
                symbol=row['symbol'],
                timestamp=int(row['timestamp']),
                open_price=float(row['open']),
                close_price=float(row['close']),
                high=float(row['high']),
                low=float(row['low']),
                volume=float(row['volume']),
                source="replayer"
            ))
        time.sleep(1 / self.speed)  # Control replay speed
        return data