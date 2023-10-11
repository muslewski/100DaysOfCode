##################### Extra Hard Starting Project ######################
import smtplib
import datetime
import random
import pandas
import os

my_email = "10iron10man10@gmail.com"
password = "skqk oeks igpa hejj"

now = datetime.datetime.now()
current_day = now.day
current_month = now.month

folder_path = "letter_templates"
files = os.listdir(folder_path)


birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        random_file = random.choice(files)
        selected_file_path = os.path.join(folder_path, random_file)
        with open(selected_file_path) as letter:
            message = letter.read()
            message = message.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy birthday!\n\n{message}"
            )
        print(f"Sent to {row['name']}.")
