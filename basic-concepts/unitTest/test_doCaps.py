import unittest

import doCaps


class TestCapitalize(unittest.TestCase):

    def test_one_word(self):
        text = "hello"
        result = doCaps.cap_text(text)
        self.assertEqual(result, "Hello");

    def test_word(self):
        text = "my name is Anthony golzanves"
        result = doCaps.cap_text(text)
        self.assertEqual(result, "My Name Is Anthony Golzanves");

    def test_word(self):
        text = None
        result = doCaps.cap_text(text)
        self.assertEqual(result, None);

    def test_exception_for_non_string_input(self):
        text = 12345
        with self.assertRaises(TypeError):
            result = doCaps.cap_text(text)

    def test_exception_message_for_non_string_input(self):
        text = 12345
        with self.assertRaisesRegex(TypeError,
                                    "Business Error Message : ABC123454 : Incorrect Type passed - Not a String"):
            caps = doCaps.cap_text(text)

    def test_exception_error_message_for_non_string_input(self):
        text = 12345
        with self.assertRaisesRegex(TypeError, "ABC123454"):
            caps = doCaps.cap_text(text)


if __name__ == "__main__":
    unittest.main();
