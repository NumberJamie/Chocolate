def iterate(values: list) -> tuple[int, int]:
    count, cals = 0, []
    for value in values:
        if value == '':
            cals.append(count)
            count = 0
            continue
        count += int(value)
    cals.sort()
    return cals[-1], sum(cals[-3:])


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer, answer2 = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    print(f'Part 2 Answer: {answer2}')

