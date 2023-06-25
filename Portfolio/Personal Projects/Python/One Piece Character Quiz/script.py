import random

quiz_questions = [
    {
        "question": "What is the name of Luffy's pirate crew?",
        "options": ["Straw Hat Pirates", "Blackbeard Pirates", "Whitebeard Pirates", "Heart Pirates"],
        "answer": "Straw Hat Pirates"
    },
    {
        "question": "What devil fruit does enel have?",
        "options": ["Gum-Gum Fruit", "Rumble-Rumble fruit", "Flame-Flame fruit", "Ice-Ice fruit"],
        "answer": "Rumble-Rumble Fruit"
    },
    {
        "question": "How many children does Big Mom have?",
        "options": ["85", "3", "200", "45"],
        "answer": "85"
    },
    {
        "question": "Who has the highest recorded bounty in history?",
        "options": ["Kaido", "Charlotte Linlin", "Gol D. Roger", "Edward Newgate"],
        "answer": "Gol D. Roger"
    },
    {
        "question": "Who is the captain of the Straw Hat Pirates?",
        "options": ["Nami", "Sanji", "Luffy", "Chopper"],
        "answer": "Luffy"
    },
    {
        "question": "Who is the navigator of the Straw Hat Pirates?",
        "options": ["Sanji", "Zoro", "Luffy", "Nami"],
        "answer": "Nami"
    }
]

def ask_question(question):
    print(quiz_questions['question'])
    for i, options in enumerate, options in enumerate(quiz_questions['options']):
        print(f"{i + 1}: {options}")
    while True:
        user_input = input("Enter your answer (1-4): ")
        try:
            user_answer_index = int(user_input) - 1
            if user_answer_index < 0 or user_answer_index > 3:
                raise ValueError
            return quiz_questions['options'][user_answer_index]
        except ValueError:
            print("Invalid Input. Please try again.")

def main():
    print("Welcome to the One Piece Character quiz!")
    random.shuffle(quiz_questions)
    score = 0
    for question in quiz_questions:
        user_answer = ask_question(question)
        if user_answer == quiz_questions['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {quiz_questions['answer']}")
    print(f"The score is {score}/{len(quiz_questions)}")
    if score == len(quiz_questions):
        print("Perfect score!")
    elif score >= len(quiz_questions) * 0.7:
        print("Great job!")
    else:
        print("Better luck next time!")
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() == "y":
        main()
    else:
        print("Thank you for playing!")

main()

