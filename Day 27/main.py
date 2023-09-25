from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label1 = Label(text="                ")
my_label1.grid(column=1, row=0)

my_label["text"] = "test"
my_label.config(text="test2")


# Button

def button_clicked():
    my_label["text"] = input_entry.get()


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry

input_entry = Entry(width=10)
input_entry.grid(column=3, row=2)
input_entry.get()


window.mainloop()
