from collections.abc import Iterable


def get_input():
    with open("input") as f:
        lines = f.readlines()
        return [int(x) for x in lines[0].split(",")]


def update_state(value: int, index: int, state: dict) -> dict:
    if value not in state.keys():
        state[value] = [index]
    else:
        state[value].append(index)

    return state


def infinite_answers(starting_list: list[int]) -> Iterable[int]:
    state = {}
    current_index = 1
    last_element = -1

    while True:
        if current_index < len(starting_list) + 1:
            next_element = starting_list[current_index - 1]
            if last_element != -1:
                state = update_state(last_element, current_index - 1, state)
            yield next_element
        else:

            if last_element not in state.keys():
                next_element = 0
                state = update_state(last_element, current_index - 1, state)
                yield next_element
            else:
                next_element = current_index - 1 - state[last_element][-1]
                state = update_state(last_element, current_index - 1, state)
                yield next_element

        last_element = next_element
        current_index += 1


def main() -> int:
    starting_numbers = get_input()

    for i, num in enumerate(infinite_answers(starting_list=starting_numbers)):
        if i == 2020 - 1:
            return num


print(main())
