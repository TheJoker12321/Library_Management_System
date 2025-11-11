import json
class JsonCreater:
    @staticmethod
    def create(json_file,data):
        with open(json_file,"a") as file:
            file.append(json.dumps(data))
