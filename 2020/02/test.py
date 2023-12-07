import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        self.assertEqual(2, iterate(line_list))
        self.assertEqual(1, iterate(line_list, old_policy=False))
