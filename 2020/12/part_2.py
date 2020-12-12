import re
from functools import reduce
from typing import List

State = tuple[int, int, int, int]
Instruction = tuple[str, int]


def get_input() -> List[str]:
    with open("./input", "r") as f:
        return f.readlines()


def get_instructions_details(s: str) -> Instruction:
    m = re.search(r"^([NSEWLRF])(\d+)$", s)
    return (m.group(1), int(m.group(2)))


def rotate_direction(state: State, spin: str, degrees: int) -> State:
    waypoint_x = state[2]
    waypoint_y = state[3]

    if spin == "L":
        if degrees == 90:
            new_waypoint = (waypoint_y * -1, waypoint_x)
        if degrees == 180:
            new_waypoint = (waypoint_x * -1, waypoint_y * -1)
        if degrees == 270:
            new_waypoint = (waypoint_y, waypoint_x * -1)

    if spin == "R":
        if degrees == 90:
            new_waypoint = (waypoint_y, waypoint_x * -1)
        if degrees == 180:
            new_waypoint = (waypoint_x * -1, waypoint_y * -1)
        if degrees == 270:
            new_waypoint = (waypoint_y * -1, waypoint_x)

    return (state[0], state[1], new_waypoint[0], new_waypoint[1])


def update_state(state: State, instruction: str) -> State:
    action, amount = get_instructions_details(instruction)

    if action == "N":
        return (
            state[0],
            state[1],
            state[2],
            state[3] + amount,
        )
    elif action == "E":
        return (
            state[0],
            state[1],
            state[2] + amount,
            state[3],
        )
    elif action == "S":
        return (
            state[0],
            state[1],
            state[2],
            state[3] - amount,
        )
    elif action == "W":
        return (state[0], state[1], state[2] - amount, state[3])
    elif action == "F":
        return (
            state[0] + (amount * state[2]),
            state[1] + (amount * state[3]),
            state[2],
            state[3],
        )
    elif action in ("L", "R"):
        return rotate_direction(state=state, spin=action, degrees=amount)

    else:
        raise RuntimeError(f"This should not happen {instruction} {action} {amount}")


def main() -> State:
    initial_state = (0, 0, 10, 1)
    instructions = get_input()

    final_state = reduce(update_state, instructions, initial_state)

    return abs(final_state[0]) + abs(final_state[1])


print(main())
