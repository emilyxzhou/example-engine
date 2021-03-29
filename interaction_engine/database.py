import json
import logging
import os

class Database:

    def __init__(self, input_file_name):
        if type(input_file_name) is not str:
            raise TypeError("file name must be string.")
        if not input_file_name.endswith(".json"):
            raise TypeError("Must be a .json file.")
        self._database_file = input_file_name
        if not os.path.exists(input_file_name):
            directory = os.path.dirname(self._database_file)
            if directory != "":
                os.makedirs(directory, exist_ok=True)
            with open(self._database_file, "w"):
                self.save_as_json()
            self._database = self.read_database()

    def __getitem__(self, item):
        self._database = self.read_database()
        return self._database[item]

    def __setitem__(self, key, value):
        self._database = self.read_database()
        if type(key) is not str:
            raise TypeError("Key must be a string.")
        if value is None:
            value = ""
        elif type(value) in [list, str, int, float]:
            if type(value) is list:
                self.if_items_in_list_are_valid(self, value, [list, str, int, float])
        else:
            print("invalid type")
            return
        self._database[key] = value
        self.save_as_json()

    def if_items_in_list_are_valid(self, value, value_types):
        for i in value:
            if type(i) not in value_types:
                print("invalid type")
                return

    def __contains__(self, item):
        self._database = self.read_database()
        return item in self._database

    def save_as_json(self):
        with open("database.json", "w") as outfile:
            json.dump(self._database, outfile)

    def read_database(self):
        with open(self._database_file) as f:
            try:
                database = json.load(f)
            except json.JSONDecodeError:
                logging.info("Error decoding JSON file, defaulting to empty database")
                database = {}
        return database

    def create_key(self, key):
        self._database = self.return_database()
        self._database[key] = ""
        self.save_as_json()

    def delete_key(self, key):
        if self._database[key] == "":
            print("this key doesn't exist")
        else:
            self._database.pop(key)
        self.save_as_json()

    def delete_value(self, key):
        self._database = self.return_database()
        self._database[key] = ""
        self.save_as_json()

    def delete_all_values(self):
        for key in self._database:
            self.delete_value(key)

    def return_database(self):
        with open(self._database_file) as f:
            try:
                database = json.load(f)
            except json.JSONDecodeError:
                logging.info("Error decoding JSON file, defaulting to empty database")
                database = {}
        return database

    def delete_database_file(self):
        os.remove(self._database_file)

    def get_keys(self):
        self._database = self.return_database()
        return [i for i in self._database.keys()]
