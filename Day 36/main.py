import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(title):
    my_email = ""
    password = ""
    recipient = ""

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = recipient
        msg['Subject'] = f'{title}'
        msg.attach(MIMEText(combined_string[:-4], 'html'))

        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=msg.as_string()
        )

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API_KEY = ""

NEWS_API = ""
AV_ENDPOINT = "https://www.alphavantage.co/query?"



SYMBOL = "TSLA"



AV_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": SYMBOL,
    "apikey": AV_API_KEY
}

av_response = requests.get(AV_ENDPOINT, AV_API_PARAMS)
time_series = av_response.json()["Time Series (Daily)"]
first_two_entries = {key: time_series[key] for key in list(time_series)[:2]}

date = list(first_two_entries.keys())[0]

winner = ""

difference_list = []

for day in first_two_entries:
    v1 = float(first_two_entries[day]["1. open"])
    v2 = float(first_two_entries[day]["4. close"])
    difference = (abs(v1 - v2)/((v1 + v2)/2)) * 100
    print(f"difference = {round(difference, 2)}")
    difference_list.append(difference)
    if v1 > v2:
        winner = f"{SYMBOL}: 🔺 {round(difference, 2)}%"
    elif v1 < v2:
        winner = f"{SYMBOL}: 🔻 {round(difference, 2)}%"
    else:
        print("there was no change")

print(date)
news_dictionary = {}

if any(value > 1 for value in difference_list):
    NEWS_PARAMS = {
        "q": "tesla",
        "from": date,
        "to": date,
        "sortBy": "popularity",
        "apikey": NEWS_API
    }
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"
    news_response = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    first_three_news = news_response.json()["articles"][:3]
    for news in first_three_news:
        news_dictionary[news["title"]] = news["description"]

    combined_string = ''
    for key, value in news_dictionary.items():
        combined_string += f'<b style="text-shadow: 2px 2px 4px rgba(0, 0, 255, 0.5);">{key}</b>:<br> {value}<br><hr>'

    send_mail(winner)
