from menu import Menu  # , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from alive_progress import alive_bar
from time import sleep
from os import system

is_on = True

machine = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


while is_on:

    order = input(f"What would you like? {machine.get_items()}: ").lower()
    if order == "off":
        with alive_bar(100, bar='solid') as bar:
            for i in range(100):
                sleep(0.02)
                bar()
        print("Successful Shutdown!")
        sleep(2)
        system("cls")
        is_on = False
    elif order == "report":
        with alive_bar(100, bar='filling') as bar:
            for i in range(100):
                sleep(0.02)
                bar()
        coffee.report()
        money.report()
        sleep(2)
        system("cls")

    elif machine.find_drink(order):
        drink = machine.find_drink(order)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            with alive_bar(100, bar='bubbles') as bar:
                for i in range(100):
                    sleep(0.02)
                    bar()
            coffee.make_coffee(drink)
            sleep(2)
            system("cls")
        else:
            sleep(2)
            system("cls")
    else:
        sleep(2)
        system("cls")
