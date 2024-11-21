import os
import smtplib
import re
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def send_mail(product_price=0, product_title="", product_url=""):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(SENDER_EMAIL, SENDER_PASSWORD)

    product_title = product_title.encode('ascii', 'ignore').decode('ascii')
    product_title_cleaned = re.sub(r'\s+', ' ', product_title).strip()

    message = f"Subject: Amazon Price Alert!\n\n{product_title_cleaned} is now {product_price} \n{product_url}"
    print(message)
    s.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
    s.quit()
