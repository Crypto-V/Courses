# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even
# elements of this list in it.

# Solution 1
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]

print(b)

# Solution 2
# def make_new_list(list):
#     updated_list = []
#     for item in list:
#         if item % 2 == 0:
#             updated_list.append(item)
#     return updated_list
#
#
# print(make_new_list([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))
