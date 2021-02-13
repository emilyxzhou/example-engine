import unittest

from example_engine.option import Option


class TestOption(unittest.TestCase):

    def test_init_with_valid_content(self):
        valid_contents = [
            "Yes",
            "No",
        ]

        for valid_content in valid_contents:
            option = Option(valid_content, "node1")
            self.assertEqual(option.option_content, valid_content)

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
