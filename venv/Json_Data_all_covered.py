import json
import csv
import pandas as pd

# print(dir(json))
json_file1 = open("sample-json-file.json", "r", encoding="utf-8")
my_json_file = json.load(json_file1)
print(len(my_json_file.keys()))
keys = []
values = []
for i in my_json_file.keys():
    keys.append(i)
print(keys)
for i in my_json_file.values():
    values.append(i)
# print(my_json_file)
print(values)
my_dick = {}
for x in range(len(my_json_file.keys())):
    my_dick[str(keys[x])] = str(values[x])
print(my_dick)


def writeIntoJsonFile(dick, fileName):  # you can pass any kind of data in dick as List,tuple,dictionary,string
    with open(fileName + ".json", "w") as wij:
        json.dump(obj=dick, fp=wij, indent=4)


fName = input("Give a name for your file: ")
writeIntoJsonFile(dick=my_dick, fileName=fName)

# json file to csv file
raw_csv = pd.json_normalize(my_dick, max_level=1)
print(raw_csv)
raw_csv.to_csv(fName+".csv")

# for csv to json
dataFrame = pd.read_csv("sample-json-file.csv")
dataFrame.to_json(fName + ".json",index=False,orient="table")
json_file1.close()
