def get_input():
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


def num_trees_on_slope(hill: list[list[str]]) -> int:
    tree_count = 0
    horizontal_index = 0
    hill_width = len(hill[0])

    for hill_level in range(len(hill)):
        if hill[hill_level][horizontal_index % hill_width] == "#":
            tree_count += 1
        horizontal_index += 3

    return tree_count


def main() -> int:
    hill = get_input()

    return num_trees_on_slope(hill=hill)


print(main())
