def decode(code: str, one_bit: str) -> int:
    result = 0
    digit_val = 2 ** (len(code) - 1)

    for c in code:
        if c == one_bit:
            result += digit_val
        digit_val /= 2

    return int(result)


def p1(seats: list[str]) -> int:
    max_id = 0

    for seat in seats:
        row = decode(seat[:7], 'B')
        col = decode(seat[7:], 'R')
        id = row * 8 + col

        max_id = max(id, max_id)

    return max_id

def p2(seats: list[str]) -> int:
    seat_ids = set()

    for seat in seats:
        row = decode(seat[:7], 'B')
        col = decode(seat[7:], 'R')
        id = row * 8 + col

        seat_ids.add(id)

    min_id = min(seat_ids)
    max_id = max(seat_ids)

    for id in range(min_id, max_id + 1):
        if id not in seat_ids:
            return id


with open('input.txt') as f:
    seats = [line.rstrip() for line in f.readlines()]

print(p1(seats))
print(p2(seats))
