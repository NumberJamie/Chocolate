def is_possible(value: list) -> int:
    maxes = {'red': 12, 'green': 13, 'blue': 14}
    identifier, possible = 0, True
    for item in [v.strip().split(' ') for v in value]:
        if not item[0].isnumeric():
            identifier = int(item[-1])
            continue
        if int(item[0]) > maxes.get(item[-1]):
            possible = False
    return identifier if possible else 0


def fewest(value: list) -> int:
    r, g, b = 0, 0, 0
    for item in [v.strip().split(' ') for v in value]:
        if not item[0].isnumeric():
            continue
        r = int(item[0]) if item[-1] == 'red' and int(item[0]) > r else r
        g = int(item[0]) if item[-1] == 'green' and int(item[0]) > g else g
        b = int(item[0]) if item[-1] == 'blue' and int(item[0]) > b else b
    return r * g * b


def iterate(values: list, lowest: bool = False) -> int:
    possible_games = 0
    for value in values:
        value = value.replace(':', ';').replace(',', ';').split(';')
        if not lowest:
            possible_games += is_possible(value)
            continue
        possible_games += fewest(value)
    return possible_games


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, lowest=True)
    print(f'Part 2 Answer: {answer}')
