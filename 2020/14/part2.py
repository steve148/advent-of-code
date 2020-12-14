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

    return int(new_bitwise_value, 2)


def get_memory_updates(index: int, value: int, mask: str) -> list[tuple[int, int]]:
    bitwise_value = f"{index:036b}"

    if mask[0] == "X":
        addresses = ["0", "1"]
    if mask[0] == "1":
        addresses = ["1"]
    if mask[0] == "0":
        addresses = [bitwise_value[0]]

    for i in range(1, len(mask)):
        if mask[i] == "0":
            new_addresses = [address + bitwise_value[i] for address in addresses]
            addresses = new_addresses

        if mask[i] == "1":
            new_addresses = [address + "1" for address in addresses]
            addresses = new_addresses

        if mask[i] == "X":
            new_addresses = []
            for address in addresses:
                new_addresses.append(f"{address}0")
                new_addresses.append(f"{address}1")
            addresses = new_addresses

    update_numbers = [int(x, 2) for x in addresses]
    return [(address, value) for address in update_numbers]


def handle_instruction(state: dict, instruction: str) -> dict:
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

        mask = state["mask"]

        memory_index = int(match.group(1))
        memory_value = int(match.group(2))

        memory_updates = get_memory_updates(
            index=memory_index, value=memory_value, mask=mask
        )

        new_memory = state["memory"]
        for index, value in memory_updates:
            new_memory[index] = value

        return {"memory": new_memory, "mask": mask}

    raise RuntimeError(f"Me no understand instruction {instruction}")


def main() -> int:
    instructions = get_input()

    state: dict = {"memory": {}, "mask": 0}

    final_state = functools.reduce(handle_instruction, instructions, state)

    return sum(final_state["memory"].values())


print(main())
