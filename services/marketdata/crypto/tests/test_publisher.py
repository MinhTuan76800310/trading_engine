import unittest
from services.marketdata.crypto.publisher import MarketDataPublisher
from services.marketdata.crypto.schema import get_unified_schema

class TestPublisher(unittest.TestCase):
    def test_publish(self):
        publisher = MarketDataPublisher()
        data = [get_unified_schema("BTC/USDT", 1699999999, 45000, 45000, 45100, 44900, 100, "test")]
        try:
            publisher.publish(data)
        except Exception as e:
            self.fail(f"Publish failed: {e}")

if __name__ == "__main__":
    unittest.main()