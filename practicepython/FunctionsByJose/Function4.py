# Python function that takes a list and retruns a list with unique values.

# Easy way


# def unique_list(lst):
#     return set(lst)
#
#
# print(list(unique_list([1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])))


def unique_list(lst):
    seen_numbers = []
    for num in lst:
        if num not in seen_numbers:
            seen_numbers.append(num)
    return seen_numbers


print(list(unique_list([1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])))

