import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
        self.assertEqual(iterate(line_list), 7)
        self.assertEqual(iterate(line_list, three_measurement=True), 5)
