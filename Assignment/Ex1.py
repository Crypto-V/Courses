original_list = ["cup", 'cereal', 'milk', (8, 4, 3)]
# Selecting each number inside of the tuple and assigning to the variable.
num1 = original_list[3][0]
num2 = original_list[3][1]
num3 = original_list[3][2]

new_list = [num1, num2, num3]  # Creating a list and placing the numbers
new_list.sort()  # Sorting the list
new_tuple = tuple(new_list)  # After sorting we are converting the list into tuple
original_list.pop()  # Poping out the last element from the list.
original_list.append(new_tuple)  # Apending the tuple to the original list.

print(original_list)
