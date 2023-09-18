############### Blackjack Project #####################
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
##! Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
import time
import art

tokens = 1000

print("1. Blackjack")
game_choice = input("Choose: ")
if game_choice == "1":
  with_tokens = input(
    "Play with tokens 🪙  ('\033[93myes\033[0m' or '\033[96mno\033[0m'): ")
while game_choice == "1":
  os.system("clear")
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  person_cards = []
  dealer_cards = []
  score = 0
  dealer_score = 0

  if with_tokens == "yes":
    print(art.logo)
    bet = int(input("\nChoose your bet: "))
    os.system("clear")

  for card in range(2):
    person_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

  blackjack = True
  while blackjack:
    score = sum(person_cards)
    print(art.logo)
    if with_tokens == "yes":
      print(f"  Your tokens: \033[34m{tokens}\033[0m  Your bet: \033[94m{bet}\033[0m\n")
    print(f"  Your cards: {person_cards}  Score: \033[95m{score}\033[0m")
    print(f"  Dealer first card: \033[35m{dealer_cards[0]}\033[0m")
    if score >= 21:
      blackjack = False
    else:
      blackjack_choice = input("\n'hit' or 'stand': ")
      if blackjack_choice == "hit":
        person_cards.append(random.choice(cards))
        score = sum(person_cards)
        if score >= 21:
          if 11 in person_cards and score > 21:
            person_cards[person_cards.index(11)] = 1
          else:
            blackjack = False
      elif blackjack_choice == "stand":
        blackjack = False
      else:
        print("\033[91mThere is no such an option!\033[0m")
        time.sleep(1)
    os.system("clear")

  dealer_score = sum(dealer_cards)

  while dealer_score <= 17:
    dealer_cards.append(random.choice(cards))
    dealer_score = sum(dealer_cards)

  print(art.logo)
  #dealer_cards = [11, 10]
  #person_cards = [11, 10]
  score = sum(person_cards)
  dealer_score = sum(dealer_cards)
  if with_tokens == "yes":
    print(f"  Your tokens: \033[34m{tokens}\033[0m")
  print(f"  Your final hand: {person_cards}  Score: \033[95m{score}\033[0m")
  print(
    f"  Dealer hand: {dealer_cards}  Score: \033[35m{dealer_score}\033[0m\n")

  if (score > dealer_score and score <= 21) or (score <= 21
                                                and dealer_score > 21):
    if score == 21 and len(person_cards) <= 2:
      print("\033[01m\033[92mYou win with Blackjack!💎🤑\033[0m")
      if with_tokens == "yes":
        print(f"\033[92m+{bet}\033[0m")
      tokens +=bet
    else:
      print("\033[92mYou win!🤑\033[0m")
      if with_tokens == "yes":
        print(f"\033[92m+{bet}\033[0m")
      tokens +=bet
  elif score == dealer_score:
    if len(person_cards) <= 2 and score == 21 and dealer_score == 21 and len(
        dealer_cards) <= 2:
      print("\033[01m\033[36mIt's a draw with two blackjacks!🍀🍀🍀\033[0m")
    else:
      print("\033[36mIt's a draw!\033[0m")
  else:
    print("\033[31mYou loose!😞\033[0m")
    if with_tokens == "yes":
        print(f"\033[31m-{bet}\033[0m")
    tokens -=bet

  if input(
      "\nPlay again ('\033[32myes\033[0m' or '\033[31mno\033[0m'): ") == "no":
    game_choice = 0
