import unittest
from interaction_engine.option import Option
from interaction_engine.node import Node
from interaction_engine.interaction import Interaction


class TestInteraction(unittest.TestCase):
    def test_interaction(self):
        option1 = Option("Ok", "satisfaction level")
        option2 = Option("No", "quit")
        option3 = Option("satisfied", "quit")
        option4 = Option("not satisfied", "problem report")
        node1 = Node("Hello, let's start", [option1, option2])
        node2 = Node("Are you satisfied by current service?", [option3, option4])
        interaction = Interaction()
        interaction.add_node("start", node1)
        interaction.add_node("satisfaction level", node2)
        interaction.interact()#can I test interacton() here?


if __name__ == "__main__":
    unittest.main()