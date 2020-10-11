# Creating the list of divisors from 2 to 101.
divisors_list = list(range(2, 101))
# Creating a new list that will hold the
# numbers that will not pass our test which will be the prime numbers.
list_of_primes = []
# Declaring the variable counter that will allow me to control how many entries
# do i want to make.
counter = 0
while counter < 5:
    # Getting input from the user!
    scanner = int(input("Enter any integer number you want: "))
    # In this loop i will check the number that user entered can be divided by any of
    # the numbers we have in divisors_list.
    for num in divisors_list:
        # The number will be tested on remainder and at the same time i removed the
        # division between same numbers.In case that the number will not be able to pass
        # the test than it will be appended to the list of primes.
        if scanner % num == 0 and scanner != num:
            break
    else:
        list_of_primes.append(scanner)
        print(f"Number {scanner} is a prime number!")
    # Incrementing our counter to make sure we don't run in the infinite loop.
    counter += 1
print(f"Here is the list of prime numbers: {list_of_primes}")
