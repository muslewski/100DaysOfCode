import art
import os


#Add
def add(x, y):
    return x + y


#Substract
def substract(x, y):
    return x - y


#Multiply
def multiply(x, y):
    return x * y


#Divide
def divide(x, y):
    return x / y


operations = {"+": add, "-": substract, "*": multiply, "/": divide}

print(art.logo)


def calculator():
    num1_unverified = input("First number: ")
    try:
        num1 = float(num1_unverified)
        error = True
    except ValueError:
        num1 = "\033[31mundefined\033[0m"
        error = False

    join = True

    while join:
        operation_symbol = input(
            f"Operation from {art.random_color5}colored\033[00m above: ")
        num2_unverified = input("Next number: ")

        try:
            num2 = float(num2_unverified)
            error2 = True
        except ValueError:
            num2 = "\033[31mundefined\033[0m"
            error = False

        answer = "\033[31mI don't know!\033[0m"

        if error and error2:
            for symbol in operations:
                if operation_symbol == symbol:
                    answer = operations[symbol](num1, num2)

        print(f"\n{num1} {operation_symbol} {num2} = \033[32m{answer}\033[0m")
        if input("\nContinue - 'y' New - 'n': ") == "y":
            num1 = answer
            print("")
        else:
            join = False
            os.system("clear")
            calculator()


calculator()
