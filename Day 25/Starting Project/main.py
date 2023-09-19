# with open("weather_data.csv") as data:
#     list_of_data = data.readlines()
#     print(list_of_data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperature = []
#     for row in data:
#         temperature.append(int(row[1]))
#
# print(temperature)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_colors = data["Primary Fur Color"]
data_colors_numbers = data_colors.value_counts()
grey = data_colors_numbers.Gray
cinnamon = data_colors_numbers.Cinnamon
black = data_colors_numbers.Black

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey, cinnamon, black]
}

data_csv = pandas.DataFrame(data_dict)
data_csv.to_csv("squirrel_count.csv")
