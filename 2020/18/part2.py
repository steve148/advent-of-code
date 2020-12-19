def get_input() -> list[str]:
    with open("input") as f:
        return f.readlines()


def parse_input(lines: list[str]) -> list[str]:
    return [line.strip().replace(" ", "") for line in lines]


def evaluate_expression(left: int, operator: str, right: int) -> str:
    if operator == "+":
        return str(left + right)
    if operator == "*":
        return str(left * right)


def evaluate_equation(equation: str) -> int:
    stack = []
    while len(equation) > 0 or len(stack) > 1:
        while len(stack) < 3:
            stack.append(equation[0])
            equation = equation[1:]

        next_token = equation[0] if len(equation) else ""
        right_token = stack.pop()
        center_token = stack.pop()
        left_token = stack.pop()

        if left_token == "(" and right_token == ")":
            stack.append(center_token)
        elif (
            left_token.isnumeric()
            and center_token in ["+", "*"]
            and right_token.isnumeric()
            and next_token != "+"
        ):
            stack.append(
                evaluate_expression(
                    left=int(left_token), operator=center_token, right=int(right_token)
                )
            )
        elif len(equation):
            stack.extend([left_token, center_token, right_token])
            stack.append(equation[0])
            equation = equation[1:]

    return int(stack[0])


def main() -> int:
    equations = parse_input(get_input())

    equation_answers = [evaluate_equation(equation) for equation in equations]

    return sum(equation_answers)


print(main())
