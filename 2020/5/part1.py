import math

BoardingPass = tuple[int, int, int]


def get_input() -> list[str]:
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


def traverse_string_for_index(s: str, first_half_character: str) -> int:
    low = 0
    high = 2 ** len(s) - 1
    for c in s:
        if c == first_half_character:
            high -= math.floor((high - low) / 2) + 1
        else:
            low += math.ceil((high - low) / 2)

    return low


def parse_seat(s: str) -> BoardingPass:
    row = traverse_string_for_index(s[0:7], "F")
    column = traverse_string_for_index(s[7:10], "L")
    return row, column, row * 8 + column


def get_max_seat_id(boarding_passes: list[BoardingPass]) -> int:
    highest_num = boarding_passes[0][2]

    for boarding_pass in boarding_passes:
        if boarding_pass[2] > highest_num:
            highest_num = boarding_pass[2]

    return highest_num


def main() -> int:
    boarding_passes = [parse_seat(s) for s in get_input()]
    return get_max_seat_id(boarding_passes)


print(main())
