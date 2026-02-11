import unittest
from my_sum import sum

class testSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([5,5,5]), 15)

if __name__ =='__main__':
    unittest.main()