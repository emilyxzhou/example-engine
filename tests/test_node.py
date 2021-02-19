import unittest
from node import Node
from option import Option

class Test_node(unittest.TestCase):
    def test_node(self):
        option1 = Option("Ok", "satisfaction level")
        option2 = Option("No", "quit")
        node = Node("Hello, let's start", [option1, option2], "greeting")
        self.assertEqual(node.question(), "Hello, let's start")
        self.assertEqual(node.array_of_options(), [option1, option2])
        self.assertEqual(node.key(), "greeting")


if __name__ == "__main__":
    unittest.main()