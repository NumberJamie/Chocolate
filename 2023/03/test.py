import unittest

from solution import iterate


class TestSolution(unittest.TestCase):
    def test_all(self):
        line_list = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....',
                     '......755.', '...$.*....', '.664.598..']
        self.assertEqual(4361, iterate(line_list))
