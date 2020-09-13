"""
In the list below we will replace the letter f and the word card with another words and letter.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'f'], [3, 9, 4, 12], 4), 'car', 42]
# Selecting the element that we want to replace and assigning another value
my_list[2][0][3] = "CHANGED"
my_list[3] = "CHANGED"
print(my_list)