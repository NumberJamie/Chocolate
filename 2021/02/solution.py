def iterate(values: list, with_aim: bool = False) -> int:
    horizontal, depth, aim = 0, 0, 0
    for value in values:
        value = value.split(' ')
        if value[0] == 'forward':
            horizontal += int(value[-1])
            depth += (int(value[-1]) * aim) if with_aim else 0
        if value[0] == 'up':
            depth += int(value[-1]) if not with_aim else 0
            aim -= int(value[-1])
        if value[0] == 'down':
            depth += int(value[-1]) if not with_aim else 0
            aim += int(value[-1])
    return horizontal * depth


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, with_aim=True)
    print(f'Part 2 Answer: {answer}')
