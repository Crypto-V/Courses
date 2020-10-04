# Ask the user for a number. Depending on whether the number is even
# or odd, print out an appropriate message to the user
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

given_number = int(input("Enter one number: "))
check_number = int(input("Enter the number you want to divide with: "))


def check(num1, num2):
    if num1 % 4 == 0:
        print("Number is a multiple of 4")
    elif (num1 % num2) == 0:
        print(str(num1) + " is even number.")
    else:
        print(str(num1) + " is odd ")


while given_number != 0:
    check(given_number, check_number)
    break

else:
    print("0 can't be divided try another number")
    given_number1 = int(input("Enter one number: "))
    check_number1 = int(input("Enter the number you want to divide with: "))
    check(given_number1, check_number1)
