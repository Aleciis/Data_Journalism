import json


f1 = open("Parks_Data.csv", "r")
lines = f1.readlines()

dictionary ={}

# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("Parks_Data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()