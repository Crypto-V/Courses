# Create a program that asks the user to enter their name and their age. Print out a message
# addressed to them that tells them the year that they will turn 100 years old.

# Get the user input and store in variables
ask_name = input("What is your name user? ")
ask_age = int(input("How old are you? "))


# Creating the function that will do the work
def when_you_will_be_100(var1, var2):
    year = 2020
    if var2 > 0 and var1 != "":
        make_100 = year - var2 + 100
        print("Hello " + var1 + " based on my calculations you will be 100 years old in " + str(make_100) + ".")
    else:
        print("Wrong data entered.")


# Calling the function with the given attributes
when_you_will_be_100(ask_name, ask_age)
