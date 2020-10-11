# Write a program that asks the user how many Fibonnaci numbers to generate and
# # then generates them. Take this opportunity to think about how you can use functions.
# # Make sure to ask the user to enter the number of numbers in the sequence to generate.
# # (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
# # the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibonacci(num):
    num2 = 1
    series = 0
    my_list = []
    for i in range(num):
        my_list.append(series)
        num1 = num2
        num2 = series
        series = num1 + num2
    print(my_list)


# running function after taking user input
num = int(input('Enter how many numbers needed in Fibonacci series-: '))
fibonacci(num)
