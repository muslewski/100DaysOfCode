print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride!")
  age = input("What is your age? ")
  if(int(age)<12):
    print("You need to pay $5")
  elif(int(age)<18):
    print("You need to pay $7")
  else:
    print("You need to pay $12")
else:
  print("You cant ride")
