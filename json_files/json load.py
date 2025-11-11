import json
class JsonLoad:
    @staticmethod
    def load(json_file):
        with open(json_file,"r") as file:
            data=(json.load(file))
            print(data)
