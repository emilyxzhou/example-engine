class Option:

    def __init__(self, option_content, next_node_key):

        if type(option_content) is not str:
            raise TypeError("Option content must be string")

        self._option_content = option_content
        self._next_node_key = next_node_key

    @property
    def option_content(self):
        return self._option_content

    @property
    def next_node_key(self):
        return self._next_node_key


if __name__ == "__main__":

    my_option = Option("Yes", "node1")
    my_option2 = Option(3, "node1")
