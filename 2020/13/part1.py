def read_input() -> tuple[int, list[str]]:
    with open("./input", "r") as f:
        lines = f.readlines()
        start_time = int(lines[0].strip())
        bus_ids = lines[1].strip().split(",")
        return (start_time, bus_ids)


def find_earliest_bustime(start_time: int, bus_ids: list[str]) -> int:
    current_time = start_time
    while True:
        print(current_time)
        for bus_id in bus_ids:
            if bus_id != "x" and current_time % int(bus_id) == 0:
                return int(bus_id) * (current_time - start_time)
        current_time += 1


def main() -> int:
    start_time, bus_ids = read_input()
    return find_earliest_bustime(start_time=start_time, bus_ids=bus_ids)


print(main())
