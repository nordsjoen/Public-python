#Hangman -made by nordsjoen

import random
import os

#function to clear terminal
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

word_list = ["actor", "advice", "airport", "alarm", "bait", "ball", "bedroom",
"boat", "car", "cat", "coal", "clock", "python"]


def hangly(into):
    state =["_______ ", # 0
           "|/",        # 1
           "|/    |",   # 2
           "|     O",   # 3
           "|     |",   # 4
           "|    /|\\", # 5
           "|    / \\", # 6
           "|",         # 7
           "____" ]     # 8


    print_list = [[0, 2, 3, 5, 6, 7], # 0 dead
                  [0, 2, 3, 5, 7, 7], # 1
                  [0, 2, 3, 4, 7, 7], # 2
                  [0, 2, 3, 7, 7, 7], # 3
                  [0, 2, 7, 7, 7, 7], # 4
                  [0, 1, 7, 7, 7, 7], # 5
                  [8, 1, 7, 7, 7, 7]] # 6 or more guesses left
    if into > 6:
        into = 6

    for i in print_list[into]:
        print(state[i])


def game():

    hangmanword = str(random.sample(word_list, k=1))
    hangmanword = hangmanword.strip("'[]")

    guesses = 6
    wrong = ""
    hangman = []
    hidden = []

    print(f"\nOk lets start :)  Word lenght is: {len(hangmanword)}")

    #For-loop to hide the hangman word
    for words in hangmanword:
        hidden.append("_")

    #Hidden list to used for indexing later where the letter should be written.
    for words in hangmanword:
        hangman.append(words)

    while True:
        #For-loop to transfr corecctly entered words from a list into a string
        hidden_strip = ""
        for i in hidden:
            hidden_strip = hidden_strip + i

        print(f"You have {guesses} more guesses")
        print(f"Word: {hidden_strip}\n")

        hangly(guesses) # Prints hangman
        guess = input("Please enter a letter :").lower()

        try:
            # Spellchecker
            if len(guess) > 1 or not guess.isalpha() or not guess.islower():

                clear()
                print(f"\nOnly 1 lowercase letter, no numbers or symbols... Try again..    Wrongly gussed words:{wrong}")

            #Else-if to check if the user has tried the letter before
            elif hidden.count(guess) >= 1 or wrong.count(guess) >= 1:

                clear()
                print(f"You have already guessed: {guess}    Wrongly gussed words:{wrong}\n")

            #Else-if to check if the letter is correct
            elif hangmanword.count(guess) >= 1:

                clear()
                print(f"\nCORRECT! You entered: {guess}   Wrongly gussed words:{wrong}")

                #For-loop to check if it is more than 1 of the same letter,
                #enters the letters into a list.hidden in correct order/index.
                for i in range(hangmanword.count(guess)):

                    hidden[hangman.index(guess)] = guess
                    hangman[hangman.index(guess)] = "_"
            #Else-if if the user guessed wrong.
            elif hangmanword.count(guess) == 0:

                guesses = guesses - 1
                wrong = wrong + guess

                clear()
                print(f"\nWrongly guessed letters: {wrong}")


        finally:
            #To check if the user has more turns, if not, print the hangword and break
            if guesses == 0:
                print("You lost.")
                print(f"Correct word:{hangmanword}\n")
                hangly(guesses)
                break

            #Else-if for when the user wins :)
            elif hidden.count("_") == 0:
                print("You won!")
                print(f"Correct word:{hangmanword}\n")
                hangly(guesses)
                break



#Software starts here:
clear()
print("\nLet's play hangman\n")

#Loop to check if the player wants to keep playing or not.
while True:

    play = input("Do you want to play yes or no: ").lower()

    if play == "yes":

        clear()
        game()

    elif play == "no":

        print("Ok... \n\n\nBYE!")
        exit()

    else:

        print("Please enter 'yes' or 'no'")
