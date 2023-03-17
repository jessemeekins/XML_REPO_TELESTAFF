#%%
from companies import FIRST_RESPONERS_COMPANIES
from abc import ABC, abstractmethod



class DataSource(ABC):
    """Connect and Retrieve Class"""

    @abstractmethod
    def connect(self): 
        ...

    @abstractmethod
    def retrieve_data(self): 
        ...
        
class XMLFileDataSource(DataSource):
    """Methods to Retrieve XML file types"""

    def connect(self):
        print("[*]"*10)
        
    def retrieve_data(self):
        print('[*] Connecting to Data Source...')
        import xml.etree.ElementTree as ET
        tree = ET.parse('/Users/jessemeekins/Documents/VS Code (original)/XML_REPO_TELESTAFF/Flask_API/XML_EXPORT_DATA/XML EXPORT 3_7_22.xml')
        root = tree.getroot()
        return root
    
class XLSXFileDataSource(DataSource):
    """Methods for retrieving XLSX file types"""

    def connect(self):
        print('[*] Connecting to XLSX data...')

    def retrieve_data(self):
        print('[*] Retreiving data from XLSX file database...')


class DataProccessing(ABC):
    """Outlining the class pattern"""

    def __init__(self, data_source: DataSource):
        """Init the bridge connection"""
        self.data_source = data_source

    @abstractmethod
    def _define_fields(self, record) -> dict: 
        """Internal method"""

    @abstractmethod
    def personnel_records(self, records) -> dict: 
        ...

    @abstractmethod
    def apply_data_strategy(self, records: dict) -> dict: 
        ...

    @abstractmethod
    def create_dictionary(self, records: dict) -> dict: 
        ...
    
    @abstractmethod
    def add_records_to_dictionary(self, records: dict) -> dict: 
        ...
    
    def proccess(self, filetype: str):
        """Work flow to be executed"""
        
        if filetype:
            self.data_source.connect()
            file_source = self.data_source.retrieve_data()
            data = self.personnel_records(file_source)
            records = self.apply_data_strategy(data)
            new_dictionary = self.create_dictionary(records)
            result = self.add_records_to_dictionary(new_dictionary)
            print(result)
            

class ALSCountStrategy(DataProccessing):
    """First class strategy"""

    def _define_fields(self, record) -> dict:
        # Try/Except returns all data required or defaults to None type  
        try:
            # EID of employee 
            eid = record.find('RscEmployeeIDCh').text
            # Name of employee 
            name = record.find('RscMasterNameCh').text
            # Rank of employee 
            rank = record.find('PosJobAbrvCh').text
            try:
                # RscFormulaID maps back to Telestaff Person Formula ID, this will give license level
                position = record.find('RscFormulaIDCh').text
            except:
                # if RscFormulaID isnt available, Pull PosFormulaID -> Nozzle, Hookup ect.
                position = record.find('PosFormulaIDCh').text
            paycode = record.find('WstatAbrvCh').text
            # Unit abreviation 
            comp = record.find('PUnitAbrvCh').text
            # Start date and time 
            start = record.find('StaffingStartDt').text
            # End date and time 
            end = record.find('ShiftEndDt').text
            # Return a dictionary to be later added to the class dictionary self.personnelDict
            data = {'EID':eid, 'NAME':name, 'RANK':rank, 'POSITION':position, 'PAYCODE': paycode, 'COMP':comp, 'START':start, 'END': end}
            return data
        
        except Exception: 
            ...

    def personnel_records(self, records) -> dict:
        personnel_dictionary = {}
        
        for child in records.iter('Record'): 
            data = self._define_fields(child)
            # Checks that eack "data" is not None
            if data != None:
                # Adds record dict to Global personnelDict 
                personnel_dictionary[data['EID']] = {"eid": data['EID'] ,"name": data['NAME'], "rank": data['RANK'], "position": data['POSITION'], "paycode": data['PAYCODE'], "company_abr": data['COMP'], "start": data['START'], "end": data["END"]}
            else: ...
        else:
            return personnel_dictionary
        
    def apply_data_strategy(self, records: dict) -> dict:
        print('[*] ALS Strategy')
        return records
    
    def create_dictionary(self, records: dict) -> dict:
        return records
    
    def add_records_to_dictionary(self, records: dict) -> dict:
        print('[*] Filtered ALS Records')
        print( '[*] Total Records:' , records.__len__())
    
    
class BLSCountStrategy(DataProccessing):
    """BLS data class stretegy"""

    def _define_fields(self, record) -> dict:
        return record
    
    def parse_records(self, records) -> dict:
        print('[*] BLS Parser')
        return records
    
    def apply_data_strategy(self, records: dict) -> dict:
        print('[*] BLS data strategy', records)
        return records
    
    def create_dictionary(self, records: dict) -> dict:
        print('[*] BLS create dict')
        return records
    
    def add_records_to_dictionary(self, records: dict) -> dict:
        print('[*] BLS add to dict')
        return records.__len__()
    
    
class StrategyExportFactory(ABC):
    """Export Factory for different data manipulation methods"""
   
    @abstractmethod
    def get_data_strategy(self) -> DataProccessing: 
        ...
        

class ALSCountStretegyExporter(StrategyExportFactory):
    """ALS Count Factory"""
   
    def get_data_strategy(self) -> DataProccessing:
        return ALSCountStrategy(DataSource)
    
    
class BLSCountStrategyExporter(StrategyExportFactory):
    """BLS Count Strategy"""

    def get_data_strategy(self) -> DataProccessing:
        return BLSCountStrategy(DataSource)

    
def execute_order() -> StrategyExportFactory:

    strategy = {
        'ALS': ALSCountStrategy,
        'BLS': BLSCountStrategy
    }

    while True:
        export_type = input("Enter the report type: ['ALS', 'BLS']")
        if export_type in strategy:
            return strategy[export_type]
        print('Unknown export type...')

def main(facorty: StrategyExportFactory) -> None:

    data_exporter = facorty.get_data_strategy()
    data_exporter.proccess('ALS')


if __name__ == '__main__':
    factory = execute_order()
    main(factory)






# %%
