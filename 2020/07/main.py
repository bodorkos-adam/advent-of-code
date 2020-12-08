import re


CONTAINER_RULE_RE = re.compile('^([a-z ]+) bags contain (.+)')
CONTENT_RULE_RE = re.compile('^(\d+) ([a-z ]+) bag')


def parse_content_rule(raw_rule: str) -> tuple[str, int]:
    match = CONTENT_RULE_RE.match(raw_rule)
    count = int(match[1])
    color = match[2]

    return color, count


def parse_container_rule(raw_rule: str) -> tuple[str, dict[str, int]]:
    match = CONTAINER_RULE_RE.match(raw_rule)
    color = match[1]
    rules = {}

    for raw_content_rule in match[2].split(', '):
        if not raw_content_rule.startswith('no'):
            content_color, count = parse_content_rule(raw_content_rule)
            rules[content_color] = count

    return color, rules


def parse_rules(raw_rules: list[str]) -> dict[str, dict[str, int]]:
    color_rules: dict[str, dict[str, int]] = {}

    for rule_str in raw_rules:
        color, rules = parse_container_rule(rule_str)
        color_rules[color] = rules

    return color_rules


def contains_recursive(color_rules: dict[str, dict[str, int]], container_color: str, color_to_find: str) -> bool:
    rules = color_rules[container_color]

    if color_to_find in rules:
        return True
    else:
        for color in rules:
            if contains_recursive(color_rules, color, color_to_find):
                return True

    return False


def count_recursive(color_rules: dict[str, dict[str, int]], container_color: str) -> int:
    total_bags_contained = 0

    for color, count in color_rules[container_color].items():
        total_bags_contained += count * (1 + count_recursive(color_rules, color))

    return total_bags_contained


def p1(color_rules: dict[str, dict[str, int]]) -> int:
    num_colors_containing_shiny_gold = 0

    for color in color_rules:
        if contains_recursive(color_rules, color, 'shiny gold'):
            num_colors_containing_shiny_gold += 1

    return num_colors_containing_shiny_gold


def p2(color_rules: dict[str, dict[str, int]]) -> int:
    return count_recursive(color_rules, 'shiny gold')


with open('input.txt') as f:
    raw_rules = [line.rstrip() for line in f.readlines()]

color_rules = parse_rules(raw_rules)

print(p1(color_rules))
print(p2(color_rules))
