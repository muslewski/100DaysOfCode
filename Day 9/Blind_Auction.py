from replit import clear
import art

print(art.logo)

play = True
data = {}
highest = 0

while play:
    name = input("What is your name: ")
    price = int(input("What is your bid: $"))
    data[name] = price

    for person in data:
        if data[person] > highest:
            highest = data[person]
            winner = person

    choice = input("Are there any other players? 'yes' or 'no': ")
    if choice == "no":
        play = False
    clear()

print(f"The winner is {winner} with a bid of ${highest}")
