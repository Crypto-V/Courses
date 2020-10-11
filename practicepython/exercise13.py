import random


# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.


def generating_list_of_numbers():
    my_list = []
    while len(my_list) <= 10:
        my_list.append(random.randint(1, 9))
    print(f"This is my given list: {my_list}")
    return my_list


def do_work_with_loop(given_list):
    # this one uses a for loop
    final_list = []
    for i in given_list:
        if i not in final_list:
            final_list.append(i)
    return final_list


def do_work_with_sets(given_list):
    return list(set(given_list))


one_list = generating_list_of_numbers()
print(f"This is my final list: {do_work_with_loop(one_list)}")
print(f"This is my final list: {do_work_with_sets(one_list)} , this one is not different is just ordered ! ))")





