import importlib.util
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location("categoriser", Path(__file__).resolve().parents[1] / "Work Experience Code.py")
categoriser = importlib.util.module_from_spec(spec)
spec.loader.exec_module(categoriser)


class CategoriserTests(unittest.TestCase):
    def test_case_and_spacing(self):
        self.assertEqual(categoriser.categorise_transaction("  TESCO   Express "), "Food")

    def test_unknown_transaction(self):
        self.assertEqual(categoriser.categorise_transaction("Unlisted merchant"), "Other")

    def test_transport(self):
        self.assertEqual(categoriser.categorise_transaction("Train ticket"), "Transport")


if __name__ == "__main__":
    unittest.main()
