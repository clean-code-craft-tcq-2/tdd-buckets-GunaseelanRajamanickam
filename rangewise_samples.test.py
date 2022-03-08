import unittest
import rangewise_samples

class RangewiseTest(unittest.TestCase):
  def test_infers_readings_as_per_range(self):
    self.assertTrue(rangewise_samples.infers_readings([4,5]) == "4-5, 2")

if __name__ == '__main__': # pragma: no cover
  unittest.main()
