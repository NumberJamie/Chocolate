import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']
        self.assertEqual(iterate(line_list), 2)
        self.assertEqual(iterate(line_list, at_all=True), 4)
