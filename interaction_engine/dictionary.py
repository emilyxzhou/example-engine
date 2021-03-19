from interaction_engine.node import Node


class DictionaryOfNode:
    def __init__(self):
        self._dictionary_of_nodes = {}

    def go_to_next_node(self, current_node, choice_index):
        return self._dictionary_of_nodes[current_node.get_next_node_key(choice_index)]

    def get_dictionary_of_nodes(self):
        return self._dictionary_of_nodes
