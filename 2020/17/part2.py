import copy
from itertools import product

Coordinate = tuple[int, int, int, int]
Coordinates = list[Coordinate]
VerticalSlice = list[list[str]]
Cube = list[VerticalSlice]
HyperCube = list[Cube]


def empty_line(size: int) -> list[str]:
    return ["."] * size


def get_input() -> HyperCube:
    with open("input") as f:
        lines = f.readlines()
        cube_size = len(lines)
        return [
            [
                empty_vertical_slice(cube_size),
                empty_vertical_slice(cube_size),
                empty_vertical_slice(cube_size),
            ],
            [
                empty_vertical_slice(cube_size),
                [list(line.strip()) for line in lines],
                empty_vertical_slice(cube_size),
            ],
            [
                empty_vertical_slice(cube_size),
                empty_vertical_slice(cube_size),
                empty_vertical_slice(cube_size),
            ],
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


def empty_cube(cube_size: int, vertical_slice_size: int) -> Cube:
    return [empty_vertical_slice(vertical_slice_size) for _ in range(cube_size)]


def add_empty_cells_to_cube(cube: Cube) -> Cube:
    new_size = len(cube[0]) + 2
    return [
        empty_vertical_slice(new_size),
        *[add_empty_cells_to_slice(vertical_slice) for vertical_slice in cube],
        empty_vertical_slice(new_size),
    ]


def add_empty_cells_to_hypercube(hypercube: HyperCube):
    cube_size = len(hypercube[0]) + 2
    vertical_slice_size = len(hypercube[0][0]) + 2
    return [
        empty_cube(cube_size, vertical_slice_size),
        *[add_empty_cells_to_cube(cube) for cube in hypercube],
        empty_cube(cube_size, vertical_slice_size),
    ]


def is_valid_coordinate(coordinate: Coordinate, hypercube: HyperCube) -> bool:

    x, y, z, w = coordinate
    size_w = len(hypercube)
    size_z = len(hypercube[0])
    size_y = len(hypercube[0][0])
    size_x = len(hypercube[0][0][0])
    return (
        x >= 0
        and x < size_x
        and y >= 0
        and y < size_y
        and z >= 0
        and z < size_z
        and w >= 0
        and w < size_w
    )


def neighbhour_coordinates(coordinate: Coordinate, hypercube: HyperCube) -> Coordinates:
    x, y, z, w = coordinate
    index_shifts = list(product((-1, 0, 1), repeat=4))
    index_shifts.remove((0, 0, 0, 0))
    coordinates = [
        (x + x_shift, y + y_shift, z + z_shift, w + w_shift)
        for x_shift, y_shift, z_shift, w_shift in index_shifts
    ]

    return [
        coordinate
        for coordinate in coordinates
        if is_valid_coordinate(coordinate, hypercube)
    ]


def update_state(hypercube: HyperCube) -> HyperCube:
    old_hypercube = add_empty_cells_to_hypercube(hypercube)
    new_hypercube = copy.deepcopy(old_hypercube)

    for w, cube in enumerate(old_hypercube):
        for z, vertical_slice in enumerate(cube):
            for y, line in enumerate(vertical_slice):
                for x, old_cell in enumerate(line):
                    coordinates = neighbhour_coordinates((x, y, z, w), old_hypercube)

                    neighbors = [
                        old_hypercube[l][k][j][i] for i, j, k, l in coordinates
                    ]

                    num_active_neighbors = len(
                        [neighbor for neighbor in neighbors if neighbor == "#"]
                    )

                    if (old_cell == "#" and num_active_neighbors in [2, 3]) or (
                        old_cell == "." and num_active_neighbors == 3
                    ):
                        next_cell_state = "#"
                    else:
                        next_cell_state = "."

                    new_hypercube[w][z][y][x] = next_cell_state

    return new_hypercube


def num_active_elements(hypercube: HyperCube) -> int:
    count = 0
    for cube in hypercube:
        for vertical_slice in cube:
            for line in vertical_slice:
                for cell in line:
                    if cell == "#":
                        count += 1
    return count


def hypercube_dimensions(hypercube: HyperCube) -> tuple[int, int, int, int]:
    return (
        len(hypercube),
        len(hypercube[0]),
        len(hypercube[0][0]),
        len(hypercube[0][0][0]),
    )


def print_hypercube(hypercube: HyperCube) -> None:
    for w, cube in enumerate(hypercube):
        for z, vertical_slice in enumerate(cube):
            print(f"z={z} w={w}")
            for line in vertical_slice:
                print(repr("".join(line)))
            print()


def main() -> int:
    hypercube = get_input()

    rounds = 6

    for round in range(rounds):
        print(f"Round {round}")
        hypercube = update_state(hypercube)

    return num_active_elements(hypercube)


print(main())
