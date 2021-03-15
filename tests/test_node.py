import unittest
from interaction_engine.node import Node
from interaction_engine.option import Option


class TestNode(unittest.TestCase):
    def test_init_with_valid_content(self):
        valid_contents = [
                         [Option("Yes", "node1"), Option("No", "quit")],
                         [Option("Start", "node1"), Option("Exit", "quit")]
        ]

        for option_array in valid_contents:
            node = Node("Shall we Start?", option_array)
            self.assertEqual(node.array_of_options, option_array)

    def test_init_with_invalid_content(self):
        invalid_contents = [
            3,
            ["Yes", "No"]
        ]

        for invalid_content in invalid_contents:
            self.assertRaises(
                TypeError,
                Option,
                "Shall we Start?", invalid_content
            )


if __name__ == "__main__":
    unittest.main()
