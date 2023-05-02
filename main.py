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

        self.input_path = None
        self.output_path = None

    def user_interface(self):
        print("hello user")
        # set self.output_path and self.input_path

    def run(self):
        # hier Benutzerschnittstelle 
        # also: Fragen, welcher Typ und Pfad die Eingangs- und Ausgangsdatei haben
        # Diese informationen verwerten
        self.user_interface()

        # Dateityp verarbeiten und aufgrund dessen die entsprechende Methode der importierten Converter aufrufen
        self.JSONconverterXML.JSONtoXML(self.input_path, self.output_path)
        self.JSONconverterXML.XMLtoJSON(self.input_path, self.output_path)
        self.XMLconverterCSV.XMLtoCSV(self.input_path, self.output_path)
        self.XMLconverterCSV.CSVtoXML(self.input_path, self.output_path)
        self.CSVconverterJSON.CSVtoJSON(self.input_path, self.output_path)
        self.CSVconverterJSON.JSONtoCSV(self.input_path, self.output_path)


if __name__ == "__main__":
    converter = Converter()
    converter.run()
