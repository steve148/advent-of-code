import re

Rules = dict[str, list[tuple[int, int]]]


def get_input():
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


def parse_rules(lines: list[str]) -> Rules:
    rules = {}
    for line in lines:
        m = re.search(r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$", line)
        if m:
            rules[m.group(1)] = [
                (int(m.group(2)), int(m.group(3))),
                (int(m.group(4)), int(m.group(5))),
            ]

    return rules


def parse_ticket(line: str) -> list[int]:
    return [int(s) for s in line.split(",")]


def parse_input(lines: list[str]) -> tuple:
    index_first_blank_line = lines.index("")
    rules_input = parse_rules(lines[:index_first_blank_line])

    lines = lines[index_first_blank_line + 1 :]
    index_second_blank_line = lines.index("")
    your_ticket_input = parse_ticket(lines[index_second_blank_line - 1])

    lines = lines[index_second_blank_line + 2 :]
    other_tickets_input = [parse_ticket(line) for line in lines]

    return (rules_input, your_ticket_input, other_tickets_input)


def number_could_be_valid(num: int, rules: Rules) -> bool:
    for _, valid_numbers in rules.items():
        for min_num, max_num in valid_numbers:
            if num >= min_num and num <= max_num:
                return True
    return False


def main() -> float:
    rules, your_ticket, other_tickets = parse_input(get_input())

    print(rules, your_ticket, other_tickets)
    ticket_numbers = [num for ticket in other_tickets for num in ticket]

    invalid_numbers = [
        num for num in ticket_numbers if not number_could_be_valid(num, rules)
    ]

    return sum(invalid_numbers)


print(main())
