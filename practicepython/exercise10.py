a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def unique_values(var1, var2):
    my_list = []
    for x in var1:
        if x in var2:
            my_list.append(x)

    return set(my_list)


print(unique_values(a, b))
