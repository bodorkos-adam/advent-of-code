def p1(numbers: list[int]) -> int:
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i+1:]:
            sum2 = num1 + num2

            if sum2 > 2020:
                break

            if sum2 == 2020:
                return num1 * num2

def p2(numbers: list[int]) -> int:
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i+1:]):
            sum2 = num1 + num2

            if sum2 > 2020:
                break

            for num3 in numbers[j+1:]:
                sum3 = sum2 + num3

                if sum3 > 2020:
                    break

                if sum3 == 2020:
                    return num1 * num2 * num3


with open('input.txt') as f:
    numbers = sorted([int(x) for x in f.readlines()])

print(p1(numbers))
print(p2(numbers))
