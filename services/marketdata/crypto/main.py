import sys
import time
import threading
from .sources.binance import BinanceSource
from .sources.coinbase import CoinbaseSource
from .sources.simulator import SimulatorSource
from .sources.replayer import ReplayerSource
from .publisher import MarketDataPublisher
from .config import Config

def run_source(source):
    """Run WebSocket-based source in a separate thread."""
    source.start()

def main(source_type, file_path=None):
    publisher = MarketDataPublisher()
    symbols = Config.SYMBOLS

    if source_type == "binance":
        source = BinanceSource()
        # Run WebSocket in a separate thread
        threading.Thread(target=run_source, args=(source,), daemon=True).start()
    elif source_type == "coinbase":
        source = CoinbaseSource()
        source.start()
    elif source_type == "simulator":
        source = SimulatorSource()
        source.start()
    elif source_type == "replayer":
        if not file_path:
            raise ValueError("Replayer requires a file path")
        source = ReplayerSource(file_path, speed=1.0)
        source.start()
    else:
        raise ValueError("Invalid source type")

    try:
        while True:
            data = source.fetch_data(symbols)
            if data:
                publisher.publish(data)
                print(f"Published: {data}")
            time.sleep(Config.POLL_INTERVAL)
    except KeyboardInterrupt:
        source.stop()
        print("Stopped")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_type> [file_path for replayer]")
        sys.exit(1)
    source_type = sys.argv[1]
    file_path = sys.argv[2] if len(sys.argv) > 2 else None
    main(source_type, file_path)