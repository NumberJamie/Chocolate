import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
        self.assertEqual(iterate(line_list), 150)
        self.assertEqual(iterate(line_list, with_aim=True), 900)
