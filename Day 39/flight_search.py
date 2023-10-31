import os
import requests
import datetime

date_now = datetime.datetime.now() + datetime.timedelta(days = 1)

date_to = date_now + datetime.timedelta(days = 179)
date_now = date_now.strftime("%d/%m/%Y")
date_to = date_to.strftime("%d/%m/%Y")

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
tequila_endpoint_get = "https://api.tequila.kiwi.com/locations/query"

header = {
            "apikey": TEQUILA_API_KEY
        }

home = "LON"

class FlightSearch:
    def searcher(self, city):
        self.city = city
        query = {
            "term": city,
            "locations_type": "city"
        }

        response = requests.get(tequila_endpoint_get, params=query, headers=header)
        response.raise_for_status()
        return response.json()

    def search_price(self, iata):
        search_api = "https://api.tequila.kiwi.com/v2/search"

        search_params = {
            "fly_from": home,
            "fly_to": iata,
            "date_from": f"{date_now}",
            "date_to": f"{date_to}",
            "curr": "USD"
        }

        search_response = requests.get(search_api, search_params, headers=header)

        data = search_response.json()["data"][0]
        price = data["price"]
        return f"{self.city}: {price}$"

