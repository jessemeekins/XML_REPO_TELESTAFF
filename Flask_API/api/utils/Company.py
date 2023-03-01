#%%
#------------->   COMPANY.PY CLASS MODULE  <---------------
# Company class is ised to create Object froms a list of companies.
# The list of companies can be found in companies.py. It isnt 100%,
# correct but will surfice for the time being. The Company Class allows,
# Record objects to be added to the Company staff list. Additional functions,
# have been outlined to manipulate and change the Objects attributes.
# These attributes will be used in the app.py file to further proccess,
# the companies and personnel to provide a more robust application.
# Some of the below functions will appear abstract, but ill try to put,
# references to pythons documentation for followup. 


# Importing the Record class and all of its functionality
from .Record import *
DEBUG = True
# Import global DEBUG Setting, will be used in config file

# Importing all nessecary packages
# logging will further developed in near future
import logging
from functools import singledispatch

# Defining the company class
class Company():
    # Initializing the company class
    # Only requires 1 argument to set up the Object
    # argument format should be "E69" or "T420"
    def __init__(self, name:str) -> None:
        # argument passed into this value
        self.name = name
        # Default empty staff list, will hold all Record Objects, that represent staffing records
        self.staff = []
        # Of the staffing records, how many have "1.0" in their position, representing paramedic
        self.medic_count =  0 
        # Default to false, will toggle to true once an Object with Paramedic is passed into the list
        # Trouble shoot this method within this class, under __add__() function
        self.is_als = False
        # Not yet functional within this class, mostly designed for comparer operators < > = in app.py
        self.overstaffed = False

    def __dict__(self):
        return {"name": self.name, "staff": self.staff, "medic_count": self.medic_count, "is_als": self.is_als}

    # Function returns a string representation of this Object. Fully Customizable.
    def __str__(self) -> str:
        return f"[{self.name} ALS: {self.is_als}] numParamedics: {self.medic_count}"
    
    # Defines a human readable representation of the Object if no other methods are called upon the Object
    # calling this method will launch a second func within this func to refresh if Objects values when, 
    # Record Objects are added and deleted
    def __repr__(self) -> str:
        # internal class method that auto refreshes and checks staffing list for paramedics and update counts
        self.refresher()
        # The actual formated string representation that is returned
        return f"""

        COMPANY: {self.name}
        STAFF: {self.staff}
        MEDICS: {self.medic_count}
        ALS: {self.is_als}

        """
    # This allows a Company Object to allow + operator to add a Record to the staff list
    # jesse = Record(...)
    # engine69 = Company(...)
    # engine69 + jesse
    # This will add a "jesse" object to the Company Objects list

    def __add__(self, obj:dict) -> None:
        # Try/except clause to disregard companies not outlined in the companies lists, i.e. BC's 
        try:
            # First checks if the passed in argument is an Object
            if isinstance(obj, dict): 
            # then object module is name "Record.Recorsd" and length(staff List is less that 4)
              
                # Appends object to self.staff list
                formatted = {"eid": obj.eid, "name": obj.name, "rank": obj.rank, "position": obj.position, "paramedic": obj.paramedic, "company": obj.company_abr, "time": obj.time}
                self.staff.append(formatted)
                # checks if object has paramedic set to true
                if obj.paramedic:
                    # object i set to true, change is als to true
                    self.is_als = True 
                    # medic added to count 
                    self.medic_count += 1
                    print('** SUCCESS **')
            else:
                # DEBUG message to help in developement
                if DEBUG:
                    print('__ADD__ error')
            
                    pass
        except:
            pass

 
    # This function allows two object to use the "-" operator to remove Record Object from Company list
    def __sub__(self, obj:object) -> None:
        # checks to make sure argument is a ObjectType
        if isinstance(obj, object):
            # Removes record from Company List
            self.staff.remove(obj)
            # checks is the removed object is a paramedic (True/False)
            if obj.paramedic:
                # removed from count
                self.medic_count -= 1
            # After removing medic from count, checks if medic count is 0;
            # if the number equal to 0, changes the Company is_als to False
            if self.medic_count == 0:
                self.is_als = False
        # if debug is true, print to console
        if DEBUG:
            # Prints the deleted Object
            print(obj)
            # Prints the resulting list of the Compant
            print(self.staff)

    # This functions provides "==" operatores amongs Objects. 
    # This function accepts a True/False arugment
    def __eq__(self, obj:bool) -> bool:
        # Checks if argument is an ObjectType == Boolean value
        if isinstance(obj, bool):
            # Checks if the company and the passed in bollean are equal to each other
            # SPECIAL_NOTE: False == False will return True
            if self.is_als == obj:
                return True
            else:
                return False
        # If this operation fails
        else:
            # DEBUG == True
            if DEBUG:
                # Prints to console
                print(f"{Company(__name__)} failed to execute '==' comp..." )
            # DEBUG == False
            else:
                # Enters error message into log for further debuggin
                logging.DEBUG(f"{Company(__name__)} failed to execute '==' comp..." )
    
    # Method provides ">" comparatuive funxtionality bwetween objects.
    # Method will be primarily used in the main app.py for business logic rules ect.
    def __gt__(self, obj: int):
        # Checks if obj is a integer

        # Future Error Handling will be good, try/except clasuses with detailed messages,
        # will be critical in on going development
        if isinstance(obj, int):
            # Defines what data to compare to object, must be integer to integer comparison
            if self.medic_count > obj:
                # if medic count greater than integer passed in as argument
                return True
            else:
                return False
        else:
            # DEBUG == True
            if DEBUG:
                # Prints to console
                print(f"{Company(__name__)} failed to execute '>' comp..." )
            # DEBUG == False
            else:
                # Enters error message into log for further debuggin
                logging.DEBUG(f"{Company(__name__)} failed to execute '>' comp..." )


                


    ######################################
    ###   Class "Getter" Methods for   ###
    ###   each variable in the class   ###
    ######################################
    
    def get_name(self) -> str:
        if DEBUG:
            print(self.name)
        return self.name
    
    def get_staff(self) -> list:
        if DEBUG:
            print(self.staff)
        return self.staff
        
    def get_medic_count(self) -> int:
        if DEBUG:
            print(self.medic_count)
        return self.medic_count

    def get_als(self) -> bool:
        if DEBUG:
            print(self.is_als)
        return self.is_als
    
    def get_overstaffed(self) -> bool:
        if DEBUG:
            print(self.overstaffed)
        return self.overstaffed

    def refresher(self):
        if not self.is_als:
            for s in self.staff:
                if s.paramedic:
                    self.is_als = True
                    self.medic_count += 1
    
    


