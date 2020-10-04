# Create a program that asks the user for a number from 1 to 100 and
# then prints out a list of all the divisors of that number.

given_number = int(input("Enter the number for division: "))


def print_the_divisors(user_number):
    my_list = []
    for num in range(1, 101):
        if num % user_number == 0 and user_number != 0:
            my_list.append(num)
    return my_list


print(print_the_divisors(given_number))
