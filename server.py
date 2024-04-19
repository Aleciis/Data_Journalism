# flask --app data_server run
from flask import Flask
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def year():
    f= open("Data_Journalism/data/Parks_Data.json", "r")
    data=json.load(f)
    f.close()
    print(data)
    return render_template('macro_page.html', Parks= data.keys())

@app.route('/about')
def index():
    f= open("Data_Journalism/data/Parks_Data.json", "r")
    data=json.load(f)
    f.close()
    print(data)
    return render_template('about.html',  Parks= data.keys())


    

app.run(debug=True)