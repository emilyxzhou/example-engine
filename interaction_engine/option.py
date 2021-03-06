class Option:

    def __init__(self, option_content, next_node_key):
        if not type(option_content) is str:
            raise TypeError("Only strings are allowed for option content")
        if not type(next_node_key) is str:
            raise TypeError("Only strings are allowed for key of next node")
        self._option_content = option_content
        self._next_node_key = next_node_key

    @property
    def option_content(self):
        return self._option_content

    @property
    def next_node_key(self):
        return self._next_node_key
