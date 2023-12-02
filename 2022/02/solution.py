def iterate(values: list, strategic: bool = False) -> int:
    loss, draw, win = (['A Z', 'B X', 'C Y'], ['A X', 'B Y', 'C Z'], ['A Y', 'B Z', 'C X'])
    score = 0
    for value in values:
        check_list = {'X': loss, 'Y': draw, 'Z': win}.get(value[-1])
        if strategic:
            value = next((check_list[index] for index, char in enumerate(check_list) if char[0] == value[0]), value)
        score += 'XYZ'.index(value[-1]) + 1
        score += 3 if value in draw else 0
        score += 6 if value in win else 0
    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, strategic=True)
    print(f'Part 2 Answer: {answer}')

