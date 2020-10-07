import random

generated_number = random.randint(1, 9)
human_guess = 0
count = 0

while human_guess != generated_number and human_guess != "exit":
    guess = int(input("What's your guess?"))

    if guess == "exit":
        break

    human_guess = guess
    count += 1

    if guess < generated_number:
        print("Too low!")
    elif guess > generated_number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you", count, "tries!")


