import unittest

class TestStringMethods(unittest.TestCase):
    # assertEqual compares the first two items to ensure they're the same
    def test_upper(self):
        self.assertEqual('switch'.upper(), 'SWITCH')
    
    def test_isupper(self):
        self.assertTrue('SWITCH'.isupper())

if __name__ == '__main__':
    unittest.main()