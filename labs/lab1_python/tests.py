import unittest
from roots_number import *

class TestRootsNumber(unittest.TestCase):

    def test(self):
        self.assertEqual(roots_number(1, 1, 1), 0)
        self.assertEqual(roots_number(1, 4, 4), 0)
        self.assertEqual(roots_number(1, -4, 4), 2)
        self.assertEqual(roots_number(0, 1, -1), 2)
        self.assertEqual(roots_number(1, -5, 6), 4)
        self.assertEqual(roots_number(1, 0, -1), 2)

if __name__ == "__main__":
    unittest.main()


