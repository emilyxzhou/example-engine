from interaction_engine.node import Node


class Interaction:
#dictionary_of_nodes should have key "start" and key "quit"
    def __init__(self):
        #self._dictionary_of_nodes = dictionary_of_nodes
        self._dictionary_of_nodes = {}
        self._dictionary_of_user_input = {}

    def add_node(self, key, node):
        if not type(key) is str:
            raise TypeError("Only strings are allowed for the new node's key")
        if not type(node) is Node:
            raise TypeError("Only Nodes are allowed for the new node body")
        self._dictionary_of_nodes[key] = node

    def delete_node(self, key):
        if not type(key) is str:
            raise TypeError("Only strings are allowed for the node's key")
        self._dictionary_of_nodes.pop(key)

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

    def print_question_and_options(self, current_node):
        if not type(current_node) is Node:
            raise TypeError("Only Nodes are allowed to pass in for print_question")
        print(current_node.question)
        for option in current_node.array_of_options:
            print(option.option_content)

    def go_to_next_node(self, current_node, choice_index):
        return self._dictionary_of_nodes[current_node.get_next_node_key(choice_index)]

    def interact(self):
        choice_index = -1
        current_node = self._dictionary_of_nodes["start"]
        self.print_question_and_options(current_node)
        choice_index = input()
        while current_node.get_next_node_key(choice_index) != "quit":
            self.print_question_and_options(current_node)
            choice_index = input()
            current_node = self.go_to_next_node(current_node, choice_index)


