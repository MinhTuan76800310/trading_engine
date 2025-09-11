import websocket
import json
from .base import MarketDataSource
from ..schema import get_unified_schema
from ..config import Config

class BinanceSource(MarketDataSource):
    def __init__(self):
        self.ws = None
        self.data_queue = []  # Store incoming data
        self.symbols = Config.SYMBOLS

    def on_message(self, ws, message):
        data = json.loads(message)
        kline = data.get("k", {})
        if kline:
            symbol = data["s"]  # e.g., "BTCUSDT"
            unified = get_unified_schema(
                symbol=symbol.replace("USDT", "/USDT"),  # Normalize to "BTC/USDT"
                timestamp=kline["t"],  # Kline start time
                open_price=float(kline["o"]),
                close_price=float(kline["c"]),
                high=float(kline["h"]),
                low=float(kline["l"]),
                volume=float(kline["v"]),
                source="binance"
            )
            self.data_queue.append(unified)

    def on_error(self, ws, error):
        print(f"Binance WS error: {error}")

    def on_close(self, ws, *args):
        print("Binance WS closed")

    def on_open(self, ws):
        print("Binance WS opened")
        # Subscribe to Kline streams for all symbols
        for symbol in self.symbols:
            ws.send(json.dumps({
                "method": "SUBSCRIBE",
                "params": [f"{symbol.lower().replace('/', '')}@kline_5m"],
                "id": 1
            }))

    def start(self):
        self.ws = websocket.WebSocketApp(
            Config.BINANCE_WS_URL,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.ws.run_forever()

    def stop(self):
        if self.ws:
            self.ws.close()

    def fetch_data(self, symbols):
        # Return any queued data and clear queue
        data = self.data_queue[:]
        self.data_queue = []
        return data