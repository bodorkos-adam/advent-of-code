def find_chain(adapters: set[int], current_adapter: int, num_jumps: list[int]) -> tuple[bool, list[int]]:
    for i in range(1, 4):
        if current_adapter + i in adapters:
            num_jumps[i - 1] += 1
            uses_all, num_jumps = find_chain(adapters, current_adapter + i, num_jumps)

            if uses_all:
                return True, num_jumps

    if current_adapter == max(adapters):
        num_jumps[2] += 1
        return True, num_jumps

    return False, num_jumps


def p1(adapters: set[int]) -> int:
    _, num_jumps = find_chain(adapters, 0, [0, 0, 0])
    return num_jumps[0] * num_jumps[2]


with open('input.txt') as f:
    adapters = set([int(line) for line in f.readlines()])

print(p1(adapters))
