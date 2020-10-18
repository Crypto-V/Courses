# Write a python function that multiply all the numbers in the list!


def multiply(lst_numebrs):
    result = 1
    for num in lst_numebrs:
        result = result * num
    return result


print(multiply([1, 2, 3, -4]))
