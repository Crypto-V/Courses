import sys

states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def pull_the_city(val=None):
    if val in capital_cities.values():
        for key, value in capital_cities.items():
            if value == val:
                for k, v in states.items():
                    if v == key:
                        print(val + " is the capital of " + k)
    else:
        print("Unknown city")


if __name__ == "__main__":
    pull_the_city(sys.argv[1]) if len(sys.argv) == 2 else None
