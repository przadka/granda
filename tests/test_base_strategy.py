import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from granda.base_strategy import BaseStrategy

class ConcreteStrategy(BaseStrategy):
    def process_data(self, data):
        return data

class TestBaseStrategy(unittest.TestCase):
    def test_process_data(self):
        strategy = ConcreteStrategy()
        result = strategy.process_data([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
