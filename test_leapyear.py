import unittest
import leapyear

class TestCase(unittest.TestCase):
  def test_good1(self):
    self.assertEqual(leapyear.leap(2020), "2020 is a leap year")
def test_good2(self):
self.assertEqual(leapyear.leap(2000), "2000 is a leap year")

if __name__ == "__main__":
    unittest.main(verbosity=2)