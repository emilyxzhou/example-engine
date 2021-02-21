import unittest
from interaction_engine.option import Option


class TestOption(unittest.TestCase):
        def test_option(self):
                option1 = Option("Ok", "satisfaction level")
                option2 = Option("No", "quit")
                assert isinstance(option1._option_content, str)
                assert isinstance(option2._option_content, str)
                assert isinstance(option1._next_node_key, str)
                assert isinstance(option2._next_node_key, str)


if __name__ == "__main__":
        unittest.main()
