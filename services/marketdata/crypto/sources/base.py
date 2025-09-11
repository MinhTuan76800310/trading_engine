from abc import ABC, abstractmethod

class MarketDataSource(ABC):
    @abstractmethod
    def fetch_data(self, symbols):
        """Fetch data for given symbols. Yield or return list of dicts in unified schema."""
        pass

    @abstractmethod
    def start(self):
        """Start the source (e.g., connect to WebSocket)."""
        pass

    @abstractmethod
    def stop(self):
        """Stop the source (e.g., close WebSocket)."""
        pass