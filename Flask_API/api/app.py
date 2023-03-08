from utils.data import *
from errors import errors
from flask import Flask, render_template


app = Flask(__name__)

app.register_blueprint(errors)


# GLOBAL DICT THAT HOLDS COMPANIES AND PEROSNNEL RECORDS
companyDict = {}
personnelDict = {}

XML = FileProccessing(companyDict, personnelDict)

from utils.companies import FIRST_RESPONERS_COMPANIES

XML.add_companies_to_dict(FIRST_RESPONERS_COMPANIES)
XML.add_records_to_Dict()
XML.add_record_objects_to_companies()

@app.route('/')
def default():
    ALS_COUNT = len(list(filter(lambda x: x["ALS"] == True, companyDict.values())))
    BLS_COUNT = len(list(filter(lambda x: x["ALS"] == False, companyDict.values())))
    num_medics = len(list(filter(lambda x: x["position"] == '1.1', personnelDict.values())))
    num_people = len(list(personnelDict))
    return render_template(
        'index.html', 
        companies=companyDict, 
        personnel=personnelDict, 
        ALS_COUNT=ALS_COUNT, 
        BLS_COUNT=BLS_COUNT,
        num_people = num_people,
        num_medics = num_medics
    )

@app.route("/companies")
def index():  
    return companyDict

@app.route("/companies/als")
def als_apparatus_list():
    return {_: v for _, v in companyDict.items() if v["ALS"] == True}
    

@app.route("/companies/")
@app.route("/companies/<company>")
def single_company(company):
    company = company.upper()
    obj = companyDict.get(company)
    return obj
        
@app.route('/als_count', methods=['GET'])
@app.route('/employees/als_count', methods=['GET'])
@app.route("/companies/als_count", methods=["GET"])
def custom():
    num = len(list(filter(lambda x: x["ALS"] == True, companyDict.values())))
    return {"ALS_COUNT": num} 

@app.route('/bls_count', methods=['GET'])
@app.route('/employees/bls_count', methods=['GET'])
@app.route("/companies/bls_count", methods=['GET'])
def bls_apparatus_list():
    num = len(list(filter(lambda x: x["ALS"] == False, companyDict.values())))
    return {"BLS_COUNT": num} 

@app.route("/employees")
def employees():
    return personnelDict

@app.route("/employees/<eid>")
def single_employee(eid):
    obj = personnelDict.get(eid)
    return obj  

@app.route("/employees/<eid>/<key>")
def single_employee_detail(eid, key):
    obj = personnelDict.get(eid)
    detail = obj[f'{key}']  
    return {key:detail}


if __name__ == '__main__':
    app.run(debug=True)
