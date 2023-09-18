import art
import game_data
import random
import os
import time


def welcome():
  #First part
  print(art.logo)
  time.sleep(0.5)
  text = "Hello there! Try to get 5 points!"
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(0.02)
  time.sleep(2.5)
  os.system("clear")


POINTS = 0
HIGHEST = 0
RECORD = 0


def loop():

  def header():
    print(art.logo)

  POINTS = 0
  A_number = random.randint(0, len(game_data.data) - 1)
  B_number = random.randint(0, len(game_data.data) - 1)

  def compare(A_number, B_number):
    global POINTS
    global HIGHEST
    global RECORD

    if RECORD > HIGHEST:
      HIGHEST = RECORD

    if POINTS > 0:
      A_number = B_number
      B_number = random.randint(0, len(game_data.data) - 1)

    A_followers = game_data.data[A_number]["follower_count"]
    B_followers = game_data.data[B_number]["follower_count"]
    #Make sure that there is no the same numbers
    while B_number == A_number or A_followers == B_followers:
      B_number = random.randint(0, len(game_data.data) - 1)

    A_name = game_data.data[A_number]["name"]
    B_name = game_data.data[B_number]["name"]
    #A_followers = game_data.data[A_number]["follower_count"]
    B_followers = game_data.data[B_number]["follower_count"]
    A_description = game_data.data[A_number]["description"]
    B_description = game_data.data[B_number]["description"]
    A_localization = game_data.data[A_number]["country"]
    B_localization = game_data.data[B_number]["country"]

    A_result = f"\n\033[96mCompare A\033[0m: {A_name}, {A_description}, from {A_localization}"
    B_result = f"\033[96mAgainst B\033[0m: {B_name}, {B_description}, from {B_localization}"

    print(A_result)
    print(art.vs)
    print(B_result)

    choice = ""
    while choice != "a" and choice != "b":
      choice = input("\nWho has more followers? ('A' or 'B'): ").lower()
      if choice == "a":
        if A_followers > B_followers:
          POINTS += 1
          os.system("clear")
          header()
          RECORD = POINTS
          if RECORD > HIGHEST:
            HIGHEST = RECORD
          print(
            f"\033[92mYou're right!\033[0m Current score: {POINTS}. Your record: {HIGHEST}"
          )
          compare(A_number, B_number)

        else:
          os.system("clear")
          header()
          print(
            f"\033[91mThat is wrong!\033[0m\nFinal score: {POINTS}! Your record: {HIGHEST}"
          )
          RECORD = POINTS
          POINTS = 0
          play_again = input("\nDo you want to play again? 'yes' or 'no': ")
          if play_again == "yes":
            os.system("clear")
            loop()
          else:
            exit()

      elif choice == "b":
        if B_followers > A_followers:
          POINTS += 1
          os.system("clear")
          header()
          RECORD = POINTS
          if RECORD > HIGHEST:
            HIGHEST = RECORD
          print(
            f"\033[92mYou're right!\033[0m Current score: {POINTS}. Your record: {HIGHEST}"
          )
          compare(A_number, B_number)

        else:
          os.system("clear")
          header()
          print(
            f"\033[91mThat is wrong!\033[0m\nFinal score: {POINTS}! Your record: {HIGHEST}"
          )
          RECORD = POINTS
          POINTS = 0
          play_again = input("\nDo you want to play again? 'yes' or 'no': ")
          if play_again == "yes":
            os.system("clear")
            loop()
          else:
            exit()

      else:
        print("Choose between A and B!")

  header()
  compare(A_number, B_number)


welcome()
loop()
