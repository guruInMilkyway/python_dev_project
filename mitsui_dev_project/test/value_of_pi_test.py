import unittest
from main.value_of_pi import get_value_of_pi


class TestValueOfPi(unittest.TestCase):
    def test_value_of_pi(self):

        expected_value_of_pi = 3.141592653589793238

        self.assertAlmostEqual(get_value_of_pi(2), expected_value_of_pi, 2)
        self.assertAlmostEqual(get_value_of_pi(3), expected_value_of_pi, 6)
        self.assertAlmostEqual(get_value_of_pi(4), expected_value_of_pi, 6)
        self.assertAlmostEqual(get_value_of_pi(6), expected_value_of_pi, 6)


if __name__ == '__main__':
    unittest.main()
