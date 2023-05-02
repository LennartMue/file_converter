from enum import Enum

from json_xml import JSONxml
from xml_csv import XMLcsv
from csv_json import CSVjson


class FileType(Enum):
    XML = 0
    CSV = 1
    JSON = 2


class Converter():
    def __init__(self):
        self.JSONconverterXML = JSONxml()
        self.XMLconverterCSV = XMLcsv()
        self.CSVconverterJSON = CSVjson()

    def user_interface(self):
        print("hello user")

    def run(self):
        # hier Benutzerschnittstelle 
        # also: Fragen, welcher Typ und Pfad die Eingangs- und Ausgangsdatei haben
        # Diese informationen verwerten
        self.user_interface()

        # Dateityp verarbeiten und aufgrund dessen die entsprechende Methode der importierten Converter aufrufen
        self.JSONconverterXML.JSONtoXML()
        self.JSONconverterXML.XMLtoJSON()
        self.XMLconverterCSV.XMLtoCSV()
        self.XMLconverterCSV.CSVtoXML()
        self.CSVconverterJSON.CSVtoJSON()
        self.CSVconverterJSON.JSONtoCSV()


if __name__ == "__main__":
    converter = Converter()
    converter.run()
