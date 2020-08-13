import unittest
import gsheets_formula_usage


class GSheetsFunctionUsageTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(gsheets_formula_usage.__version__, '0.1.0')


if __name__ == '__main__':
    unittest.main()
