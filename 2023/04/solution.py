def iterate(values: list) -> int:
    points = 0
    for value in values:
        value = value.replace(': ', '|').split('|')[1::]
        for i, item in enumerate(value):
            value[i] = [int(num) for num in item.strip().split()]
        point = 0
        for item in value[0]:
            if item not in value[-1]:
                continue
            if point == 0:
                point = 1
                continue
            point *= 2
        points += point
    return points


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
