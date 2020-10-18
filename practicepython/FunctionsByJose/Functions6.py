# Python function to check for palindrome.


def palindrome(s):
    # Removing the space from the string
    striped_string = s.replace(" ", "")
    # Checking if string is equal to reversed version of the string.
    return striped_string.lower() == striped_string.lower()[::-1]


print(palindrome("Nurses run"))
