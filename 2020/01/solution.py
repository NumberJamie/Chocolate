from functools import reduce
from itertools import combinations


def iterate(values: list, amount: int) -> int:
    for value in combinations(values, amount):
        if sum(value) != 2020:
            continue
        count = reduce(lambda x, y: x * y, value)
        return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [int(line.strip()) for line in file.readlines()]
    answer = iterate(lines, 2)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, 3)
    print(f'Part 2 Answer: {answer}')

