class XMLcsv():
    def __init__(self):
        self.convert_to_xml = "converting csv to xml"
        self.convert_to_csv = "converting xml to csv"

    def CSVtoXML(self):
        print(self.convert_to_xml)

    def XMLtoCSV(self):
        print(self.convert_to_csv)


if __name__ == "__main__":
    xml_csv = XMLcsv()
