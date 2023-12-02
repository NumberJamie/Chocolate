import string


def iterate(values: list, grouped: bool = False) -> int:
    priorities, group, priority = [], [], string.ascii_letters
    for value in values:
        dupe = None
        group.append(set(char for char in value))
        if not grouped:
            first, second = value[0:len(value) // 2], value[len(value) // 2:]
            dupe = [letter for letter in first if letter in second][-1]
        if len(group) == 3 and grouped:
            dupe = next((char for char in priority if all(char in g for g in group)), None)
            group = []
        if dupe:
            priorities.append(priority.index(dupe) + 1)
    return sum(priorities)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    answer = iterate(lines)
    print(f'Part 1 Answer: {answer}')
    answer = iterate(lines, grouped=True)
    print(f'Part 2 Answer: {answer}')
