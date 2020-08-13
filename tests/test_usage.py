import unittest
import string
from gsheets_formula_usage import Index


class IndexTest(unittest.TestCase):
    def test_normal_alphabet(self):
        for index, letter in enumerate(string.ascii_uppercase):
            self.assertEqual(Index.to_letter(index), letter)

    def test_beyond_alphabet(self):
        index = len(string.ascii_lowercase)
        letter = 'AA'
        self.assertEqual(Index.to_letter(index), letter)
