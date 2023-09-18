# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("black","green")
# timmy.forward(199)
#
# Screen().exitonclick()

from prettytable import PrettyTable
from colorama import init, Fore
init(autoreset=True)

table = PrettyTable()
print(Fore.BLUE+ "BLUE ONE")


table.add_column(Fore.LIGHTRED_EX + "Pokemons:" + Fore.RESET,["Pikachu","Charmander", "Squirtle", "Bulbasaur"])
table.add_column(Fore.MAGENTA + "Nature:" + Fore.RESET, ["Electricy", "Fire", "Water", "Earth"])
table.align = "l"
print(table)
