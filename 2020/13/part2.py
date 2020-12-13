import math


def read_input() -> tuple[int, list]:
    with open("./input", "r") as f:
        lines = f.readlines()
        start_time = int(lines[0].strip())

        bus_ids = [
            int(bus_id) if bus_id != "x" else bus_id
            for bus_id in lines[1].strip().split(",")
        ]
        return (start_time, bus_ids)


def modulo_invariant(product: int, number: int) -> int:
    return pow(product, -1, number)


def chinese_remainder_theorem(numbers: list[int], remainders: list[int]) -> int:
    total_product = math.prod(numbers)
    result = 0
    for number, remainder in zip(numbers, remainders):
        number_product = total_product // number
        number_result = (
            modulo_invariant(product=number_product, number=number)
            * remainder
            * number_product
        )
        result += number_result
    return result % total_product


def find_earliest_time_subsequent_buses(bus_ids: list) -> int:
    numbers = []
    remainders = []
    for i, bus_id in enumerate(bus_ids):
        if bus_id != "x":
            numbers.append(bus_id)
            remainders.append((bus_id - i) % bus_id)

    return chinese_remainder_theorem(numbers=numbers, remainders=remainders)


def main() -> int:
    _, bus_ids = read_input()
    return find_earliest_time_subsequent_buses(bus_ids=bus_ids)


print(main())
