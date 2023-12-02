def iterate(values: list, old_policy: bool = True) -> int:
    count = 0
    for value in values:
        value = value.replace(':', '').split(' ')
        lower, upper = [int(v) for v in value[0].split('-')]
        if old_policy:
            count += 1 if lower <= int(value[-1].count(value[1])) <= upper else 0
            continue
        if (value[-1][lower - 1] == value[1]) != (value[-1][upper - 1] == value[1]):
            count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, old_policy=False)
    print(f'Part 2 Answer: {answer}')

