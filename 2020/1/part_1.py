def get_input() -> list[int]:
    with open("input", "r") as f:
        return [int(line) for line in f.readlines()]


def pair_ints_2020(expenses: list[int]) -> tuple[int, int]:
    size = len(expenses)
    for i in range(size):
        for j in range(i, size):
            if expenses[i] + expenses[j] == 2020:
                return (expenses[i], expenses[j])


def main() -> int:
    numbers = get_input()

    x, y = pair_ints_2020(numbers)

    return x * y


print(main())
