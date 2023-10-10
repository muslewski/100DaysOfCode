from tkinter import *
from tkinter.ttk import Progressbar

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/en_pl_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient='records')

generating_card = False

def generate_card():
    global generating_card, current_card
    if generating_card:
        return

    current_card = random.choice(data_dict)
    canvas.itemconfig(language_item, text="English", fill="black")
    canvas.itemconfig(text_item, text=current_card["Angielski"], fill="black")
    canvas.itemconfig(canvas_image, image=white_a4)
    generating_card = True
    progress_bar.start(30)

    def flip_card():
        global generating_card
        canvas.itemconfig(language_item, text="Polish", fill="white")
        canvas.itemconfig(text_item, text=current_card["Polski"], fill="white")
        canvas.itemconfig(canvas_image, image=green_a4)

        generating_card = False
        progress_bar.stop()

    window.after(3000, flip_card)

def is_known():
    data_dict.remove(current_card)
    datas = pandas.DataFrame(data_dict)
    datas.to_csv("words_to_learn.csv", index=False)
    generate_card()


window = Tk()
window.minsize(800, 750)
window.title("Smart Bites")
window.iconbitmap("images/icon_flash_cards.ico")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

white_a4 = PhotoImage(file="images/card_front.png")
green_a4 = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(0, 0, image=white_a4, anchor=NW)
language_item = canvas.create_text(400, 150, text="", font=("Ariel", 25, "italic"))
text_item = canvas.create_text(400, 253, text="Ready?", font=("Ariel", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

good_image = PhotoImage(file="images/right.png")
bad_image = PhotoImage(file="images/wrong.png")
good = Button(image=good_image, highlightthickness=0, borderwidth=0, command=is_known)
bad = Button(image=bad_image, highlightthickness=0, borderwidth=0, command=generate_card)

progress_bar = Progressbar(window, mode='determinate', length=300)
progress_bar.grid(column=1, row=1)

bad.grid(column=0, row=1)
good.grid(column=2, row=1)

generate_card()


window.mainloop()
