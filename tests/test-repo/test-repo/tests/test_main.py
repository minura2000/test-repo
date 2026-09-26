import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import greet, main  # noqa: E402


class TestGreet(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Minura"), "Hello, Minura! Welcome to test-repo.")

    def test_default_name_when_none(self):
        self.assertEqual(greet(None), "Hello, friend! Welcome to test-repo.")

    def test_default_name_when_blank(self):
        self.assertEqual(greet("   "), "Hello, friend! Welcome to test-repo.")

    def test_strips_whitespace(self):
        self.assertEqual(greet("  Sahasra "), "Hello, Sahasra! Welcome to test-repo.")


class TestMain(unittest.TestCase):
    def run_main(self, argv):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = main(argv)
        return code, buffer.getvalue()

    def test_main_with_name(self):
        code, out = self.run_main(["Minura"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "Hello, Minura! Welcome to test-repo.\n")

    def test_main_with_multiple_words(self):
        code, out = self.run_main(["Minura", "Hansana"])
        self.assertEqual(code, 0)
        self.assertIn("Minura Hansana", out)

    def test_main_without_args(self):
        code, out = self.run_main([])
        self.assertEqual(code, 0)
        self.assertIn("friend", out)


if __name__ == "__main__":
    unittest.main()
