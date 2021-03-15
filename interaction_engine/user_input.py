class UserInput:
    def __init__(self):
        self._dictionary_of_user_input = {}

    def add_user_input(self, key, input):
        if not type(key) is str:
            raise TypeError("Only strings are allowed for the user input's key")
        if not type(input) is str:
            raise TypeError("Only strings are allowed for the user input's body")
        self._dictionary_of_user_input[key] = input

    def delete_user_input(self, key):
        if not type(key) is str:
            raise TypeError("Only strings are allowed for the user input's key")
        self._dictionary_of_user_input.pop(key)