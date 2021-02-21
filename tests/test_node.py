import unittest
from interaction_engine.node import Node
from interaction_engine.option import Option


class TestNode(unittest.TestCase):
    def test_node(self):
        option1 = Option("Ok", "satisfaction level")
        option2 = Option("No", "quit")
        node = Node("Hello, let's start", [option1, option2])
        assert isinstance(node._question, str)
        for options in self._array_of_options:
            assert isinstance(options, Option)

if __name__ == "__main__":
    unittest.main()
