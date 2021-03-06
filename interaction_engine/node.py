from interaction_engine.option import Option


class Node:  # each interaction round with user

    def __init__(self, question, array_of_options):
        if not type(question) is str:
            raise TypeError("Only strings are allowed for question")
        for option in array_of_options:
            if not type(option) is Option:
                raise TypeError("Only Options are allowed for options")
        self._question = question
        self._array_of_options = array_of_options

    def get_next_node_key(self, input_choice_index):
        return self._array_of_options[input_choice_index].next_node_key

    @property
    def array_of_options(self):
        return self._array_of_options

    @property
    def question(self):
        return self._question
