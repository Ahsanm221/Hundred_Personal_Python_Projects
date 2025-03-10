import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# #print(round(sum(temp_list)/len(temp_list), 2))
# print(data["temp"].max())
#
#
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# temp_monday = int(monday.temp)
# monday_temp_F = temp_monday*(9/5)+32
# print(monday_temp_F)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
cin_color = 0
gray_color = 0
black_color = 0
for color in fur_color:
    if color == "Cinnamon":
        cin_color += 1
    elif color == "Gray":
        gray_color += 1
    elif color == "Black":
        black_color += 1

# cin_color = Fur_color.count() == "Cinnamon"
# gray_color = Fur_color.count() == "Gray"
# black_color = Fur_color.count() == "Black"
print(cin_color,black_color,gray_color)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, cin_color, black_color]
}

df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
print(df)