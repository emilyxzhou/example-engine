from interaction_engine.dictionary import DictionaryOfNode
from interaction_engine.database import Database
from interaction_engine.interface import Interface


class Interaction:
    # dictionary_of_nodes should have key "start" and key "quit"
    def __init__(self, dictionary, database):
        if not type(dictionary) is DictionaryOfNode:
            raise TypeError("Only Dictionary is allowed")
        self.dictionary = dictionary
        if not type(database) is Database:
            raise TypeError("Only Database is allowed")
        self.database = database
        self.current_node = self.dictionary.get_dictionary_of_nodes["start"]

    def interact(self):
        choice_index = 1
        interface = Interface(self.current_node)
        while self.current_node.get_next_node_key(choice_index) != "quit":
            interface.print_question_and_options()
            interface.go_to_next_node()


