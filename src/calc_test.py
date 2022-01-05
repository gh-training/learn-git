import unittest
from calc import add, sub

class TestStringMethods(unittest.TestCase):

    def test_add_2arg(self):
        # Make sure 3 + 4 = 7
        self.assertEqual(add(3, 4), 7, 'adding three and four')

    def test_add_3arg(self):
        self.assertEqual(add(3, 5, 2), 10, 'adding three, five and two')

    def test_add_zeroes(self):
        self.assertEqual(add(0, 0, 0), 0 , 'adding zeroes together is zero')

    def test_sub_2arg(self):
        # Make sure 4 - 3 = 1
        self.assertEqual(sub(4, 3), 1, 'subtracting three from four')

    def test_sub_3arg(self):
        self.assertEqual(sub(4, 3, 1), 0, 'subtracting three from four')

    def test_sub_3argi_zero(self):
        self.assertEqual(sub(4, 3, 1), 0, 'subtracting three from four')

if __name__ == '__main__':
    unittest.main()
