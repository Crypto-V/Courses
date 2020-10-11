import random


# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
# uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your code in a main method.


def password_generator(len_of_password):
    all_letters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_items = "!@#$%^&*()?"
    p = "".join(random.sample(all_letters, len_of_password))
    return p[0].upper()+p + char_items[random.randint(0, 12)]


passlen = int(input("Enter the len of required password: "))

print(password_generator(passlen))
