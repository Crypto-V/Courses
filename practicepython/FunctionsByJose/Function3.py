# Python function that takes a string and counts how many lower case letters and uppercase letters are in the string.

my_str = "Hello Mr. Rogers, how are you this fine Tuesday?"


# Using dictionaries


def up_low(s):
    d = {"upper": 0, "lower": 0}

    for char in s:
        if char.isupper():
            d["upper"] += 1
        elif char.islower():
            d["lower"] += 1
        else:
            pass

    print(f"Original String:  {s}")
    print(f"Lower case count : {d['upper']}")
    print(f"Upper case count : {d['lower']}")


up_low(my_str)

# Using for loop


# def up_low(s):
#     lowercase = 0
#     uppercase = 0
#
#     for char in s:
#         if char.isupper():
#             uppercase += 1
#         elif char.islower():
#             lowercase += 1
#         else:
#             pass
#
#     print(f"Original String:  {s}")
#     print(f"Lower case count : {lowercase}")
#     print(f"Upper case count : {uppercase}")
#
#
# up_low(my_str)

# Using while loop

# def up_low(string):
#     upper_case = 0
#     lower_case = 0
#     index = 0
#     while index <= len(my_str) - 1:
#         if string[index] not in [" ", ".", ",", "?"]:
#             if string[index].isupper():
#                 upper_case += 1
#             else:
#                 lower_case += 1
#         index += 1
#     print(f"There are {str(upper_case)} upper case letters in the given string! ")
#     print(f"There are {str(lower_case)} lower case letters in the given string! ")
#
#
# up_low(my_str)
