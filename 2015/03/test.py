import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_one(self):
        line_list = {
            '>': 2,
            '^>v<': 4,
            '^v^v^v^v^v': 2,
        }
        for key, value in line_list.items():
            self.assertEqual(iterate(key), value)

    def test_two(self):
        line_list = {
            '^v': 3,
            '^>v<': 3,
            '^v^v^v^v^v': 11,
        }
        for key, value in line_list.items():
            self.assertEqual(iterate(key, use_robot=True), value)
