def find_chain(adapters: set[int], current_adapter: int, j1: int, j2: int, j3: int) -> tuple[bool, int, int, int]:
    if current_adapter + 1 in adapters:
        j1 += 1
        uses_all, j1, j2, j3 = find_chain(adapters, current_adapter + 1, j1, j2, j3)

        if uses_all:
            return True, j1, j2, j3

    if current_adapter + 2 in adapters:
        j2 += 1
        uses_all, j1, j2, j3 = find_chain(adapters, current_adapter + 2, j1, j2, j3)

        if uses_all:
            return True, j1, j2, j3

    if current_adapter + 3 in adapters:
        j3 += 1
        uses_all, j1, j2, j3 = find_chain(adapters, current_adapter + 3, j1, j2, j3)

        if uses_all:
            return True, j1, j2, j3

    if current_adapter == max(adapters):
        j3 += 1
        return True, j1, j2, j3

    return False, j1, j2, j3

def p1(adapters: set[int]) -> int:
    uses_all, j1, j2, j3 = find_chain(adapters, 0, 0, 0, 0)

    return j1 * j3


with open('input.txt') as f:
    adapters = set([int(line) for line in f.readlines()])

print(p1(adapters))
