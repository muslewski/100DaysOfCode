import random


class fg:
    #red = '\033[31m'
    #green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'


#chatgpt generated below
colors = [
    getattr(fg, color) for color in dir(fg)
    if not callable(getattr(fg, color)) and not color.startswith("__")
]
random_color = random.choice(colors)
random_color2 = random.choice(colors)
random_color3 = random.choice(colors)
random_color4 = random.choice(colors)
random_color5 = random.choice(colors)

logo = f"""
  _____________________
 |  _________________  |
 | | Welcome!     0. | |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | {random_color}+\033[00m | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | {random_color2}-\033[00m | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | {random_color3}*\033[00m | |
 | |___|___|___| |___| |
 | | . | 0 | = | | {random_color4}/\033[00m | |
 | |___|___|___| |___| |
 |_____________________|
"""
