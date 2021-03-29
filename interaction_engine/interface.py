from interaction_engine.node import Node


class Interface:
    def __init__(self):
        self._choice_index = 1

    def print_question_and_options(self):
        print(self._current_node.question)
        for option in self._current_node.array_of_options:
            print(option.option_content)

    def go_to_next_node(self):
        self._choice_index = input()
        #if not type input is int or input!=1-options.size(), print error and continue looping
        self._current_node = self.dictionary.go_to_next_node(self.current_node, self._choice_index)

    def run(self, current_node):
        if not type(current_node) is Node:
            raise TypeError("Only Nodes are allowed to pass in for print_question")
        self.print_question_and_options()
        self.go_to_next_node()