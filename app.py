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


from Record import *
from Company import *
from companies import *

# Datetime variable to attached time stamps to logging and reaprts
from datetime import datetime as dt
NOW = dt.utcnow()
# Python logging module, basic config to file
# Full implemintation forthcoming
import logging
FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='test_logger.log',level=logging.DEBUG, format=FORMAT)

logging.info(f'PROGRAM START: {NOW}')

# Python xml module config and file location to be uploaded and parsed 
# ET.parse as ET, tree and root are used by convention
import xml.etree.ElementTree as ET
tree = ET.parse('/Users/jessemeekins/Documents/VS Code (original)/XML_REPO_TELESTAFF/ROS11 MFD2023-02-23.xml')
root = tree.getroot()

# Stores all MFD Company Objects for further usage
companyDict = {}
# Stores all MFD XML roster records used for later analysis and use 
personnelDict = {}


# This class is used to create all the Company.Coompany object from Company.py,
# adds them to the global variable companyDict -> dictionary. Company.Company Objects,
# are stored in key/values pairs. The company's abbreviated name as a string is the key,
#  example ('E69', 'T420'). The value is the actual Company.Company Object. I'm using the,
# .get() method to search for the matching value and returning the corisponding object.
# The Object that is returned bty the query can be 

DEBUG = True

class FileProccessing:
    # Initialization takes in no auguements
    def __init__(self) -> None:
        pass
    
    #############################################################################
    ####    Class Function used by create_all_record_objects() to,           ####
    ####    to locate and extract text data from specific XML tags           ####
    #############################################################################

    def parse_record(self, record) -> dict:
        # Try/Except returns all data required or defaults to None type  
        try:
            # EID of employee in XML Record
            eid = record.find('RscEmployeeIDCh').text
            # Name of employee in XML Record
            name = record.find('RscMasterNameCh').text
            # Rank ef employee inXML Record
            rank = record.find('PosJobAbrvCh').text
            # Position of employee in XML Record 1.0 denotes paramedic
            position = record.find('PosFormulaIDCh').text
            # Unit abreviation located in XML Record
            comp = record.find('PUnitAbrvCh').text
            # Start date and time of Record inside XML record
            start = record.find('StaffingStartDt').text
        
            # Return a dictionary to be later added to the class dictionary self.personnelDict
            return {'EID':eid, 'NAME':name, 'RANK':rank, 'POSITION':position, 'COMP':comp, 'START':start}
        
        # If any values are not found or errors in parsing required data, 
        # program will continue collecting data without crashing.
        # Excpetion will be caught as variabble "e" as logged in log file
        except Exception as e:
            # Logging error to log file 
            logging.error(e)
            # Returning Nonetype, record will not be added to class dict
            return None
                
    ###############################################################################
    ####    Function for looping through all Apparatus List in comapnies.py,   ####
    ####  creating objects utilizing the Company class located in company.py   ####
    ###############################################################################

    def create_apparatus_objects(self) -> None:
        # For Loop through companies listed in "from companies import *" -> companies.py 
        for object in ALL_MFD_COMPANIES:
            # Creates Company object from company.py Company class
            company = Company(object)
            # Adds Company Object to Global Company Dictionary variable for later use
            companyDict[company.name] = company

    ###############################################################################
    ####    Function for looping through all Records in a XML export and       ####
    #### creating objects utilizing the Records class located in records.py    ####
    ###############################################################################

    def create_all_record_objects(self) -> None:
        # For loop through children elements with tag <Record> in XML file import
        # root is defined above as apart XML package and tree manager refer to Python 3.11 Docs
        for child in root.iter('Record'):
            # Function from current class, defined 
            # above to return values with specific XML tags
            # Stores each Record instance as data 
            data = self.parse_record(child)
            # Checks that eack "data" is not None
            if data != None:
                # Creates new Record object that containes roster record data
                newRecord = Record(data['EID'] ,data['NAME'], data['RANK'], data['POSITION'], data['COMP'], data['START'])
                # Adds record dict to Global personnelDict 
                personnelDict[data['EID']] = newRecord
                Obj = companyDict.get(newRecord.company_abr, None)
                try:
                    if DEBUG:
                        pass
                except AttributeError as e:
                    if DEBUG:
                        pass
                        #print(f'[{e}] Could not find company: {newRecord.company_abr}')
                    else:
                        pass
                        #logging.error(f'[{e}] Could not find company: {newRecord.company_abr}')
    
    # Function to add Record.Record Objects to Company.Companty Object using "+" operation.
    # Takes Dict and will loop though each Key/Value Pair. The value is the Record.Record 
    # Object and will be added to the correct Company.Company Object. In doing so will 
    # automatically update the Company.Company attributes assigned upon initialization. 
    
    def add_record_objects_to_companies(self):

        for k,v in personnelDict.items():
            company = v.company_abr
            company_obj = companyDict.get(company, None)
            try:
                company_obj + v
            except TypeError as e:
                pass




run = FileProccessing()
run.create_apparatus_objects()
run.create_all_record_objects()
run.add_record_objects_to_companies()




count = 0
for k,v in companyDict.items():
    if v.is_als:
        count += 1
        print(v)


print(f'[{NOW}] ALS COUNT: {count}')

#%%
medic_count = 0
for k,v in personnelDict.items():
    if v.paramedic:
        medic_count +=1
        print(v)

print(medic_count)