"""A tiny greeting command-line tool used to practise the GitHub workflow."""

import sys


def greet(name=None):
    """Return a greeting message for the given name."""
    if name is None or not name.strip():
        name = "friend"
    return f"Hello, {name.strip()}! Welcome to test-repo."


def main(argv=None):
    """Run the command-line interface and return an exit code."""
    args = sys.argv[1:] if argv is None else argv
    name = " ".join(args) if args else None
    print(greet(name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
