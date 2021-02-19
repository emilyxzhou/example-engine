class Node:  # each interaction round with user

    def __init__(self, question, array_of_options):
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
