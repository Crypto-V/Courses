import sys

states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def pull_the_city(city=None):
    if city in states.keys():
        initials = states.get(city)
        print(capital_cities.get(initials))


if __name__ == "__main__":
    pull_the_city(sys.argv[1]) if len(sys.argv) == 2 else None
