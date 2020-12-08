def p1(groups: list[list[str]]) -> int:
    total = 0

    for group in groups:
        yes_answers = set()

        for person in group:
            for yes_answer in person:
                yes_answers.add(yes_answer)

        total += len(yes_answers)

    return total


def p2(groups: list[list[str]]) -> int:
    total = 0

    for group in groups:
        yes_answer_counts = {}

        for person in group:
            for yes_answer in person:
                yes_answer_counts[yes_answer] = yes_answer_counts.get(yes_answer, 0) + 1

        total += sum(1 for k,v in yes_answer_counts.items() if v == len(group))

    return total


with open('input.txt') as f:
    groups = [g.rstrip().split('\n') for g in f.read().split('\n\n')]

print(p1(groups))
print(p2(groups))
