def oxygen(values: list, counts: list) -> int:
    pass


def iterate(values: list) -> int:
    counts = [[0, 0] for _ in values[0]]
    for value in values:
        for index, char in enumerate(value):
            counts[index][char == '0'] += 1
    gamma = ''.join('0' if count[0] > count[1] else '1' for count in counts)
    epsilon = ''.join('1' if count[0] > count[1] else '0' for count in counts)
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
