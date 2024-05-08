# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json
import collections
import math

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
    Individual_Park_Spaces_decoded0=Individual_Park_Spaces.replace("%27", "'")
    Individual_Park_Spaces_decoded=Individual_Park_Spaces_decoded0.replace("%22", chr(34))

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
    #print(data)
    Parks= data.keys()
    Parks_Underscored= []
    for key in Parks:
        key = key.replace(" ", "_")
        Parks_Underscored.append(key)
    Individual_Park=request.query_string.decode()
    Individual_Park_Spaces=Individual_Park.replace("_", " ")
    Individual_Park_Spaces_decoded0=Individual_Park_Spaces.replace("%27", "'")
    Individual_Park_Spaces_decoded=Individual_Park_Spaces_decoded0.replace("%22", chr(34))
    Individual_Park_Spaces_String = str(Individual_Park_Spaces_decoded)

    zipcode_list= ['10001', '10002', '10003', '10004', '10005', '10007', '10009', '10010', '10011', '10012', '10013', '10014', '10016', '10017', '10018', '10019', '10021', '10022', '10023', '10024', '10025', '10026', '10027', '10028', '10029', '10030', '10031', '10032', '10033', '10034', '10035', '10036', '10037', '10038', '10039', '10040', '10065', '10128', '10280', '10301', '10302', '10303', '10304', '10305', '10306', '10307', '10308', '10309', '10310', '10312', '10314', '10451', '10452', '10453', '10454', '10455', '10456', '10457', '10458', '10459', '10460', '10461', '10462', '10463', '10464', '10465', '10466', '10467', '10468', '10469', '10470', '10471', '10472', '10473', '10474', '10475', '11004', '11101', '11102', '11103', '11104', '11105', '11106', '11201', '11203', '11204', '11205', '11206', '11207', '11208', '11209', '11210', '11211', '11212', '11213', '11214', '11215', '11216', '11217', '11218', '11219', '11220', '11221', '11222', '11223', '11224', '11225', '11226', '11228', '11229', '11230', '11231', '11232', '11233', '11234', '11235', '11236', '11237', '11238', '11239', '11354', '11355', '11356', '11357', '11358', '11359', '11360', '11361', '11362', '11363', '11364', '11365', '11366', '11367', '11368', '11369', '11370', '11372', '11373', '11374', '11375', '11377', '11378', '11379', '11385', '11411', '11412', '11413', '11414', '11415', '11416', '11417', '11418', '11419', '11420', '11421', '11422', '11423', '11426', '11427', '11428', '11429', '11432', '11433', '11434', '11435', '11436', '11691', '11692', '11693', '11694'];
    print(len(zipcode_list))
    print(f"request.url={request.url}")
    print(f"request.url={request.query_string}")
    zipcodes=request.query_string.decode()
    print(zipcodes)
    
    z = open(f"Data_Journalism/templates/INDIVIDUAL_ZIPCODES/{zipcodes}.svg", "r")
  
    zipcode_svg = z.read()
    print(zipcode_svg)
    print(str(zipcode_svg))
    park_list = []
    
    for name in Parks:
          #print(data[name]["ZIPCODE"])
          if str(data[name]["ZIPCODE"]) == str(zipcodes):
             park_list.append(name)
    
    park_list_underscored=[]
    for park in park_list:
        park=park.replace(" ", "_")
        park_list_underscored.append(park)
        # print(park_list)
        # print(park_list_underscored)
    
    # for name, zipcode in zip(Parks, range(len(zipcode_list))):
    #             print(zipcode_list[zipcode], name)
    #             if str(data[name]["ZIPCODE"]) == str(zipcode_list[zipcode]):
    #                 park_zip_count[zipcode]+=1
    # print(park_zip_count)
    list_of_total_park_zips=[]
    for name in Parks:
        list_of_total_park_zips.append(data[name]["ZIPCODE"])
    #print(sorted(list_of_total_park_zips))

    # for zips in list_of_total_park_zips:
    #     park_zip_count.append(list_of_total_park_zips.count(zips))

    park_zip_count=collections.Counter(list_of_total_park_zips)
    print(park_zip_count[str(zipcodes)]) #number of parks in specific zip code

    park_zip_count_list=[]
    for zipcode in park_zip_count:
        park_zip_count_list.append(park_zip_count[zipcode])
    avg_park_amount=round((sum(park_zip_count_list)/len(park_zip_count_list)), 2)
    print(avg_park_amount)








          

    # do f=open svg_individual_zipcodes/requestquerystring and copy text to pass as a string
    return render_template('zipcodes.html', Parks=data.keys(),zipcodes=zipcodes, park_list_underscored=park_list_underscored, Parks_and_Parks_Underscored=zip(Parks,Parks_Underscored),zipcode_svg=str(zipcode_svg), park_list=park_list,Individual_Park_Spaces = Individual_Park_Spaces_String, park_list_and_park_underscored=zip(sorted(park_list),park_list_underscored), individual_park_count=park_zip_count[str(zipcodes)], avg_park_amount=avg_park_amount)


app.run(debug=True)