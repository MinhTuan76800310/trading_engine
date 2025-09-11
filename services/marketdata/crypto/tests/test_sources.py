import unittest
from services.marketdata.crypto.sources.simulator import SimulatorSource
from services.marketdata.crypto.schema import get_unified_schema

class TestSources(unittest.TestCase):
    def test_simulator(self):
        source = SimulatorSource()
        data = source.fetch_data(["BTC/USDT"])
        self.assertTrue(len(data) > 0)
        self.assertEqual(data[0]["symbol"], "BTC/USDT")
        self.assertEqual(data[0]["source"], "simulator")

if __name__ == "__main__":
    unittest.main()