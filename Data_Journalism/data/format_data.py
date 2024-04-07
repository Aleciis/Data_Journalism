import json
import csv


f1 = open("Data_Journalism/data/Parks_Data.csv", "r")
lines = f1.readlines()
list=[]
dictionary={}
with open('Data_Journalism/data/Parks_Data.csv') as f:
   for line in csv.DictReader(f, fieldnames=('ACRES','BOROUGH','LOCATION','SIGNNAME','TYPECATEGORY','URL','ZIPCODE','multipolygon')):
    list.append(line['SIGNNAME'])
print(list)

# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("Data_Journalism/data/Parks_Data.json", "w")
json.dump(list, f2, indent = 4)

f2.close()