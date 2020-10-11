# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order


def revere_the_string(given_string):
    return " ".join(given_string.split()[::-1])


given_string = input("Type here a string which will be reversed!: ")
print(revere_the_string(given_string))
