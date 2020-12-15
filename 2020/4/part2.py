import re


def get_input():
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


def get_passports_from_input(lines: list[str]) -> list[dict]:
    passports = []
    current_passport = {}

    for line in lines:
        if line == "":
            passports.append(current_passport)
            current_passport = {}
        else:
            fields = line.split(" ")
            for field in fields:
                key, value = field.split(":")
                current_passport[key] = value

    passports.append(current_passport)

    return passports


def all_fields_exist(passport: dict) -> bool:
    keys = passport.keys()
    for expected_field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if expected_field not in keys:
            return False

    return True


def valid_year(passport: dict, key: str, min: int, max: int) -> bool:
    return (
        passport.get(key)
        and int(passport.get(key)) >= min
        and int(passport.get(key)) <= max
    )


def valid_height(height: str) -> bool:
    match = re.search(r"(\d+)([a-zA-Z]+)", height)

    if not match:
        return False

    amount, units = match.groups()
    amount = int(amount)
    if units == "in":
        return amount >= 59 and amount <= 76

    if units == "cm":
        return amount >= 150 and amount <= 193

    raise RuntimeError("units did not match any known types")


def valid_hair_colour(hair_colour: str) -> bool:
    return re.search(r"^#[0-9a-f]{6}$", hair_colour)


def valid_eye_colour(eye_colour: str) -> bool:
    return eye_colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_passport_id(passport_id: str) -> bool:
    return re.search(r"^[0-9]{9}$", passport_id)


def is_valid(passport: dict) -> bool:
    print(passport)
    return (
        all_fields_exist(passport)
        and valid_year(passport, "byr", 1920, 2002)
        and valid_year(passport, "iyr", 2010, 2020)
        and valid_year(passport, "eyr", 2020, 2030)
        and valid_height(passport.get("hgt"))
        and valid_hair_colour(passport.get("hcl"))
        and valid_eye_colour(passport.get("ecl"))
        and valid_passport_id(passport.get("pid"))
    )


def main() -> int:
    lines = get_input()

    passports = get_passports_from_input(lines=lines)

    valid_passports = [
        passport for passport in passports if is_valid(passport=passport)
    ]

    return len(valid_passports)


print(main())
