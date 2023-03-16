#%%
from typing import Protocol
from companies import FIRST_RESPONERS_COMPANIES
from abc import ABC, abstractmethod
from time import sleep

class DataSource(ABC):
    @abstractmethod
    def connect(self):
        print('[*] Connecting to Data Source...')

    @abstractmethod
    def retrieve_data(self):
        pass

class XMLFileDataSource(DataSource):
    def connect(self):
        print("[*]"*10)
        
    def retrieve_data(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse('/Users/jessemeekins/Documents/VS Code (original)/XML_REPO_TELESTAFF/Flask_API/XML_EXPORT_DATA/XML EXPORT 3_7_22.xml')
        root = tree.getroot()
        return root
    
class XLSXFileDataSource(DataSource):
    def connect(self):
        print('[*] Connecting to XLSX data...')

    def retrieve_data(self):
        print('[*] Retreiving data from XLSX file database...')

class DataProccessing(ABC):
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    @abstractmethod
    def parse_records(self, records) -> dict:
        pass

    @abstractmethod
    def apply_data_strategy(self, records: dict) -> dict:
        pass
    
    @abstractmethod
    def create_dictionary(self, records: dict) -> dict:
        pass

    @abstractmethod
    def add_records_to_dictionary(self, records: dict) -> dict:
        pass

    def proccess(self, filetype: str):

        if filetype:

            self.data_source.connect()
            file_source = self.data_source.retrieve_data()
            data = self.parse_records(file_source)
            self.apply_data_strategy(data)
            self.create_dictionary(data)
            self.add_records_to_dictionary(data)
            for i in file_source:
                print (i)
            print(file_source)




class ALSCountStrategy(DataProccessing):
    def parse_records(self, records) -> dict:
        print('[*] ALS Parse')
        return super().parse_records(records)

    def apply_data_strategy(self, records: dict) -> dict:
        print('[*] ALS Strategy')
        return super().apply_data_strategy(records)

    def create_dictionary(self, records: dict) -> dict:
        print('[*] ALS DICT Created')
        return super().create_dictionary(records)
    
    def add_records_to_dictionary(self, records: dict) -> dict:
        print('[*] ALS Records added')
        return super().add_records_to_dictionary(records)
    

ALS = ALSCountStrategy(XMLFileDataSource())
ALS.proccess('test')





