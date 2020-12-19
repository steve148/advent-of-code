import re


def get_input() -> list[str]:
    with open("input") as f:
        return f.readlines()


def parse_input(lines: list[str]):
    return [line.strip().replace(" ", "") for line in lines]


def find_closing_bracket_index(equation: str) -> int:
    unclosed_pairs = 0
    for i in range(0, len(equation)):
        if equation[i] == "(":
            unclosed_pairs += 1

        if equation[i] == ")":
            unclosed_pairs -= 1

        if unclosed_pairs == 0:
            return i


def get_left_value(equation: str) -> tuple[int, int, int]:
    print("get_left_value", equation)
    if equation[0] == "(":
        closing_bracket = find_closing_bracket_index(equation)
        print("closing_bracket", closing_bracket)
        return evaluate_equation(equation[1:closing_bracket]), 0, closing_bracket

    m = re.search(r"^\d+", equation)
    if m:
        return int(m.group()), 0, m.span()[1] - 1


def evaluate_expression(left: int, operator: str, right: int) -> int:
    if operator == "+":
        return left + right
    if operator == "*":
        return left * right


def evaluate_equation(equation: str) -> int:
    print("evaluate_equation", equation)
    left_value, left_start, left_end = get_left_value(equation)

    print("left", left_value, left_start, left_end)

    operator = equation[left_end + 1]

    print("operator", operator)

    right_value, right_start, right_end = get_left_value(equation[left_end + 2 :])
    right_start += left_end + 2
    right_end += left_end + 2

    print("right", right_value, right_start, right_end)

    new_value = evaluate_expression(left_value, operator, right_value)

    print(new_value)

    if right_end == len(equation) - 1:
        return new_value
    else:
        return evaluate_equation(str(new_value) + equation[right_end + 1 :])


def main() -> int:
    equations = parse_input(get_input())

    equation_answers = [evaluate_equation(equation) for equation in equations]

    print(equation_answers)

    return sum(equation_answers)


print(main())
