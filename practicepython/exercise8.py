import random


# TO be continued....

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


def computer_choice():
    made_options = ["Rock", "Paper", "Scissors"]
    random_option = random.randint(0, 2)
    computer = made_options[random_option]
    return computer.lower()


def human_choice():
    choise = input("Enter rock or paper or scissors: ")
    human_option = choise
    print(f"Human picked: {human_option}")
    print(f"Computer picked: {computer_choice()}")

    return human_option.lower()


def continue_or_exit():
    while True:
        y_or_n = input("Do you want to play another game? y or n \t")
        if y_or_n in ["Yes", "Y", "y", "yes"]:
            print(do_the_game(computer_choice(), human_choice()))
        else:
            break
    return ""


computer_score = 0
human_score = 0


def do_the_game(comp_opt, human_opt):
    global computer_score
    global human_score
    if comp_opt == human_opt:
        print("Thats Equality!, no points allocated!")
    if comp_opt == "rock" and human_opt == "scissors":
        print("You lost!")
        computer_score += 1
    elif comp_opt == "rock" and human_opt == "paper":
        print("You won!")
        human_score += 1
    elif comp_opt == "paper" and human_opt == "rock":
        print("You lost!")
        computer_score += 1
    elif comp_opt == "paper" and human_opt == "scissors":
        print("You won!")
        human_score += 1
    elif comp_opt == "scissors" and human_opt == "rock":
        print("You won!")
        human_score += 1
    elif comp_opt == "scissors" and human_opt == "paper":
        print("You lost!")
        computer_score += 1
    return computer_score, human_score


do_the_game(computer_choice(), human_choice())
print("Computer score: " + str(computer_score) + "\n" + "Human score: " + str(human_score))
continue_or_exit()

# while True:
#     print(do_the_game(computer_choice(),human_choice()))
#     continue_or_exit()
#     if True:
#         print(do_the_game(computer_choice(), human_choice()))
#     else:
#         break


# choise = input("Enter rock or paper or scissors: ")
# made_options = ["Rock", "Paper", "Scissors"]
# random_option = random.randint(0, 2)
# game_rule = {
#     "Rock": "Paper",
#     "Paper": "Scissors",
#     "Scissors": "Rock"
# }
#
#
# def rock_paper_scissors_game(option):
#     if option in game_rule[computer_choice()]:
#         return "you won!"
#     else:
#         return "You lose!"
#
#
# print(rock_paper_scissors_game(choise))
