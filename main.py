# import csv
# data = []
# # with open('weather_data.csv') as f:
# #     # for data_line in f:
# #     #     data.append(data_line)
# #     data = f.readlines()
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     teamprature = []
#     # data2 = data[1:]
#     i=0
#     for row in data:
#         if i==0 :
#             i += 1
#             continue
#         i += 1
#         # print(row)
#         teamprature.append(int(row[1]))
# print(teamprature)
# # print(data)
# import pandas
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
# print(f"max is{data['temp'].max()}")
import pandas
data = pandas.read_csv("squirrel_data.csv")
d3 = data.Age
print("bye")
print(d3)
d2 = data[data["Primary Fur Color"] == "Black"].Age
print(type(d2))
print(d2)
print('asdkna')
print(data)
# print(data["Primary Fur Color"])
index = pandas.Index(data["Primary Fur Color"])
# print(index.to_list())
p = data["Primary Fur Color"].value_counts()
print(type(p))
print(p.index.values.tolist())
print('hello')
p_index = pandas.Index(p)
print(p_index)
p_dict = p.to_dict()
print(p_dict)
p_list = p.to_list()
print(p_list)
# num_grey = p[p.]
# num_grey = p_dict["Gray"]
# num_red = p_dict["Cinnamon"]
# num_black = p_dict["Black"]
data_dict = {
    "fur color": p.index.values.tolist(),
      "count":  p_list
}
print(data_dict)
p_data = pandas.DataFrame(data_dict)
p_data.to_csv("squirrel3.csv")
