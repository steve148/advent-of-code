import re
from functools import reduce
from typing import List

Position = tuple[int, int, str]
Instruction = tuple[str, int]


def get_input() -> List[str]:
    with open("./input", "r") as f:
        return f.readlines()


def get_instructions_details(s: str) -> Instruction:
    m = re.search(r"^([NSEWLRF])(\d+)$", s)
    return (m.group(1), int(m.group(2)))


def rotate_direction(direction: str, spin: str, degress: int) -> str:
    directions = "NESWNESW"

    index_change = int(degress / 90)

    if spin == "L":
        index = directions.rfind(direction)
        return directions[index - index_change]
    elif spin == "R":
        index = directions.find(direction)
        return directions[index + index_change]
    else:
        raise RuntimeError(f"Another no-no {spin}")


def update_position(position: Position, instruction: str) -> Position:
    action, amount = get_instructions_details(instruction)

    if action == "N":
        return (position[0], position[1] + amount, position[2])
    elif action == "E":
        return (position[0] + amount, position[1], position[2])
    elif action == "S":
        return (position[0], position[1] - amount, position[2])
    elif action == "W":
        return (position[0] - amount, position[1], position[2])
    elif action == "F":
        return update_position(position=position, instruction=f"{position[2]}{amount}")
    elif action in ("L", "R"):
        return (
            position[0],
            position[1],
            rotate_direction(direction=position[2], spin=action, degress=amount),
        )
    else:
        raise RuntimeError(f"This should not happen {instruction} {action} {amount}")


def main() -> Position:
    initial_position = (0, 0, "E")
    instructions = get_input()

    final_position = reduce(update_position, instructions, initial_position)

    return abs(final_position[0]) + abs(final_position[1])


print(main())
