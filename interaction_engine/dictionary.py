from interaction_engine.node import Node


class Dictionary:
    def __init__(self):
        self._dictionary_of_nodes = {}

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

    def go_to_next_node(self, current_node, choice_index):
        return self._dictionary_of_nodes[current_node.get_next_node_key(choice_index)]

    def get_dictionary_of_nodes(self):
        return self._dictionary_of_nodes
