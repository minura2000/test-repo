# test-repo

A small, complete starter repository by [Minura Hansana](https://github.com/minura2000), made to practise the GitHub workflow and to try Claude Code cloud sessions.

It contains a tiny Python command-line tool (`greeter`) with unit tests, so there is real code for Claude Code to read, run and change.

## Features

- `greet(name)` builds a greeting message
- Simple command-line interface
- Unit tests using Python's built-in `unittest` (no extra packages needed)

## Getting Started

Requires Python 3.8 or newer.

```bash
git clone https://github.com/minura2000/test-repo.git
cd test-repo
python main.py Minura
```

Output:

```
Hello, Minura! Welcome to test-repo.
```

Run without a name to get a default greeting:

```bash
python main.py
```

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```
test-repo/
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── tests/
    └── test_main.py
```

## Trying Claude Code on this repo

Once this repo is connected to your Claude account, start a cloud session and try prompts like:

- "Add a `--shout` flag to main.py that prints the greeting in uppercase, and add a test for it"
- "Add a `--times N` option that repeats the greeting N times"
- "Review this repo and suggest improvements"

## License

Released under the MIT License. See [LICENSE](LICENSE).
