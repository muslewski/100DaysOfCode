import smtplib
import os

my_email = os.environ.get("my_email")
password = os.environ.get("password")

class NotificationManager:
    def __init__(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="hackypotter@proton.me",
                msg=f"Subject: Your Future Adventures!\n\n{message}"
            )