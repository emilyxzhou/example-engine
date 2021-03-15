from interaction_engine.node import Node
from interaction_engine.dictionary import Dictionary
from interaction_engine.user_input import UserInput


class Interaction:
    # dictionary_of_nodes should have key "start" and key "quit"
    def __init__(self, dictionary, user_input):
        if not type(dictionary) is Dictionary:
            raise TypeError("Only Dictionary is allowed")
        self.dictionary = dictionary
        if not type(user_input) is UserInput:
            raise TypeError("Only User_input is allowed")
        self.user_input = user_input
        self.current_node = self.dictionary.get_dictionary_of_nodes["start"]

    def print_question_and_options(self, current_node):
        if not type(current_node) is Node:
            raise TypeError("Only Nodes are allowed to pass in for print_question")
        print(current_node.question)
        for option in current_node.array_of_options:
            print(option.option_content)

    def interact(self):
        self.print_question_and_options(self.current_node)
        choice_index = input()
        while self.current_node.get_next_node_key(choice_index) != "quit":
            self.print_question_and_options(self.current_node)
            choice_index = input()
            self.current_node = self.dictionary.go_to_next_node(self.current_node, choice_index)


