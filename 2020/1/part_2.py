def get_input() -> list[int]:
    with open("input", "r") as f:
        return [int(line) for line in f.readlines()]


def pair_ints_2020(expenses: list[int]) -> tuple[int, int, int]:
    size = len(expenses)
    for i in range(size):
        for j in range(i, size):
            for k in range(j, size):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return (expenses[i], expenses[j], expenses[k])


def main() -> int:
    numbers = get_input()

    x, y, z = pair_ints_2020(numbers)

    return x * y * z


print(main())
