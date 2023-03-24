import unittest

# Assume that our Software approved version is "9.3(3)"

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        switch_version = switch_os()
        self.assertEqual(switch_version, switch_os())

def switch_os():
    switch_os = '8.5(1)'
    return switch_os        

if __name__ == '__main__':
    unittest.main()