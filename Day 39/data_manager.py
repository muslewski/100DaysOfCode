import requests
from flight_search import FlightSearch

sheety_endpoint_get = "https://api.sheety.co/959d4aad9762ee6ae341720e1891685b/flightDeals/prices"

response = requests.get(sheety_endpoint_get)
response.raise_for_status()

flight_searcher = FlightSearch()


class DataManager:
    def __init__(self):
        self.data = response.json()["prices"]
        print(self.data)
        self.output = []

    def update(self):
        for item in self.data:
            # id = item["id"]
            # sheety_endpoint_put = f"{sheety_endpoint_get}/{id}"

            data = flight_searcher.searcher(item["city"])
            iata = data["locations"][0]["code"]

            # iata = {
            #     "price": {
            #         "iataCode": iata
            #     }
            # }

            # response_put = requests.put(sheety_endpoint_put, json=iata)
            # response_put.raise_for_status()
            # print(response_put.text)

            self.output.append(flight_searcher.search_price(iata))
