
#!/usr/bin/env python3

import unittest

class TestExampleText(unittest.TestCase):
    def test_firstname(self):
        with open('example.txt','r') as f:
            line = f.read()
            self.assertIn('Evan', line)

    def test_lastname(self):
        with open('example.txt', 'r') as f:
            line = f.read()
            self.assertIn('Dotterer', line)
            f.close() 
if __name__ == '__main__':
    unittest.main()