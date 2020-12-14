def read_input() -> tuple[int, list]:
    with open("./input", "r") as f:
        lines = f.readlines()
        start_time = int(lines[0].strip())

        bus_ids = [
            int(bus_id) if bus_id != "x" else bus_id
            for bus_id in lines[1].strip().split(",")
        ]
        return (start_time, bus_ids)


def time_difference_between_buses(bus_ids: list) -> list:
    return [i for i in range(len(bus_ids)) if bus_ids[i] != "x"]


def find_earliest_time_subsequent_buses(bus_ids: list) -> int:
    time_differences = time_difference_between_buses(bus_ids)
    real_bus_ids = [bus_id for bus_id in bus_ids if bus_id != "x"]

    current_time = 0
    lcm = 1

    for i in range(len(real_bus_ids) - 1):
        bus_id = real_bus_ids[i + 1]
        time_difference = time_differences[i + 1]
        lcm *= real_bus_ids[i]

        while (current_time + time_difference) % bus_id != 0:
            current_time += lcm

    return current_time


def main() -> int:
    _, bus_ids = read_input()
    return find_earliest_time_subsequent_buses(bus_ids=bus_ids)
