#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import os
import time


def start():
    print("""\033[30m
     _____                        _   _                 _               
    / ____|                      | \ | |               | |              
   | |  __ _   _  ___  ___ ___   |  \| |_   _ _ __ ___ | |__   ___ _ __ 
   | | |_ | | | |/ _ \/ __/ __|  | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
   | |__| | |_| |  __/\__ \__ \  | |\  | |_| | | | | | | |_) |  __/ |   
    \_____|\__,_|\___||___/___/  |_| \_|\__,_|_| |_| |_|_.__/ \___|_|
  \033[0m""")

    print("  Welcome to the number guessing game!!!")
    print("  I'm thinking of a number between 1 and 100.")
    print(f"  psst the correct answer is {answer}\n")


def game():
    option_is_wrong = True
    attempts = 0
    while option_is_wrong:
        difficulty = input("Choose a difficulty. 'easy' or 'hard': ")
        if difficulty == "easy":
            attempts = 10
            option_is_wrong = False
        elif difficulty == "hard":
            attempts = 5
            option_is_wrong = False
        else:
            print("\033[91mThere is no such an option!\033[0m")
            option_is_wrong = True
            time.sleep(1)
            os.system("clear")
            start()

    guess = 0
    win_status = False
    while guess != answer:
        os.system("clear")
        start()
        print(f"You have {attempts} attempts ramaining to guess the number!")
        guess = input("Make a guess: ")

        if guess.isdigit() == True:
            guess = int(guess)
            if guess < answer:
                print("Too low!")
                time.sleep(1)
                attempts -= 1
            elif guess > answer:
                print("Too high!")
                attempts -= 1
                time.sleep(1)
            else:
                os.system("clear")
                start()
                print(f"\033[92mYou win with {attempts} attempts left!\033[0m")
                win_status = True
                break
        else:
            print("\033[91mWrong guess!\033[0m")
            time.sleep(1)
            attempts -= 1

        if attempts < 1:
            os.system("clear")
            start()
            print("\033[31mYou've run out of guesses, you loose!\033[0m")
            break


play_again = True
while play_again:
    answer = random.randint(1, 100)
    start()
    game()
    again = input("\n Play again? 'yes' or 'no': ")
    if again == "no":
        play_again = False
        break
    
    while again != "yes":
        print("\033[91mThere is no such an option!\033[0m")
        time.sleep(1)
        os.system("clear")
        start()
        again = input("\n Play again? 'yes' or 'no': ")
    os.system("clear")
