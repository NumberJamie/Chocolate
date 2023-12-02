def iterate(values: list, at_all: bool = False) -> int:
    count = 0
    for value in values:
        value = list(map(int, value.replace('-', ',').split(',')))
        if (value[0] <= value[2] <= value[3] <= value[1] or value[2] <= value[0] <= value[1] <= value[3]) and not at_all:
            count += 1
        if (value[0] <= value[3] and value[1] >= value[2]) and at_all:
            count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, at_all=True)
    print(f'Part 2 Answer: {answer}')
