import re
import string

number_re = re.compile(r'\d+')


def has_special(index: int, values: list, match: re) -> bool:
    x, y = return_min_max(values[index], match)
    matrix = values[index][x:y]
    matrix += values[index - 1][x:y] if index - 1 > 0 else ''
    matrix += values[index + 1][x:y] if index + 1 < len(values) else ''
    return any(char in string.punctuation.replace('.', '') for char in matrix)


def return_min_max(value: str, match: re) -> tuple:
    x, y = match.start(), match.end()
    x -= 1 if x - 1 > 0 else 0
    y += 1 if y + 1 < len(value) else 0
    return x, y


def iterate(values: list) -> int:
    numbers = []
    for index, value in enumerate(values):
        matches = re.finditer(number_re, value)
        for match in matches:
            num = int(value[match.start():match.end()])
            if has_special(index, values, match):
                numbers.append(num)
    return sum(numbers)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
