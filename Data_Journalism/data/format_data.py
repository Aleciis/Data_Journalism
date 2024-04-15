import json
import csv


f1 = open("Data_Journalism/data/Parks_Data.csv", "r")
lines = f1.readlines()
listed=[]
dictionary={}


with  open('Data_Journalism/data/Parks_Data.csv', 'r') as read_obj: 
  
    # Return a reader object which will 
    # iterate over lines in the given csvfile 
    csv_reader = csv.reader(read_obj) 
  
    # convert string to list 
    list_of_csv = list(csv_reader) 
  
#print(list_of_csv) 
edited_csv = list_of_csv[1:]
#print(edited_csv)
#print(list_of_csv[0][0])

for sublist in edited_csv:
        if sublist[3] not in dictionary:
            dictionary[sublist[3]]= {}
        for key in dictionary:
          if list_of_csv[0][0] not in dictionary[key]:
            dictionary[sublist[3]][list_of_csv[0][0]] = sublist[0]
            dictionary[sublist[3]][list_of_csv[0][1]] = sublist[1]
            dictionary[sublist[3]][list_of_csv[0][2]] = sublist[2]
            dictionary[sublist[3]][list_of_csv[0][3]] = sublist[3]
            dictionary[sublist[3]][list_of_csv[0][4]] = sublist[4]
            dictionary[sublist[3]][list_of_csv[0][5]] = sublist[5]
            dictionary[sublist[3]][list_of_csv[0][6]] = sublist[7] #trimmed zipcode is on a different coloumn
            
# some issues: Names "Park" and "Sitting Area" are shared between multiple parks (around 100 parks are just named "Park")
# just say "data not found"
    
#print(dictionary)
        



# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("Data_Journalism/data/Parks_Data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()