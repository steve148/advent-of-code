import functools
import re


def get_input() -> list[str]:
    with open("input") as f:
        return f.readlines()


def combine_value_with_bitmask(value: int, mask: str) -> int:
    bitwise_value = f"{value:036b}"

    new_bitwise_value_list = []
    for value_bit, mask_bit in zip(bitwise_value, mask):
        bit = value_bit if mask_bit == "X" else mask_bit
        new_bitwise_value_list.append(bit)

    new_bitwise_value = "".join(new_bitwise_value_list)

    print(bitwise_value)
    print(mask)
    print(new_bitwise_value)

    return int(new_bitwise_value, 2)


def handle_instruction(state: dict, instruction: str) -> dict:
    print(state)
    if "mask" in instruction:
        match = re.search(r"mask = (\w+)", instruction)
        if not match:
            raise RuntimeError(f"Mem instruction should match {instruction}")

        new_mask = match.group(1)
        return {"memory": state["memory"], "mask": new_mask}

    if "mem" in instruction:
        match = re.search(r"mem\[(\d+)\] = (\d+)", instruction)
        if not match:
            raise RuntimeError(f"Mem instruction should match {instruction}")

        memory_index = int(match.group(1))
        memory_value = int(match.group(2))
        new_memory = state["memory"]
        new_memory[memory_index] = combine_value_with_bitmask(
            memory_value, state["mask"]
        )
        return {"memory": new_memory, "mask": state["mask"]}

    raise RuntimeError(f"Me no understand instruction {instruction}")


def main() -> int:
    instructions = get_input()

    # Initialize memory.
    state: dict = {"memory": {}, "mask": 0}

    final_state = functools.reduce(handle_instruction, instructions, state)

    return sum(final_state["memory"].values())


print(main())
