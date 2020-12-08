import functools

with open('input.txt') as f:
    lines = f.readlines()

def count_trees(lines, num_advance_right, num_advance_down = 1):
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

res = [
    count_trees(lines, 1, 1),
    count_trees(lines, 3, 1),
    count_trees(lines, 5, 1),
    count_trees(lines, 7, 1),
    count_trees(lines, 1, 2)
]

print(functools.reduce(lambda a, b: a * b, res))
