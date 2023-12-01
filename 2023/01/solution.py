def convert(token: str) -> str:
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for key, value in numbers.items():
        token = token.replace(key, key[0] + str(value) + key[-1])
    return token


def trebuchet(token: str) -> int:
    return int(next(filter(str.isdigit, token)) + next(filter(str.isdigit, token[::-1])))


def iterate(values: list, do_convert: bool = False) -> int:
    initial = 0
    for value in values:
        if do_convert:
            value = convert(value)
        initial += trebuchet(value)
    return initial


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, True)
    print(f'Part 2 Answer: {answer}')
