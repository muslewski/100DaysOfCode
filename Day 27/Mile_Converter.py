from tkinter import *

window = Tk()
window.title("Mile to Km Converter 🔥")
window.minsize(500, 300)
window.config(padx=20, pady=30)

user_input = Entry(width=20, font=("Arial", 14, "normal"))
user_input.grid(column=1, row=0, pady=20, padx=20)

third_label = Label(text="  Miles", font=("Arial", 22, "normal"))
third_label.grid(column=2, row=0, pady=20, padx=20)

first_label1 = Label(text="is equal to  ", font=("Arial", 22, "normal"))
first_label1.grid(column=0, row=1, pady=20, padx=20)

result = Label(text=f"0", font=("Arial", 22, "normal"))
result.grid(column=1, row=1, pady=20, padx=20)

third_label1 = Label(text="Km", font=("Arial", 22, "normal"))
third_label1.grid(column=2, row=1, pady=20, padx=20)


def calculate_km():
    if user_input.get().isdigit():
        result["text"] = float(user_input.get()) * 1.609344
        result.config(fg="green")
    else:
        result["text"] = "Invalid input!"
        result.config(fg="red")


calculate = Button(text="Calculate", font=("Arial", 18, "normal"), command=calculate_km)
calculate.grid(column=1, row=2, pady=20, padx=20)

window.mainloop()
