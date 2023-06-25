import random

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)

user_choice = input("select either rock, paper or scissors: ")

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("Draw. Try again.")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")