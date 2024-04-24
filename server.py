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
    #print(Individual_Park_Spaces)
    Parks= data.keys()
    Parks_Underscored= []
    for key in Parks:
        key = key.replace(" ", "_")
        Parks_Underscored.append(key)
    #print(Parks_underscored)
    
    
    return render_template('micro_page.html',  Parks= data.keys(), Parks_Underscored=Parks_Underscored, Parks_and_Parks_Underscored=zip(Parks,Parks_Underscored), Individual_Park_Spaces = Individual_Park_Spaces)


    

app.run(debug=True)