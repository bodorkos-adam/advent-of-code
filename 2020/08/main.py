def parse_line(line: str) -> tuple[str, int]:
    parts = line.split(' ')
    return parts[0], int(parts[1])


def execute(instructions: list[tuple[str, int]]) -> tuple[bool, int]:
    acc = 0
    i = 0
    indices_already_executed = set[int]()

    while i not in indices_already_executed:
        indices_already_executed.add(i)
        instruction, number = instructions[i]

        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            acc += number
            i += 1
        elif instruction == 'jmp':
            i += number

        if i == len(instructions):
            return True, acc

    return False, acc


def p1(instructions: list[tuple[str, int]]) -> int:
    terminates, acc = execute(instructions)
    return acc


def p2(instructions: list[tuple[str, int]]) -> int:
    for i in range(len(instructions)):
        instruction, number = instructions[i]

        if instruction == 'nop':
            instructions[i] = 'jmp', number

            terminates, acc = execute(instructions)
            if terminates:
                return acc

            instructions[i] = 'nop', number

        elif instruction == 'jmp':
            instructions[i] = 'nop', number

            terminates, acc = execute(instructions)
            if terminates:
                return acc

            instructions[i] = 'jmp', number


with open('input.txt') as f:
    instructions = [parse_line(line) for line in f.readlines()]

print(p1(instructions))
print(p2(instructions))
