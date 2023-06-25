import random

num_range = []

for i in range(1, 101):
    num_range.append(i)

program_choice = int(random.choice(num_range))

def number_game():
    print("Let's play a game!")
    print("I'll come up with a random number between 1 to 100 and you have to guess what it is.")
    print("I'll tell you if you're answer is too high or too low until you get it correct.")

    while True:
        user_choice = int(input("Now, what do you think is the number?: "))
        if user_choice == program_choice:
            print("That is correct! Good Job!")
            break
        elif user_choice > program_choice:
            print("You're too high. Try again.")
        elif user_choice < program_choice:
            print("You're too low. Try again.")
        else:
            print("Please enter a valid number.")

number_game()