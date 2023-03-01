#%%

##########################################################################
##########################################################################                                                     
### Class used to parse XML file from imports, proccess "records"      ###
### from XML file. Each Record will be turned into class object        ###
### and stored in a local class Dict. Record Objects will be added     ###
### to Company class object created from a list of companies in MFD    ###
### After dictionaries are made, Record Objects will be added to       ###
### Company Object and stored, within their own "self.staff" dict      ###
### for further proccessing.                                           ###
##########################################################################
##########################################################################

from functools import reduce

from .Record import *
from .Company import *
from .companies import *

# Datetime variable to attached time stamps to logging and reaprts
from datetime import datetime as dt
NOW = dt.utcnow()
# Python logging module, basic config to file
# Full implemintation forthcoming
import logging

logging.basicConfig(filename='test_logger.log', level=logging.CRITICAL)


# Python xml module config and file location to be uploaded and parsed 
# ET.parse as ET, tree and root are used by convention
import xml.etree.ElementTree as ET
tree = ET.parse('/Users/jessemeekins/Documents/VS Code (original)/XML_REPO_TELESTAFF/Flask_API/XML_FLASK_API_BUILD/api/utils/ROS11 MFD2023-02-23.xml')
root = tree.getroot()


# This class is used to create all the Company.Company object from company.py,
# adds them to the global variable companyDict -> dictionary. Company.Company Objects,
# are stored in key/values pairs. The company's abbreviated name as a string is the key,
#  example ('E69', 'T420'). The value is the actual Company.Company Object. I'm using the,
# .get() method to search for the matching value and returning the corisponding object.
# The Object that is returned by the query can be 

DEBUG = True

class FileProccessing:
    # Initialization takes in no auguements
    def __init__(self, company_dictionary, personnel_dictionary) -> None:
        self.company_dictionary = company_dictionary
        self.personnel_dictionary = personnel_dictionary
    
    #############################################################################
    ####    Class Function used by create_all_record_objects() to,           ####
    ####    to locate and extract text data from specific XML tags           ####
    #############################################################################

    def parse_record(self, record) -> dict:
        # Try/Except returns all data required or defaults to None type  
        try:
            # EID of employee 
            eid = record.find('RscEmployeeIDCh').text
            # Name of employee 
            name = record.find('RscMasterNameCh').text
            # Rank of employee 
            rank = record.find('PosJobAbrvCh').text

            # Position of employee in XML Record 1.0 denotes paramedic
            # Value can be changed in Person Formula ID Field in Person Profile Settings under skill. 
            # EMT-P -> 1.1, EMT-A -> 1.2, EMT-B -> 1.3 
            # Current Testing is using 1.0

            try:
                # RscFormulaID maps back to Telestaff Person Formula ID, this will give license level
                position = record.find('RscFormulaIDCh').text
            except:
                # if RscFormulaID isnt available, Pull PosFormulaID -> Nozzle, Hookup ect.
                position = record.find('PosFormulaIDCh').text
            # Unit abreviation 
            comp = record.find('PUnitAbrvCh').text
            # Start date and time 
            start = record.find('StaffingStartDt').text
            # End date and time 
            end = record.find('ShiftEndDt').text
            # Return a dictionary to be later added to the class dictionary self.personnelDict
            data = {'EID':eid, 'NAME':name, 'RANK':rank, 'POSITION':position, 'COMP':comp, 'START':start, 'END': end}

            return data
        
        # If any values are not found or errors in parsing required data, 
        # program will continue collecting data without crashing.
        # Excpetion will be caught as variabble "e" as logged in log file
        except Exception as e:
            # Logging error to log file
            #print(e)
            # Returning Nonetype, record will not be added to class dict
            return None
                
    ###############################################################################
    ####    Function for looping through all Apparatus List in comapnies.py,   ####
    ####  creating objects utilizing the Company class located in company.py   ####
    ###############################################################################
    
    def add_companies_to_dict(self) -> None:
        for company in ALL_MFD_COMPANIES: 
            # Adds Company Object to Global Company Dictionary variable for later use
            self.company_dictionary[company] = {"ALS": False, "medic_count": 0, "staff": []}

    def create_apparatus_objects(self, data: dict) -> object:
        # For Loop through companies listed in "from companies import *" -> companies.py
            # Creates Company object from company.py Company class

            try:
                if isinstance(data, dict):
                    company = Company(data)
                    return company
            except:
                print('ERROR: Apparatus Obj')
                pass

    ###############################################################################
    ####    Function for looping through all Records in a XML export and       ####
    #### creating objects utilizing the Records class located in records.py    ####
    ###############################################################################
    
    def add_records_to_Dict(self):
        # For loop through children elements with tag <Record> in XML file import
        # root is defined above as apart XML package and tree manager refer to Python 3.11 Docs
        for child in root.iter('Record'):
            data = self.parse_record(child)
            # Checks that eack "data" is not None

            if data != None:
                # Adds record dict to Global personnelDict 
                self.personnel_dictionary[data['EID']] = {"eid": data['EID'] ,"name": data['NAME'], "rank": data['RANK'], "position": data['POSITION'], "company_abr": data['COMP'], "start": data['START'], "end": data["END"]}
                try:
                    if DEBUG:
                        pass
                except AttributeError as e:
                    if DEBUG:
                        pass
                        print(f'[{e}] Could not find company')
                    else:
                        pass
                        logging.error(f'[{e}] Could not find company')
            else:
                print('Record not added to dict')
                print(type(data))


    def create_employee_object(self, data: dict) -> object:
            # Checks if argument is of Dict Type
            if isinstance(data, dict):
                # Creates new Record object that containes roster record data
                try:
                    newRecord = Record(data['EID'] ,data['NAME'], data['RANK'], data['POSITION'], data['COMP'], data['START'], data['END'])
                except:
                    if DEBUG:
                        pass
                        print('ERROR: Personnel Record Object not created')
                    else:
                        pass
                        #logging.error(f'[{e}] Could not find company: {newRecord.company_abr}')
            else:
                print('ERROR: Dict Object required.')
                
    
    # Function to add Record.Record Objects to Company.Companty Object using "+" operation.
    # Takes Dict and will loop though each Key/Value Pair. The value is the Record.Record 
    # Object and will be added to the correct Company.Company Object. In doing so will 
    # automatically update the Company.Company attributes assigned upon initialization. 
    
    def add_record_objects_to_companies(self) -> None:
        # Loops through person object dictionary
        for _, value in self.personnel_dictionary.items():
            # Isolates the personnel record's company name asscoiated with records position
            company_name = value['company_abr']
            # Gets the company object out of company dict using the personnelDict company_abr
            comp_obj = self.company_dictionary.get(company_name, None)
            # Try/Except
            try:
                # Adds personnel Dict to companyDict's List object
                comp_obj['staff'].append(value)
                # checking for 1.0 -> EMT-P
                if value['position'] == "1.0":
                    # Updates ALS status
                    comp_obj['ALS'] = True
                    # Increases medic count by 1
                    comp_obj['medic_count'] += 1
            # Saves an error in variable "e"
            except TypeError as e:
                logging.debug(f"[ERROR] {company_name} not found. 'add_record_objects_to_companies'.")


















# %%
