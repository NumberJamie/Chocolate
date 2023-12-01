import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']
        self.assertEqual(iterate(line_list), (24000, 41000))
