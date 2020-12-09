from typing import Optional


def is_sum(number: int, numbers: list[int]) -> bool:
    count = len(numbers)

    for i, _ in enumerate(numbers):
        for j in range(i + 1, count):
            if numbers[i] + numbers[j] == number:
                return True

    return False


def find_invalid_number(numbers: list[int], how_many_to_check: int) -> int:
    for i in range(how_many_to_check, len(numbers)):
        prev_numbers = numbers[i - how_many_to_check : i]

        if not is_sum(numbers[i], prev_numbers):
            return numbers[i]


def p1(numbers: list[int]) -> int:
    return find_invalid_number(numbers, 25)


def p2(numbers: list[int]) -> int:
    invalid_number = find_invalid_number(numbers, 25)

    for i in range(len(numbers)):
        total = numbers[i]

        for j in range(i + 1, len(numbers)):
            total += numbers[j]

            if total > invalid_number:
                break
            elif total == invalid_number:
                contiguous_range = numbers[i : j + 1]

                return min(contiguous_range) + max(contiguous_range)


with open('input.txt') as f:
    numbers = [int(line) for line in f.readlines()]

print(p1(numbers))
print(p2(numbers))
