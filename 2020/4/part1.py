def get_input():
    with open("input") as f:
        return f.readlines()


def get_passports_from_input(lines: list[str]) -> list[dict]:
    passports = []
    current_passport = {}

    for line in lines:
        if line.strip() == "":
            passports.append(current_passport)
            current_passport = {}
        else:
            fields = line.split(" ")
            for field in fields:
                key, value = field.split(":")
                current_passport[key] = value

    passports.append(current_passport)

    return passports


def is_valid(passport: dict) -> bool:
    keys = passport.keys()
    for expected_field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if expected_field not in keys:
            return False

    return True


def main() -> int:
    lines = get_input()

    passports = get_passports_from_input(lines=lines)

    valid_passports = [
        passport for passport in passports if is_valid(passport=passport)
    ]

    return len(valid_passports)


print(main())
