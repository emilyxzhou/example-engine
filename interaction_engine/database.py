import json


class Database:
    def __init__(self):
        self._database = {}

    def get_dictionary_of_nodes(self):
        return self._database

    def save_as_json(self):
        with open("database.json", "w") as outfile:
            json.dump(self._database, outfile)
