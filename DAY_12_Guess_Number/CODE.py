from random import randint
from ART import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to check users guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


#Make a function to set difficulty Level
def set_diffitculty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a random number between 1 and 100
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_diffitculty()

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))
        #Track the number of turns and reduce by 1 if they het it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you LOSE.")
            return


game()
