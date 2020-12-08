from functools import reduce


def count_trees(lines: list[str], num_advance_right: int, num_advance_down: int) -> int:
    num_trees = 0
    num_lines = len(lines)
    num_cols = len(lines[0]) - 1
    row = 0
    col = 0

    while row < num_lines:
        if lines[row][col] == '#':
            num_trees += 1
        row += num_advance_down
        col = (col + num_advance_right) % num_cols

    return num_trees


def p1(lines: list[str]) -> int:
    return count_trees(lines, 3, 1)


def p2(lines: list[str]) -> int:
    return reduce(lambda a, b: a * b, [
        count_trees(lines, 1, 1),
        count_trees(lines, 3, 1),
        count_trees(lines, 5, 1),
        count_trees(lines, 7, 1),
        count_trees(lines, 1, 2)
    ])


with open('input.txt') as f:
    lines = f.readlines()

print(p1(lines))
print(p2(lines))
