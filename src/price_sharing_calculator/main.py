from os import environ

from general_utils.consts import load_env


def get_vars_from_env() -> tuple[int, int, int, int]:
    salary_will = environ.get("SALARY_WILL")
    salary_michelle = environ.get("SALARY_MICHELLE")
    base_rent = environ.get("BASE_RENT")
    ren_rent = environ.get("REN_RENT")
    assert None not in [salary_will, salary_michelle, base_rent, ren_rent], "Need to fill your .env file."
    salary_will = int(salary_will)
    salary_michelle = int(salary_michelle)
    base_rent = int(base_rent)
    ren_rent = int(ren_rent)
    return base_rent, ren_rent, salary_michelle, salary_will


def get_ratio(salary: int, total: int) -> float:
    return round(salary / total, 4)


def get_electricity_owed() -> float:
    electricity_bills = []
    print("Hit return to stop.")
    electricity_bill = input("How big was the electricity bill? ")
    while electricity_bill:
        electricity_bills.append(float(electricity_bill))
        electricity_bill = input("How big was the next electricity bill? ")
    electricity_owed = sum(electricity_bills) - 100 * len(electricity_bills)
    return electricity_owed


def main():
    load_env()
    base_rent, ren_rent, salary_michelle, salary_will = get_vars_from_env()

    total = salary_will + salary_michelle
    michelle_ratio = get_ratio(salary_michelle, total)
    electricity_total = get_electricity_owed()
    rent_check = base_rent + ren_rent + electricity_total
    shared = rent_check - ren_rent
    michelle_owes = round(michelle_ratio * shared, 2)

    print(f"Rent check total is ${rent_check}. Calculated using {base_rent=} + {ren_rent=} + {electricity_total=}")
    print(f"Rent without Ren: ${shared}.")
    print()
    print(f"Will salary:      ${salary_will:>6}")
    print(f"Michelle salary:  ${salary_michelle:>6}")
    print(f"Will percent:      {round((1-michelle_ratio) * 100, 2):>6}%")
    print(f"Michelle percent:  {round(michelle_ratio * 100, 2):>6}%")
    print()
    print(f"Rent to be split ${shared} after removing Ren ${ren_rent}.")
    print()
    print(f"Will owes:        ${round(rent_check - michelle_owes, 2):>7}")
    print(f"Michelle owes:    ${michelle_owes:>7}")


if __name__ == "__main__":
    main()
