# Program that check if the string is pangram or not.
# Pangram - is a word or sentence that have every letter of the alphabet at least once.

import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)
    # Remove the spaces from the input string
    str1 = str1.replace(" ", "")
    # Convert into lower case
    str1 = str1.lower()
    # Grab unique letter of the strings with set().
    str1 = set(str1)
    # Check if the set of alphabet is equal to input string set.
    return str1 == alphaset


print(ispangram("The quick brown fox jumps over the lazy dog"))
