import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import greet, main


def run_main(argv):
    """Run main() with the given arguments and return (exit_code, stdout)."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        code = main(argv)
    return code, buffer.getvalue()


class GreetTests(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Minura"), "Hello, Minura! Welcome to test-repo.")

    def test_greet_without_name(self):
        self.assertEqual(greet(), "Hello, friend! Welcome to test-repo.")


class MainTests(unittest.TestCase):
    def test_main_prints_greeting(self):
        code, output = run_main(["Minura"])
        self.assertEqual(code, 0)
        self.assertEqual(output, "Hello, Minura! Welcome to test-repo.\n")

    def test_shout_flag_prints_uppercase(self):
        code, output = run_main(["--shout", "Minura"])
        self.assertEqual(code, 0)
        self.assertEqual(output, "HELLO, MINURA! WELCOME TO TEST-REPO.\n")

    def test_shout_flag_after_name(self):
        _, output = run_main(["Minura", "--shout"])
        self.assertEqual(output, "HELLO, MINURA! WELCOME TO TEST-REPO.\n")

    def test_shout_flag_without_name(self):
        _, output = run_main(["--shout"])
        self.assertEqual(output, "HELLO, FRIEND! WELCOME TO TEST-REPO.\n")


if __name__ == "__main__":
    unittest.main()
