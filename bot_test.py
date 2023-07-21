import unittest
from bot import capitalize_first_letter, upper_last_word, format_message_norm

class TestFunctions(unittest.TestCase):
    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter("juri stand lp"), "Juri Stand Lp")
        self.assertEqual(capitalize_first_letter("test case"), "Test Case")
        self.assertEqual(capitalize_first_letter("UPPERCASE WORDS"), "Uppercase Words")

    def test_upper_last_word(self):
        self.assertEqual(upper_last_word("juri stand lp"), "juri stand LP")
        self.assertEqual(upper_last_word("test case"), "test CASE")
        self.assertEqual(upper_last_word("ALL UPPERCASE"), "ALL UPPERCASE")

    def test_format_message_norm(self):
        character_name = 'Ryu'
        msg = {
            'moveName': 'crouch MP',
            'startup': 6,
            'active': 6,
            'recovery': 4,
            'onBlock': -1,
            'onHit': 4,
            'extraInfo': ['Very cool', 'Really strong']
        }

        formatted_msg = format_message_norm(msg, character_name)
        expected_msg = (
            ">>> ### Ryu - crouch MP\n"
            "**Startup:**  6      **Active:**  6      **Recovery:**  4\n"
            "**On Block:**  -1      **On Hit:**  4\n"
            "**__Extra Info:__**\n"
            "- Very cool\n"
            "- Really strong"
        )
        self.assertEqual(formatted_msg, expected_msg)

unittest.main()