# with open ("weather_data.csv", "r") as data:
#     d_list = data.readlines()
#     new_list = []
#     for item in d_list:
#         new_list.append(item.strip())
#     print(new_list)

# import csv

# #csv.reader

# with open ("weather_data.csv", "r") as data:
#     d_list = csv.reader(data)
#     temperature = []
#     print(d_list)
#     for row in d_list:
#         temperature.append(row[1])
#     new_temp = []
#     for item in temperature[1:]:
#         new_temp.append(int(item))
#     print(new_temp)

        
#from http.client import _DataType
from statistics import mean
import pandas as pd

data = pd.read_csv("squirrel.csv")

#print(data["temp"])
# data_dict = data.to_dict()
# #print(data_dict)

# #print((data["temp"]).to_list())
# max = mean(data["temp"])
# #print(f"maximum :{max}")

# print(data.day)


#print(data[data.day == 'Monday'])
#print(data[data.temp == max(data.temp)])
# Monday = data[data.day == "Monday"]
# temp_cel = int(Monday.temp)
# temp_far = (temp_cel * (9/5)) + 32
# print(temp_far)
#print(data["Primary Fur Color"].value_counts())
red_squirrel_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
grey_squirrel_count = len(data[data['Primary Fur Color'] == "Gray"])
black_squirrel_count = len(data[data['Primary Fur Color'] == "Black"])
print(red_squirrel_count)
print(grey_squirrel_count)
print(black_squirrel_count)


dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(dict)
df.to_csv("squirrel_color.csv")
