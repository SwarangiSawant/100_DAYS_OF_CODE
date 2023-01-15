#HOW TO CHECK USER'S ANSWER

word_list=["ardvark", "baboon", "camel"]

#TODO_1 Randomly choose a word from the word_list and to assign it to a variable called chosen_word
import random

chosen_word=random.choice(word_list)

#TODO_2 Ask the user to guess a letter and assign their answer to a variable called guess.Make guess lowercase.
guess=input("Guess a letter: ").lower()

#TODO_3 Check if the letters in the choosen_word.
for letter in chosen_word:
  if letter==guess:
    print("Right")
  else:
    print("Wrong")