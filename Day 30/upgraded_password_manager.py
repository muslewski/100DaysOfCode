from tkinter import *
from tkinter import messagebox, ttk
import pandas as pd
import secrets
import string
import pyperclip
import os
import json

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

popular_username = "10kento10@gmail.com"
FONT = ("Courier", 18, "bold")
EFONT = ("", 12, "bold")

# Status of Theme
with open("dark_theme_status.txt", "r") as file_txt:
    status_from_txt = file_txt.read()
    if status_from_txt.strip().lower() == "true":
        dark_theme_status = True
    else:
        dark_theme_status = False


# Status of Entry
def check_focus():
    if website_entry == window.focus_get():
        window.focus()
        website_entry.focus()
    elif user_entry == window.focus_get():
        window.focus()
        user_entry.focus()
    elif password_entry == window.focus_get():
        window.focus()
        password_entry.focus()


# ---------------------------- MENU FUNCTIONS ------------------------------- #

def menu_commands():
    menu = Menu(window, bg="black")
    window.config(menu=menu)

    password_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Passwords", menu=password_menu)
    password_menu.add_command(label="Remove All Passwords", command=remove_passwords)
    password_menu.add_command(label="View Passwords", command=view_passwords)
    password_menu.add_command(label="Change Passwords", command=edit_file)

    settings_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Settings", menu=settings_menu)

    theme_submenu = Menu(settings_menu, tearoff=0)
    settings_menu.add_cascade(label="Change Theme", menu=theme_submenu)

    theme_submenu.add_command(label="Light", command=light_theme)
    theme_submenu.add_command(label="Dark", command=dark_theme)

    settings_menu.add_command(label="Language", command=dummy_function)
    settings_menu.add_command(label="Logout", command=dummy_function)
    settings_menu.add_command(label="Switch User", command=dummy_function)

    security_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Security", menu=security_menu)
    security_menu.add_command(label="Change Master Password", command=dummy_function)
    security_menu.add_command(label="Lock Session", command=dummy_function)
    security_menu.add_command(label="Password Generator", command=dummy_function)
    security_menu.add_command(label="Two-Factor Authentication", command=dummy_function)
    security_menu.add_command(label="Secure Password File", command=dummy_function)

    import_export_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Import/Export", menu=import_export_menu)
    import_export_menu.add_command(label="Export Passwords", command=dummy_function)
    import_export_menu.add_command(label="Import Passwords", command=dummy_function)

    history_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="History", menu=history_menu)
    history_menu.add_command(label="Activity Log", command=dummy_function)

    statistics_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Statistics", menu=statistics_menu)
    statistics_menu.add_command(label="Password Analytics", command=dummy_function)

    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=dummy_function)
    help_menu.add_command(label="Contact Support", command=dummy_function)


def remove_passwords():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to remove all passwords?")
    if confirm:
        print("Remove Passwords")
        with open('pass.txt', 'w'):
            pass


def view_passwords():
    # Create a new window
    password_window = Tk()
    password_window.title("View Passwords")

    # Load data from the pass.txt file into the DataFrame
    try:
        data = pd.read_csv("pass.txt", sep=" \| ", header=None, engine='python')
    except FileNotFoundError:
        # Handle the situation when the file does not exist
        label = Label(password_window, text="File pass.txt does not exist!")
        label.pack()
        return

    # Display data in table form
    tree = ttk.Treeview(password_window, columns=("Website", "Email", "Password"), show="headings")
    tree.heading("Website", text="Website")
    tree.heading("Email", text="Email")
    tree.heading("Password", text="Password")

    for index, row in data.iterrows():
        website, email, password = row
        tree.insert("", "end", values=(website, email, password))

    tree.pack()

    password_window.mainloop()


