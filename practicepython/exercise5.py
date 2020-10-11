import random
# Creating the function that will generate a integer number.


def number_generator(fr, to):
    # Fr represents the starting value and to is the end point of the random range.
    return random.randint(fr, to)


# Creating a empty list that will be filled up with random values.
list1 = []
while len(list1) <= 15:  # Setting up the limit of values in the set to be no more than 15
    list1.append(number_generator(1, 100))  # Appending the random value to the list.

list2 = []
while len(list2) <= 15:
    list2.append(number_generator(2, 50))
# Concatenating the values of list1 and 2 into a tuple to remove the duplicates.
final_list = set(list1 + list2)
print(list(final_list))  # Printing out the final list casted into a list.
