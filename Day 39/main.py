#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

print("Hello World")
manager = DataManager()
manager.update()
output = manager.output
result = ""
for item in output:
    result += item + "\n"

# Remove the last "\n" since it's added after the last item
result = result.rstrip("\n")
print(result)
NotificationManager(message=result)