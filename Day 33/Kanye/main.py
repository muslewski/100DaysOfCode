from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data["quote"]
    if len(quote) > 50:
            canvas.itemconfigure(quote_text, text=quote, font=("Arial", 20, "bold"))
    elif len(quote) > 80:
        canvas.itemconfigure(quote_text, text=quote, font=("Arial", 18, "bold"))
    else:
        canvas.itemconfigure(quote_text, text=quote, font=("Arial", 30, "bold"))
    print(quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()