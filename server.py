# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def year():
    f= open("Data_Journalism/data/Parks_Data.json", "r")
    data=json.load(f)
    f.close()
    #print(data)
    Parks= data.keys()
    Parks_Underscored= []
    for key in Parks:
        key = key.replace(" ", "_")
        Parks_Underscored.append(key)
    #print(Parks_underscored)
        listzip=[]
    park_boroughs = [0,0,0,0,0] # M, X, B, Q, R
    for name in Parks: 
        for number in data[name]["ZIPCODE"]:
            if data[name]["ZIPCODE"] not in listzip:
                listzip.append(data[name]["ZIPCODE"])

        for letter in data[name]["BOROUGH"]:
          if str(letter) == "M":
            park_boroughs[0]+=1
          if str(letter) == "X":
            park_boroughs[1]+=1
          if str(letter) == "B":
            park_boroughs[2]+=1
          if str(letter) == "Q":
            park_boroughs[3]+=1
          if str(letter) == "R":
            park_boroughs[4]+=1
    print(park_boroughs)
    # creates list of unique zipcodes
    #print(listzip)
    
    
    
    return render_template('macro_page.html', Parks= data.keys(), Parks_Underscored=Parks_Underscored, Parks_and_Parks_Underscored=zip(Parks,Parks_Underscored), SVG_ZIPCODES = "../SVG_ZIPCODES")

@app.route('/about')
def index():
    f= open("Data_Journalism/data/Parks_Data.json", "r")
    data=json.load(f)
    f.close()
    #print(data)
    Parks= data.keys()
    Parks_Underscored= []
    for key in Parks:
        key = key.replace(" ", "_")
        Parks_Underscored.append(key)
    #print(Parks_underscored)
    
    return render_template('about.html',  Parks= data.keys(), Parks_Underscored=Parks_Underscored, Parks_and_Parks_Underscored=zip(Parks,Parks_Underscored))

@app.route('/micro')
def micro():
    f= open("Data_Journalism/data/Parks_Data.json", "r")
    data=json.load(f)
    f.close()
    print(f"request.url={request.url}")
    print(f"request.url={request.query_string}")
    Individual_Park=request.query_string.decode()
    Individual_Park_Spaces=Individual_Park.replace("_", " ")
    Individual_Park_Spaces_decoded=Individual_Park_Spaces.replace("%27", "'")
    print(Individual_Park_Spaces_decoded)
    Parks= data.keys()
    Parks_Underscored= []
    for key in Parks:
        key = key.replace(" ", "_")
        Parks_Underscored.append(key)
    Individual_Park_Spaces_String = str(Individual_Park_Spaces_decoded)
    #print(Individual_Park_Spaces)
    #print(data[Individual_Park_Spaces_String]["BOROUGH"])

    for borough in data[Individual_Park_Spaces_String]["BOROUGH"]:
        if str(borough) == "M":
            borough = "Manhattan"
        if str(borough) == "B":
            borough = "Brooklyn"
        if str(borough) == "X":
            borough = "The Bronx"
        if str(borough) == "Q":
            borough = "Queens"
        if str(borough) == "R":
            borough = "Staten Island"
    print(borough)
    print(data[Individual_Park_Spaces_String])
    #print(Parks_underscored)
    
 
    return render_template('micro_page.html',  Parks= data.keys(), Parks_Underscored=Parks_Underscored, Parks_and_Parks_Underscored=zip(Parks,Parks_Underscored), Individual_Park_Spaces = Individual_Park_Spaces_String, Park_Acres = data[Individual_Park_Spaces_String]["ACRES"],Park_Borough = borough,Park_Location = data[Individual_Park_Spaces_String]["LOCATION"],Park_Type = data[Individual_Park_Spaces_String]["TYPECATEGORY"],Park_URL = data[Individual_Park_Spaces_String]["URL"],Park_Zipcode = data[Individual_Park_Spaces_String]["ZIPCODE"])
@app.route('/zipcodes')
def zipcodes():
    f= open("Data_Journalism/data/Parks_Data.json", "r")
    data=json.load(f)
    f.close()


    print(f"request.url={request.url}")
    print(f"request.url={request.query_string}")
    zipcodes=request.query_string.decode()
    print(zipcodes)

    # do f=open svg_individual_zipcodes/requestquerystring and copy text to pass as a string
    return render_template('zipcodes.html', zipcodes=zipcodes)


app.run(debug=True)