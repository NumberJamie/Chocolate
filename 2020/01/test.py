import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(iterate(line_list, 2), 514579)
        self.assertEqual(iterate(line_list, 3), 241861950)
