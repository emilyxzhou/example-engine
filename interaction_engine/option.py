class Option:

    def __init__(self, option_content, next_node_key):
        assert isinstance(option_content, str)
        assert isinstance(next_node_key, str)
        self._option_content = option_content
        self._next_node_key = next_node_key

    @property
    def option_content(self):
        return self._option_content

    @property
    def next_node_key(self):
        return self._next_node_key
