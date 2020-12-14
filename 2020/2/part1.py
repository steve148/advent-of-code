import re


def get_input() -> list[str]:
    with open("input", "r") as f:
        return f.readlines()


def parse_lines(lines: list[str]) -> list[tuple[int, int, str, str]]:
    result = []
    for line in lines:
        match = re.search(r"^(\d+)\-(\d+) ([a-z]): ([a-z]+)$", line)

        if not match:
            raise RuntimeError(f"Match should always succeed {line}")

        result.append(
            (
                int(match.group(1)),
                int(match.group(2)),
                match.group(3),
                match.group(4),
            )
        )

    return result


def password_is_correct(min: int, max: int, letter: str, password: str) -> bool:
    return min <= password.count(letter) and max >= password.count(letter)


def main() -> int:
    lines = get_input()

    test_cases = parse_lines(lines)

    correct_passwords = [
        test_case for test_case in test_cases if password_is_correct(*test_case)
    ]

    return len(correct_passwords)


print(main())
