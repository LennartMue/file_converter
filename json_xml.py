class JSONxml():
    
    def __init__(self):
        self.convert_to_json = "converting xml to json"
        self.convert_to_xml = "converting json to xml"

    def XMLtoJSON(self, input1, output1):
        import json
        import xmltodict
        with open(input1) as xml_File:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            with open(output1) as json_file:
                json_file.write(json_data)

        print(self.convert_to_json)

    def JSONtoXML(self, input2, output2):
        import xml
        import jsontodict

        print(self.convert_to_xml)


if __name__ == "__main__":
    json_xml = JSONxml()
    input1 = "C:\\Users\\3872573\\Documents\\Konverter\\XML\\test.xml"
    output1 = "C:\\Users\\3872573\\Documents\\Konverter\\JSON\\testoutput.json"
    input2 = "C:\\Users\\3872573\\Documents\\Konverter\\JSON"
    output2 = "C:\\Users\\3872573\\Documents\\Konverter\\XML"
    XMLtoJSON(input1, output1)
