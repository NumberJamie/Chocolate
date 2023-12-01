import unittest

from solution import trebuchet, convert, iterate


class TestSolution(unittest.TestCase):
    def test_one(self):
        line_list, lines = [], {
            '1abc2': 12,
            'pqr3stu8vwx': 38,
            'a1b2c3d4e5f': 15,
            'treb7uchet': 77
        }
        for key, value in lines.items():
            line_list.append(key)
            self.assertEqual(trebuchet(key), value)
        self.assertEqual(iterate(line_list), 142)

    def test_two(self):
        line_list, lines = [], {
            'two1nine': 29,
            'eightwothree': 83,
            'abcone2threexyz': 13,
            'xtwone3four': 24,
            '4nineeightseven2': 42,
            'zoneight234': 14,
            '7pqrstsixteen': 76
        }
        for key, value in lines.items():
            key = convert(key)
            line_list.append(key)
            self.assertEqual(trebuchet(key), value)
        self.assertEqual(iterate(line_list), 281)
