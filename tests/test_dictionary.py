import unittest
from interaction_engine.dictionary import Dictionary
from interaction_engine.node import Node
from interaction_engine.option import Option


class TestDictionary(unittest.TestCase):
    def test_add_with_valid_content(self):
        node = Node("Shall we Start?", [Option("Yes", "node1"), Option("No", "quit")])
        dictionary = Dictionary()
        dictionary.add_node("start", node)
        for saved_node in dictionary.get_dictionary_of_nodes():
            self.assertEqual(node, saved_node)

    def test_add_with_invalid_content(self):
        invalid_contents = [
            3,
            ["Yes", "No"]
        ]

        for invalid_content in invalid_contents:
            self.assertRaises(
                TypeError,
                Node,
                "start", invalid_content
            )

    def delete_node(self, key):
        node1 = Node("Shall we Start?", [Option("Yes", "node1"), Option("No", "quit")])
        node2 = Node("Shall we Start?", [Option("Yes", "node1"), Option("No", "quit")])
        dictionary = Dictionary()
        dictionary.add_node("start", node1)
        dictionary.add_node("start", node2)


if __name__ == '__main__':
    unittest.main()
