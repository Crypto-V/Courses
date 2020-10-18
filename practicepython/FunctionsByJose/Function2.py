# Write a function that will check if the given nuber is in a given range


def ran_check(number, low, high):
    return number in range(low, high+1)


print(ran_check(5, 2, 7))
