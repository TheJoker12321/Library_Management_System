import pandas
class CsvFromJson:
    @staticmethod
    def create_csv(json_file, csv_file):
        data = pandas.read_json(json_file)
        data.to_csv(csv_file, index=False)