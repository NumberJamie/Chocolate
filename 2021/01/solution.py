def iterate(values: list, three_measurement: bool = False) -> int:
    count, previous, values = 0, None, [int(value) for value in values]
    for index, value in enumerate(values):
        if three_measurement:
            value = sum(values[index:index + 3])
        if previous is not None:
            if len(values[index:index + 3]) != 3 and three_measurement:
                continue
            count += 1 if value > previous else 0
        previous = value
        continue
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, three_measurement=True)
    print(f'Part 1 Answer: {answer}')

