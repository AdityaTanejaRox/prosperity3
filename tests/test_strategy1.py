import unittest
from src.algorithms.strategy1 import Trader

class TestStrategy1(unittest.TestCase):
    def setUp(self):
        self.trader = Trader()
    
    def test_run(self):
        # Mock a TradingState object as needed
        state = None  # Replace with an appropriate mock
        result = self.trader.run(state)
        self.assertIsInstance(result, dict)
