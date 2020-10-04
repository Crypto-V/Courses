# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than given number.


def numbers_less_than(given_list):
    given_number = int(input("Enter one number: "))
    updated_list = []
    for i in given_list:
        if i < given_number:
            updated_list.append(i)
    return updated_list


print(numbers_less_than([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
