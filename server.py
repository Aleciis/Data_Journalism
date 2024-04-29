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
    return render_template('macro_page.html', Parks= data.keys(), Parks_Underscored=Parks_Underscored, Parks_and_Parks_Underscored=zip(Parks,Parks_Underscored))

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


    

app.run(debug=True)