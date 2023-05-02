class CSVjson():
    def __init__(self):
        self.convert_to_json = "converting csv to json"
        self.convert_to_csv = "converting json to csv"

    def CSVtoJSON(self):
        print(self.convert_to_json)

    def JSONtoCSV(self):
        print(self.convert_to_csv)


if __name__ == "__main__":
    csv_json = CSVjson()
