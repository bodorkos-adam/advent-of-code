import re


RE = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')


def p1(lines: list[str]) -> int:
    num_valid = 0

    for line in lines:
        match = RE.match(line)
        lo = int(match[1])
        hi = int(match[2])
        letter = match[3]
        password = match[4]

        if lo <= password.count(letter) <= hi:
            num_valid += 1

    return num_valid


def p2(lines: list[str]) -> int:
    num_valid = 0

    for line in lines:
        match = RE.match(line)
        p1 = int(match[1])
        p2 = int(match[2])
        letter = match[3]
        password = match[4]

        num_pos_matches = (password[p1 - 1] == letter) + (password[p2 - 1] == letter)

        if num_pos_matches == 1:
            num_valid += 1

    return num_valid


with open('input.txt') as f:
    lines = f.readlines()

print(p1(lines))
print(p2(lines))
