# Competitive Companion

**A Python tool for testing and debugging competitive programming solutions.**

Competitive Companion helps competitive programmers test their solutions against sample inputs and expected outputs, making it easier to catch mistakes before submitting to an online judge.

## Features

- **Run solutions** — Execute a Python solution with custom test input.
- **Check answers** — Compare the program's output against the expected output.
- **Show results** — Clearly display whether the solution passed or failed.
- **Set time limits** — Stop solutions that exceed the configured execution timeout.

## Project Status

🚧 **Early development**

The initial version focuses on running Python solutions and checking their outputs. More debugging tools and helpful error explanations may be added as the project develops.

## Project Structure

```text
competitive_companion/
├── pyproject.toml
├── README.md
└── src/
    └── competitive_companion/
        ├── __init__.py
        └── main.py
```

## Requirements

- Python 3.10 or newer
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/competitive_companion.git
cd competitive_companion
```

Install the package in editable mode:

```bash
python3 -m pip install -e .
```

## Usage

Run a Python solution with a test input and expected output:

```bash
cc solution.py --input "2 3" --expected "5"
```

For example, `solution.py` could contain:

```python
a, b = map(int, input().split())
print(a + b)
```

Expected result:

```text
CORRECT ANSWER!!!
=====================
Input: 2 3

Output: 5
Target output: 5
```

If the output does not match the expected answer, Competitive Companion reports a wrong answer.

> **Note:** The initial CLI is designed for simple test inputs. Support for test files, multiple test cases, and more detailed debugging can be added in future versions.

## Roadmap

- [x] Run Python solutions
- [x] Compare actual and expected output
- [x] Report correct and incorrect answers
- [ ] Support test cases stored in files
- [ ] Identify the first output mismatch
- [ ] Provide more useful error messages
- [ ] Add automated tests
- [ ] Support additional programming languages

## Safety

Only run code you trust. Competitive Companion currently runs solutions as local processes; a timeout does not make untrusted code safe.

## Contributing

Contributions, bug reports, and feature suggestions are welcome!

## License

This project is licensed under the MIT License. Add a `LICENSE` file before distributing the project under that license.
# Competitive Companion

A Python tool for competitive programmers to test solutions, compare outputs, and catch mistakes.

## Features

- Run Python solutions with custom test inputs
- Compare actual output with expected output
- Identify correct and incorrect answers
- Apply execution time limits

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/competitive_companion.git
cd competitive_companion
python3 -m pip install -e .
```

## Usage

```bash
cc solution.py --input "2 3" --expected "5"
```

Example solution:

```python
a, b = map(int, input().split())
print(a + b)
```

Competitive Companion runs the solution and checks whether its output matches the expected result.

## Roadmap

- [x] Run Python solutions
- [x] Compare outputs
- [ ] Support test case files
- [ ] Detect output mismatches
- [ ] Provide debugging suggestions
- [ ] Support more programming languages

## Contributing

Suggestions, bug reports, and contributions are welcome!

## License

See the `LICENSE` file for licensing information.
