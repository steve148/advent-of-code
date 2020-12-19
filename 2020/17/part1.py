import copy
from itertools import product

Coordinate = tuple[int, int, int]
Coordinates = list[Coordinate]
VerticalSlice = list[list[str]]
Cube = list[VerticalSlice]


def empty_line(size: int) -> list[str]:
    return ["."] * size


def get_input() -> Cube:
    with open("input") as f:
        lines = f.readlines()
        cube_size = len(lines)
        return [
            empty_vertical_slice(cube_size),
            [list(line.strip()) for line in lines],
            empty_vertical_slice(cube_size),
        ]


def add_empty_cells_to_slice(vertical_slice: VerticalSlice) -> VerticalSlice:
    new_size = len(vertical_slice) + 2
    return [
        empty_line(new_size),
        *[["."] + line + ["."] for line in vertical_slice],
        empty_line(new_size),
    ]


def empty_vertical_slice(size: int) -> VerticalSlice:
    return [["."] * size for i in range(size)]


def add_empty_cells_to_cube(cube: Cube):
    new_cube_size = len(cube[0]) + 2
    return [
        empty_vertical_slice(new_cube_size),
        *[add_empty_cells_to_slice(vertical_slice) for vertical_slice in cube],
        empty_vertical_slice(new_cube_size),
    ]


def is_valid_coordinate(coordinate: Coordinate, cube: Cube) -> bool:
    x, y, z = coordinate
    size_z = len(cube)
    size_y = len(cube[0])
    size_x = len(cube[0][0])
    return x not in [-1, size_x] and y not in [-1, size_y] and z not in [-1, size_z]


def neighbhour_coordinates(x: int, y: int, z: int, cube: Cube) -> Coordinates:
    index_shifts = list(product((-1, 0, 1), repeat=3))
    index_shifts.remove((0, 0, 0))
    coordinates = [
        (x + x_shift, y + y_shift, z + z_shift)
        for x_shift, y_shift, z_shift in index_shifts
    ]

    return [
        coordinate
        for coordinate in coordinates
        if is_valid_coordinate(coordinate, cube)
    ]


def update_state(cube: Cube) -> Cube:
    old_cube = add_empty_cells_to_cube(cube)
    new_cube = copy.deepcopy(old_cube)

    for z, vertical_slice in enumerate(old_cube):
        for y, line in enumerate(vertical_slice):
            for x, old_cell in enumerate(line):
                coorindates = neighbhour_coordinates(x, y, z, old_cube)

                neighbors = [old_cube[k][j][i] for i, j, k in coorindates]

                num_active_neighbors = len(
                    [neighbor for neighbor in neighbors if neighbor == "#"]
                )

                if (old_cell == "#" and num_active_neighbors in [2, 3]) or (
                    old_cell == "." and num_active_neighbors == 3
                ):
                    next_cell_state = "#"
                else:
                    next_cell_state = "."

                new_cube[z][y][x] = next_cell_state

    return new_cube


def num_active_elements(cube: Cube) -> int:
    count = 0
    for layer_z in cube:
        for layer_y in layer_z:
            for element in layer_y:
                if element == "#":
                    count += 1
    return count


def print_cube(cube: Cube) -> None:
    for z in range(len(cube)):
        print(f"z={z}")
        for line in cube[z]:
            print(repr(line))
        print()


def main() -> int:
    cube = get_input()

    rounds = 6

    for _ in range(rounds):
        cube = update_state(cube)

    return num_active_elements(cube)


print(main())
