import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001',
                     '00010', '01010']
        self.assertEqual(iterate(line_list), 198)
