import functools


def get_input():
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


def num_trees_on_slope(
    hill: list[list[str]], horizontal_step: int, vertical_step: int
) -> int:
    tree_count = 0
    horizontal_index = 0
    hill_width = len(hill[0])

    for hill_level in range(0, len(hill), vertical_step):
        if hill[hill_level][horizontal_index % hill_width] == "#":
            tree_count += 1
        horizontal_index += horizontal_step

    return tree_count


def main() -> int:
    hill = get_input()

    trees_encountered = []
    for horizontal_step, vertical_step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_encountered.append(
            num_trees_on_slope(
                hill=hill, horizontal_step=horizontal_step, vertical_step=vertical_step
            )
        )

    return functools.reduce(lambda acc, n: acc * n, trees_encountered)


print(main())
