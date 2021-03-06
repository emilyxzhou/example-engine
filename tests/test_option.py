import unittest
from interaction_engine.option import Option


class TestOption(unittest.TestCase):
        def test_init_with_valid_content(self):
                valid_contents = [
                        "yes", "no"
                ]
                for content in valid_contents:
                        option=Option(content, "Node2")
                        self.assertEqual(option.option_content, content)

        def test_init_with_invalid_content(self):
                invalid_contents = [
                        3,
                        ["Yes", "No"]
                ]

                for invalid_content in invalid_contents:
                        self.assertRaises(
                                TypeError,
                                Option,
                                invalid_content, "node1"
                        )


if __name__ == "__main__":
        unittest.main()
