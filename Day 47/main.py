from bs4 import BeautifulSoup
import requests
from send_mail import send_mail

URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find(id="productTitle").get_text()
price = soup.find(class_="a-offscreen").get_text()
priceNum = float(price.split("$")[1])

if priceNum < 100:
    send_mail(price, title, LIVE_URL)

