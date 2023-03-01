from flask import Flask
from utils.data import *
from functools import reduce


app = Flask(__name__)

companyDict = {}
personnelDict = {}

XML = FileProccessing(companyDict, personnelDict)

XML.add_companies_to_dict()
XML.add_records_to_Dict()
XML.add_record_objects_to_companies()


@app.route("/companies")
def index():  
    return companyDict

@app.route("/companies/als")
def als_apparatus_list():
    return {_: v for _, v in companyDict.items() if v["ALS"] == True}
    

@app.route("/companies/<company>")
def single_company(company):
    company = company.upper()
    obj = companyDict.get(company)
    return obj
        

@app.route("/companies/als_count", methods=["GET", "POST"])
def custom():
    num = len(list(filter(lambda x: x["ALS"] == True, companyDict.values())))
    return {"ALS_COUNT": num} 


@app.route("/companies/bls_count")
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