def get_coords(value: str, x: int, y: int) -> tuple:
    x += 1 if value == '>' else 0
    x -= 1 if value == '<' else 0
    y += 1 if value == '^' else 0
    y -= 1 if value == 'v' else 0
    return x, y


def iterate(values: str, use_robot: bool = False) -> int:
    x1, y1, x2, y2, presents, visited = 0, 0, 0, 0, 1, {(0, 0)}
    for index, value in enumerate(values):
        if use_robot:
            x, y = get_coords(value, x2, y2) if index + 1 % 2 == 0 else get_coords(value, x1, y1)
            if index + 1 % 2 == 0:
                x1, y1 = x, y
            else:
                x2, y2 = x, y
        else:
            x, y = get_coords(value, x1, y1)
            x1, y1 = x, y
        if (x, y) in visited:
            continue
        visited.add((x, y))
        presents += 1
    return presents


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines[0])
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines[0], use_robot=True)
    print(f'Part 2 Answer: {answer}')
