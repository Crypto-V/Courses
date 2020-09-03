import sys

states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def main(val=None):
    sliced_string = val.split(",")

    for index in sliced_string:
        if len(index.strip()) > 0:
            if index.strip().title() in states.keys():
                check_by_state(index.strip().title())
            elif index.strip().title() in capital_cities.values():
                check_by_capital_name(index.strip().title())
            else:
                print(index.strip() + " is neither a capital city nor a state")


def check_by_state(state):
    initials = states.get(state)
    print("The capital of " + state + " is " + capital_cities.get(initials))


def check_by_capital_name(val):
    for key, value in capital_cities.items():
        if value == val:
            for k, v in states.items():
                if v == key:
                    print(val + " is the capital of " + k)


if __name__ == "__main__":
    # main(sys.argv[1]) if len(sys.argv) == 2 else None
    main("New Jersey, Trenton, toto,            ,      sAlem")
