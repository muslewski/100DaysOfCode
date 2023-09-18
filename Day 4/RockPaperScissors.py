rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gun = '''
      __,_____
     / __.==--"
    /#(-'
    `-'
'''

#Write your code below this line 👇

import random
import os

wins = 0
losses = 0
draws = 0


def displayIntro():
    global wins
    global losses
    global draws

    print(
        f"\033[32mYour wins: {wins}, \033[31mYour losses: {losses}, \033[34mYour draws: {draws}\033[0m"
    )

    player_choice = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
        ))

    if player_choice == 0:
        print(f"\nYour choice is: {rock}")
    elif player_choice == 1:
        print(f"\nYour choice is: {paper}")
    elif player_choice == 2:
        print(f"\nYour choice is: {scissors}")
    elif player_choice == 9:
        print(f"\nYour choice is: {gun}")
    else:
        print("There is no such an option!")
        exit()

    bot_choice = random.randint(0, 2)
    if bot_choice == 0:
        print(f"\nBot choice is: {rock}")
    elif bot_choice == 1:
        print(f"\nBot choice is: {paper}")
    elif bot_choice == 2:
        print(f"\nBot choice is: {scissors}")

    if player_choice == 0 and bot_choice == 0:
        print("\n\033[34mYou draw")
        draws += 1

    elif player_choice == 0 and bot_choice == 1:
        print("\n\033[31mYou lose")
        losses += 1

    elif player_choice == 0 and bot_choice == 2:
        print("\n\033[32mYou win!")
        wins += 1

    elif player_choice == 1 and bot_choice == 0:
        print("\n\033[32mYou win!")
        wins += 1

    elif player_choice == 1 and bot_choice == 1:
        print("\n\033[34mYou draw")
        draws += 1

    elif player_choice == 1 and bot_choice == 2:
        print("\n\033[31mYou lose")
        losses += 1

    elif player_choice == 2 and bot_choice == 0:
        print("\n\033[31mYou lose")
        losses += 1

    elif player_choice == 2 and bot_choice == 1:
        print("\n\033[32mYou win!")
        wins += 1

    elif player_choice == 2 and bot_choice == 2:
        print("\n\033[34mYou draw")
        draws += 1

    elif player_choice == 9:
        print("\n\033[35mYou killed your opponent!")
        wins = 999
        losses = -999
        draws = -999


playagain = 'yes'
while playagain == 'yes':
    displayIntro()
    print('\033[0mDo you want to play again? (yes or no)')
    playagain = input()
    os.system('clear')
