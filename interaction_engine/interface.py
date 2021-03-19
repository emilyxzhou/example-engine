from interaction_engine.node import Node


class Interface:
    def __init__(self, current_node):
        if not type(current_node) is Node:
            raise TypeError("Only Nodes are allowed to pass in for print_question")
        self._choice_index = 1
        self._current_node = current_node

    def print_question_and_options(self):
        print(self._current_node.question)
        for option in self._current_node.array_of_options:
            print(option.option_content)

    def go_to_next_node(self):
        self._choice_index = input()
        self._current_node = self.dictionary.go_to_next_node(self.current_node, self._choice_index)