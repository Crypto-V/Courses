"""
Create a function that takes a string as an argument and returns a list of the characters from the string.
"""


def separate(string):
    str = string.replace(" ", "")
    return list(str)


print(separate("Hello this is very simple program"))
