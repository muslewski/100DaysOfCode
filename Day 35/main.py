import requests
from twilio.rest import Client
import os

api_key = os.environ.get("API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": os.environ.get("LAT"),
    "lon": os.environ.get("LON"),
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

first_twelve_hours = weather_data["hourly"][:13]

wid_list = [hour["weather"][0]["id"] for hour in first_twelve_hours]

print(wid_list)
if any(element < 700 for element in wid_list):
    print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="be careful, it's going to rain today! ☔",
        from_=os.environ.get("FROM_NUMBER"),
        to=os.environ.get("MY_NUMBER")
    )
    print(message.status)
