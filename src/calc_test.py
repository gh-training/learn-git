import unittest
from calc import add, sub

class TestStringMethods(unittest.TestCase):

    def test_add_2arg(self):
        # Make sure 3 + 4 = 7
        self.assertEqual(add(3, 4), 7, 'adding three and four')

    def test_add_3arg(self):
        self.assertEqual(add(3, 5, 2), 10, 'adding three, five and two')


if __name__ == '__main__':
    unittest.main()
