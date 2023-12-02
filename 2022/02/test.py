import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['A Y', 'B X', 'C Z']
        self.assertEqual(iterate(line_list), 15)
        self.assertEqual(iterate(line_list, True), 12)