# Function to open a file in edit mode
def edit_file():
    try:
        with open("pass.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        # Handle the situation when the file does not exist
        data = "File pass.txt does not exist!"

    edit_window = Tk()
    edit_window.title("Edit Passwords")

    # Text field for editing the file content
    text = Text(edit_window)
    text.insert("1.0", data)
    text.pack()

    # Button to save changes
    save_button = Button(edit_window, text="Save Changes", command=lambda: save_changes(text.get("1.0", "end-1c")))
    save_button.pack()

    edit_window.mainloop()


# Function to save changes to the file
def save_changes(new_data):
    with open("pass.txt", "w") as file:
        file.write(new_data)


def exit_app():
    window.destroy()


def dummy_function():
    pass


# ----------------------------  DARK THEME ------------------------------- #
def check_status_of_dark_theme():
    global dark_theme_status
    with open("dark_theme_status.txt", "w") as file_txt1:
        file_txt1.write(str(dark_theme_status))


# noinspection PyUnusedLocal
def change_cursor_style_dark(event):
    website_entry.config(insertwidth=2, insertbackground='blue')
    user_entry.config(insertwidth=2, insertbackground='blue')
    password_entry.config(insertwidth=2, insertbackground='blue')


def dark_theme():
    global website_label, user_label, password_label, dark_theme_status
    dark_theme_status = True
    check_status_of_dark_theme()
    window.configure(bg="#202020")
    canvas = Canvas(width=256, height=256, bg="#202020", highlightthickness=0)
    logo = PhotoImage(file=resource_path("cyber-crime.png"))
    canvas.create_image(128, 128, image=logo)
    canvas.grid(column=0, row=0, columnspan=3)
    window.logo = logo
    window.iconbitmap(resource_path("cyber-crime.ico"))
    website_label.config(bg="#202020", fg="#bf9bff")
    user_label.config(bg="#202020", fg="#bf9bff")
    password_label.config(bg="#202020", fg="#bf9bff")
    website_entry.config(bg="#120027", fg="white", highlightbackground="#3700b5")
    user_entry.config(bg="#120027", fg="white", highlightbackground="#3700b5")
    password_entry.config(bg="#120027", fg="white", highlightbackground="#3700b5")
    generate_password.config(bg="#645ff4", fg="white")
    search.config(bg="#645ff4", fg="white")
    add_button.config(bg="#645ff4", fg="white")
    website_entry.bind("<FocusIn>", change_cursor_style_dark)
    user_entry.bind("<FocusIn>", change_cursor_style_dark)
    password_entry.bind("<FocusIn>", change_cursor_style_dark)
    check_focus()


# ----------------------------  LIGHT THEME ------------------------------- #
# noinspection PyUnusedLocal
def change_cursor_style_light(event):
    website_entry.config(insertwidth=2, insertbackground='red')
    user_entry.config(insertwidth=2, insertbackground='red')
    password_entry.config(insertwidth=2, insertbackground='red')


def light_theme():
    global website_label, user_label, password_label, dark_theme_status
    dark_theme_status = False
    check_status_of_dark_theme()
    window.configure(bg="white")
    canvas = Canvas(width=256, height=256, bg="white", highlightthickness=0)
    logo = PhotoImage(file=resource_path("logo2.png"))
    canvas.create_image(128, 128, image=logo)
    canvas.grid(column=0, row=0, columnspan=3)
    window.logo = logo
    window.iconbitmap(resource_path("logo2.ico"))
    website_label.config(bg="white", fg="#7e0000")
    user_label.config(bg="white", fg="#7e0000")
    password_label.config(bg="white", fg="#7e0000")
    website_entry.config(bg="#fff4f4", fg="black", highlightthickness=2, highlightbackground="#ff8e8e")
    user_entry.config(bg="#fff4f4", fg="black", highlightthickness=2, highlightbackground="#ff8e8e")
    password_entry.config(bg="#fff4f4", fg="black", highlightthickness=2, highlightbackground="#ff8e8e")
    generate_password.config(bg="#ff5f5f", fg="white")
    search.config(bg="#ff5f5f", fg="white")
    add_button.config(bg="#ff5f5f", fg="white")
    website_entry.bind("<FocusIn>", change_cursor_style_light)
    user_entry.bind("<FocusIn>", change_cursor_style_light)
    password_entry.bind("<FocusIn>", change_cursor_style_light)
    check_focus()


# ---------------------------- AFTER ENTER CLICKED ------------------------------- #
# noinspection PyUnusedLocal
def website_entry_on_enter_pressed(event):
    user_entry.focus()


# noinspection PyUnusedLocal
def user_entry_on_enter_pressed(event):
    password_entry.focus()


# noinspection PyUnusedLocal
def password_entry_on_enter_pressed(event):
    get_pass()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    # Set the character set for password generation
    alphabet = string.ascii_letters + string.digits

    # Generate a password from letters and numbers
    password = ''.join(secrets.choice(alphabet) for _ in range(16))

    # Add special characters
    special_characters = string.punctuation
    password += ''.join(secrets.choice(special_characters) for _ in range(4))

    # Shuffle the password to mix special characters with letters and numbers
    password = ''.join(secrets.choice(password) for _ in range(len(password)))
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_pass():
    website_entry_text = website_entry.get()
    user_entry_text = user_entry.get()
    password_entry_text = password_entry.get()
    new_data = {
        website_entry_text: {
            "email": user_entry_text,
            "password": password_entry_text,
        }
    }

    if len(website_entry_text) == 0 or len(user_entry_text) == 0 or len(password_entry_text) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open('pass.json', 'r') as f:
                # json.dump(new_data, f, indent=4)
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open('pass.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            with open('pass.json', 'w') as f:
                json.dump(data, f, indent=4)


        website_entry.delete(0, END)
        password_entry.delete(0, END)

# Search
def find_password():
    website_entry_text = website_entry.get()
    try:
        with open('pass.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="This file does not exist")

    else:
        i = True
        for element in data:
            username = data[element]["email"]
            password = data[element]["password"]
            if website_entry_text.lower() == element.lower():
                messagebox.showinfo(title=f"{element}", message=f"Username: {username}\nPassword: {password}")
                i = False
        if i:
            messagebox.showinfo(title="Finder", message="Can't find any matching result...")


# ---------------------------- ENCRYPTED PASSWORDS -------------------------------
# #
# ---------------------------- UI OF LOGIN SCREEN ------------------------------- #


# ---------------------------- UI SETUP OF WIDGETS ------------------------------- #
def configure_widgets():
    # We set the weight of the column to maintain flexibility in stretching
    window.grid_columnconfigure(1, weight=1)
    # We set the vertical flexibility for all rows
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)

    website_label.grid(column=0, row=1, sticky="w")
    website_entry.grid(column=1, row=1, sticky=EW, padx=5, pady=5)
    website_entry.bind("<Return>", website_entry_on_enter_pressed)
    website_entry.bind("<Down>", lambda event=None: user_entry.focus())
    website_entry.bind("<Up>", lambda event=None: password_entry.focus())

    user_label.grid(column=0, row=2, sticky="w")
    user_entry.grid(column=1, row=2, columnspan=2, sticky=EW, padx=5, pady=5)
    user_entry.bind("<Return>", user_entry_on_enter_pressed)
    user_entry.bind("<Down>", lambda event=None: password_entry.focus())
    user_entry.bind("<Up>", lambda event=None: website_entry.focus())
    user_entry.insert(0, popular_username)

    password_label.grid(column=0, row=3, sticky="w")
    password_entry.grid(column=1, row=3, sticky=EW, padx=5, pady=5)
    password_entry.bind("<Down>", lambda event=None: website_entry.focus())
    password_entry.bind("<Up>", lambda event=None: user_entry.focus())
    generate_password.grid(column=2, row=3, padx=5, pady=5, sticky=EW)
    search.grid(column=2, row=1, padx=5, pady=5, sticky=EW)

    add_button.grid(column=1, row=4, columnspan=2, sticky=EW, padx=5, pady=5)
    password_entry.bind("<Return>", password_entry_on_enter_pressed)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.pack_propagate(0)
window.minsize(550, 450)
window.config(pady=25, padx=50)

menu_commands()
website_label = Label(text="Website:", bg="#202020", font=FONT)
user_label = Label(text="Username:", bg="#202020", font=FONT)
password_label = Label(text="Password:", bg="#202020", font=FONT)

website_entry = Entry(highlightthickness=2, font=EFONT)
website_entry.focus()
user_entry = Entry(highlightthickness=2, font=EFONT)
password_entry = Entry(highlightthickness=2, font=EFONT)
generate_password = Button(text="Generate", font=("", 8, "bold"), command=password_generator)
search = Button(text="Search", font=("", 8, "bold"), command=find_password)
add_button = Button(text="Add", font=("", 9, "bold"), command=get_pass)

if dark_theme_status:
    dark_theme()
else:
    light_theme()

configure_widgets()

window.mainloop()
