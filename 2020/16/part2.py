import functools
import re

Ticket = list[int]
Tickets = list[Ticket]
Constraints = list[tuple[int, int]]
Rules = dict[str, Constraints]
RulesToColumns = dict[str, list[int]]


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


def parse_ticket(line: str) -> Ticket:
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


def number_valid_for_constraints(num: int, constraints: Constraints) -> bool:
    for min_num, max_num in constraints:
        if num >= min_num and num <= max_num:
            return True
    return False


def number_could_be_valid(num: int, rules: Rules) -> bool:
    for _, constraints in rules.items():
        if number_valid_for_constraints(num, constraints):
            return True
    return False


def is_valid_ticket(ticket: Ticket, rules: Rules) -> bool:
    for num in ticket:
        if not number_could_be_valid(num, rules):
            return False
    return True


def column_matches_constraints(
    constraints: Constraints, column: int, tickets: Tickets
) -> bool:
    for ticket in tickets:
        if not number_valid_for_constraints(ticket[column], constraints):
            return False
    return True


def rules_match_multiple_columns(rules_to_columns: RulesToColumns) -> bool:
    for name, possible_columns in rules_to_columns.items():
        if len(possible_columns) > 1:
            return True
    return False


def sort_by_number_possible_columns(rules_to_columns: RulesToColumns) -> RulesToColumns:
    return {
        k: v for k, v in sorted(rules_to_columns.items(), key=lambda item: len(item[1]))
    }


def match_rules_to_columns(tickets: Tickets, rules: Rules) -> RulesToColumns:
    rules_to_columns = {}
    number_rules = len(rules.keys())
    for name, constraints in rules.items():
        rules_to_columns[name] = []
        for i in range(number_rules):
            if column_matches_constraints(constraints, i, tickets):
                rules_to_columns[name].append(i)

    sorted_rules_to_columns = sort_by_number_possible_columns(rules_to_columns)

    claimed_columns = set()
    for name, columns in sorted_rules_to_columns.items():
        actual_column = set(columns).difference(set(claimed_columns))
        claimed_columns = claimed_columns.union(actual_column)
        sorted_rules_to_columns[name] = list(actual_column)

    return sorted_rules_to_columns


def main() -> float:
    rules, your_ticket, other_tickets = parse_input(get_input())

    valid_tickets = [
        ticket for ticket in other_tickets if is_valid_ticket(ticket, rules)
    ]

    rules_to_columns = match_rules_to_columns(valid_tickets, rules)

    departure_field_columns = [
        columns[0]
        for field, columns in rules_to_columns.items()
        if "departure" in field
    ]

    departure_values = [
        value for i, value in enumerate(your_ticket) if i in departure_field_columns
    ]

    return functools.reduce(lambda x, y: x * y, departure_values)


print(main())
