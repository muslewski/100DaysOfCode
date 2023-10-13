import requests
from datetime import datetime
from time import sleep
import smtplib

MY_LAT = 52.406376  # Your latitude
MY_LONG = 16.925167  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.
def meetup():
    responses = requests.get(url="http://api.open-notify.org/iss-now.json")
    responses.raise_for_status()
    datas = responses.json()

    iss_latitude = float(datas["iss_position"]["latitude"])
    iss_longitude = float(datas["iss_position"]["longitude"])

    # Test
    # iss_latitude = 50
    # iss_longitude = 15

    print(f"iss_latitude = {iss_latitude}")
    print(f"iss_longitude = {iss_longitude}")

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        print("There is nothing to watch!")
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour


# Test
# hour = 2


def dark():
    if hour > sunset or hour < sunrise:
        return True
    else:
        return False


def send_mail():
    my_email = "10iron10man10@gmail.com"
    password = "skqk oeks igpa hejj"
    recipient = "hackypotter@proton.me"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg="Subject:ISS Overhead!\n\nLook up, to see..."
        )


# If the ISS is close to my current position
while meetup():
    if dark():
        print("We're watching!")
        send_mail()
        sleep(60)
    else:
        print("It's too bright outside")
        break
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
