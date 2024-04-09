import json
import csv


f1 = open("Data_Journalism/data/Parks_Data.csv", "r")
lines = f1.readlines()
listed=[]
dictionary={}
#   "B": {
#     "ParkName":{}
#     "ParkName2":{}
#   }
#   "Q":{
#     "ParkName":{}
#     "PakrkName2":{}
#   }

with  open('Data_Journalism/data/Parks_Data.csv', 'r') as read_obj: 
  
    # Return a reader object which will 
    # iterate over lines in the given csvfile 
    csv_reader = csv.reader(read_obj) 
  
    # convert string to list 
    list_of_csv = list(csv_reader) 
  
#print(list_of_csv) 

for tinylist in list_of_csv:
    if tinylist is not ['ACRES', 'BOROUGH', 'LOCATION', 'SIGNNAME', 'TYPECATEGORY', 'URL', 'ZIPCODE']:
        if(tinylist[3]) not in dictionary:
            dictionary[tinylist[3]] = tinylist
           
    
print(dictionary)
        



# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("Data_Journalism/data/Parks_Data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()