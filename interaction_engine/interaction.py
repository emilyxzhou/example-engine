from interaction_engine.node import Node


class Interaction:
#dictionary_of_nodes should have key "start" and key "quit"
    def __init__(self):
        #self._dictionary_of_nodes = dictionary_of_nodes
        self._dictionary_of_nodes = {}
        self._dictionary_of_user_input = {}

    def add_node(self, key, node):
        assert isinstance(key, str)
        assert isinstance(node, Node)
        self._dictionary_of_nodes[key] = node

    def delete_node(self, key):
        assert isinstance(key, str)
        self._dictionary_of_nodes.pop(key)

    def add_user_input(self, key, input):
        assert isinstance(key, str)
        assert isinstance(input, str)
        self._dictionary_of_user_input[key] = input

    def delete_user_input(self, key):
        assert isinstance(key, str)
        self._dictionary_of_user_input.pop(key)

    def interact(self):
        choice_index = -1
        current_node = self._dictionary_of_nodes["start"]
        while current_node.get_next_node_key(choice_index) != "quit":
            print(current_node.question)
            for options in current_node.array_of_options:
                print(options)
            choice_index = input()
            current_node = self._dictionary_of_nodes[current_node.get_next_node_key(choice_index)]


