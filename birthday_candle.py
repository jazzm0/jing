import unittest


# https://www.hackerrank.com/challenges/birthday-cake-candles/

def birthday_candle(arr):
    return "unsolved"


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(birthday_candle([3, 1, 2, 3]), 2)

    def test_a(self):
        self.assertEqual(birthday_candle([1, 2, 3, 6, 7, 7, 8]), 2)


if __name__ == '__main__':
    unittest.main()
