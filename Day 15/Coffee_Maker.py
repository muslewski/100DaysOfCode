import art
import dialogue
import os
import time
import sys
import random

# Make 3 hot flavours
# Espresso, Latte, Cappuccino
# Espresso - 50ml Water and 18g Coffe //1.50$
# Latte = 200ml Water, 24g Coffe and 150ml Milk //2.50$
# Cappuccino = 250ml Water, 24g Coffe, 100ml Milk //3.00$

# Coffe machine resources: 300ml water, 200ml milk, 100g coffe
# Coin operated: Penny - 1cent, Nickel - 5cents, Dime - 10cents, Quarter - 25cents

# Program requirements:
# 1. Print report
# 2. Check Resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee.

# TODO: 3. Charge the value. and remove used ingredients.
# TODO: 4. Give coffee to clients and get tips.
# TODO: 5. Boss told you about new client, and you serve again.

MENU = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  }
}

resources = {"water": 300, "milk": 200, "coffee": 100}

BUDGET = 20
HAND = []


def load_animation():
  # String to be displayed when the application is loading
  load_str = "Making your drink..."
  ls_len = len(load_str)

  # String for creating the rotating line
  animation = "|/-\\"
  anicount = 0

  # used to keep the track of
  # the duration of animation
  counttime = 0

  # pointer for travelling the loading string
  i = 0

  # List of RGB color codes for chroma effect
  color_palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                   (0, 255, 255), (255, 0, 255)]

  while counttime != 100:

    # used to change the animation speed
    # smaller the value, faster will be the animation
    time.sleep(0.075)

    # Choose a random color from the palette
    r, g, b = random.choice(color_palette)

    # converting the string to list
    # as string is immutable
    load_str_list = list(load_str)

    # x->obtaining the ASCII code
    x = ord(load_str_list[i])

    # y->for storing altered ASCII code
    y = 0

    # if the character is "." or " ", keep it unaltered
    # switch uppercase to lowercase and vice-versa
    if x != 32 and x != 46:
      if x > 90:
        y = x - 32
      else:
        y = x + 32
      load_str_list[i] = chr(y)

    # for storing the resultant string
    res = ''
    for j in range(ls_len):
      res = res + load_str_list[j]

    # displaying the resultant string with color
    sys.stdout.write(
      f"\r\033[38;2;{r};{g};{b}m{load_str}\033[0m{animation[anicount]}")

    sys.stdout.flush()

    # Assigning loading string
    # to the resultant string
    load_str = res

    anicount = (anicount + 1) % 4
    i = (i + 1) % ls_len
    counttime = counttime + 1


def main_menu():
  print(art.logo)
  print("\nHello new worker!")
  print("Your job is to make coffee for our boss and his clients.")
  input("\nPress enter to start...\n")


def boss_office():
  print(art.office)
  print(dialogue.boss_say)
  time.sleep(2)
  print(f"\nYou: {dialogue.response}")
  input("\n\033[90mPress enter to go to Coffe Machine...\033[0m\n")


def coffe_machine():
  global BUDGET
  global HAND
  os.system("clear")
  print(art.coffe_machine)
  if resources["water"] < 0:
    print("Please refil water!")
  if resources["milk"] < 0:
    print("Please refil milk!")
  if resources["coffee"] < 0:
    print("Please refil coffe!")
  machine_input = input("What would you like: ").lower()
  if machine_input == "espresso":
    resources["water"] -= 50
    resources["coffee"] -= 18
    price = 1.5
    HAND.append("Espresso")
  elif machine_input == "latte":
    resources["water"] -= 200
    resources["coffee"] -= 24
    resources["milk"] -= 150
    price = 2.5
    HAND.append("Latte")
  elif machine_input == "cappuccino":
    resources["water"] -= 250
    resources["coffee"] -= 24
    resources["milk"] -= 100
    price = 3.0
    HAND.append("Cappuccino")
  elif machine_input == "hot chocolate":
    price = 4.5
    HAND.append("hot chocolate")
    resources["water"] -= 100

    resources["coffee"] -= 8
  elif machine_input == "report":
    print(resources)
    time.sleep(2)
    coffe_machine()
  elif machine_input == "refil":
    resources["water"] = 300
    resources["coffee"] = 100
    resources["milk"] = 200
    print("Coffee machine refiled!")
    print(resources)
    time.sleep(2)
    coffe_machine()
  else:
    print("There is no such an option")
    time.sleep(1)
    os.system("clear")
    coffe_machine()

  if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
    print("Not enough ingredients! Please refil!")
    time.sleep(1.5)
    os.system("clear")
    coffe_machine()

  print("Please insert coins.")
  sum_coins = 0
  quarters = int(input("How many quarters (0.25$): "))
  sum_coins += 0.25 * quarters
  if sum_coins >= price:
    print("that's enough!")
  else:
    dimes = int(input("How many dimes (0.10$): "))
    sum_coins += 0.10 * dimes
    if sum_coins >= price:
      print("that's enough!")
    else:
      nickles = int(input("How many nickles (0.05$): "))
      sum_coins += 0.05 * nickles
      if sum_coins >= price:
        print("that's enough!")
      else:
        pennys = int(input("How many Penny (0.01$): "))
        sum_coins += 0.01 * pennys
        if sum_coins >= price:
          print("that's enough!")
        else:
          print("You put in too few coins. Try again!")
          time.sleep(1)
          os.system("clear")
          coffe_machine()

  BUDGET -= price
  change = sum_coins - price
  print(f"\nHere is {change} in change. You have left {BUDGET}$!")
  load_animation()
  print(f"\n\nHere is your {HAND[0]} ☕️. Enjoy!")
  choice = input("Make another one? ('yes' or 'no'): ")
  if choice == "yes":
    coffe_machine()
  elif choice == "no":
    exit()
  else:
    print("There is no such an option!")
    time.sleep(1)
    os.system("clear")


main_menu()
os.system("clear")
boss_office()
time.sleep(1)
os.system("clear")
coffe_machine()
print("This looks so delicious, should I drink it or give it to my boss...")
