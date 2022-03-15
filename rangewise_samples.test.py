import unittest
import rangewise_samples
import io
import sys

class RangewiseTest(unittest.TestCase):
  def test_infers_readings_as_per_range(self):
    self.assertTrue(rangewise_samples.infers_readings([4,5]) == "4-5, 2")
    self.assertTrue(rangewise_samples.infers_readings([3, 3, 5, 4, 10, 11, 12]) == "10-12, 3")
    self.assertTrue(rangewise_samples.infers_readings([3]) == "3-3, 1")
    self.assertTrue(rangewise_samples.infers_readings([3]) == False)
  
  def test_isSequenceOk(self):
    self.assertTrue(rangewise_samples.isSequenceOk([]) == False)

  def test_detectRange(self):
    self.assertTrue(rangewise_samples.detectRange([3, 3, 4, 5, 10, 11, 12]) == [[3,3,4,5],[10,11,12]])
  
  def test_convertCSVFormat(self):
    self.assertTrue(rangewise_samples.convertCSVFormat([3,3,4,5]) == "3-5, 4")

  def test_printOnConsole(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    rangewise_samples.printOnConsole('All is fine!')
    sys.stdout = sys.__stdout__
    print ('Captured', capturedOutput.getvalue())

if __name__ == '__main__': # pragma: no cover
  unittest.main()
