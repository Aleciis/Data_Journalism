# flask --app data_server run
from flask import Flask
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/about')
def index():
    return render_template('about.html')

@app.route('/')
def year():
    return render_template('macro_page.html')
    

app.run(debug=True)