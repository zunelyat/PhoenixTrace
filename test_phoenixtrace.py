# test_phoenixtrace.py
"""
Tests for PhoenixTrace module.
"""

import unittest
from phoenixtrace import PhoenixTrace

class TestPhoenixTrace(unittest.TestCase):
    """Test cases for PhoenixTrace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PhoenixTrace()
        self.assertIsInstance(instance, PhoenixTrace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PhoenixTrace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
