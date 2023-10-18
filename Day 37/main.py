import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Python Graph",
    "unit": "Quality",
    "type": "int",
    "color": "ajisai",
    "timezone": "PL"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

graph_add_endpoint = f"{graph_endpoint}/{graph_id}"

quantity = "10"

yesterday = datetime(year=2023, month=10, day=8)
current_date = datetime.now()
date = yesterday.strftime("%Y%m%d")

graph_add_params = {
    "date": date,
    "quantity": quantity,
}

response = requests.post(url=graph_add_endpoint, json=graph_add_params, headers=headers)
print(response.text)


# put_pixela_endpoint = f"{graph_add_endpoint}/{date}"

# put_params = {
#     "quantity": quantity
# }

# response = requests.put(url=put_pixela_endpoint, json=put_params, headers=headers)

# response = requests.delete(url=put_pixela_endpoint, headers=headers)
# print(response.text)
