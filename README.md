# Python Jour 2 - Les Boucles

[![Tests](https://github.com/mugire-can/Python-Jour-2---Les-Boucles/actions/workflows/python-tests.yml/badge.svg)](https://github.com/mugire-can/Python-Jour-2---Les-Boucles/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

Training project for learning Python loops (`for` and `while` statements).

## Overview

This project contains 9 programming exercises focusing on loop structures and control flow in Python. The exercises progress from simple iteration to more complex loop patterns.

## Exercises (Jobs)

### Job 01: Display Numbers 0-20
Display all integers from 0 to 20 using a `for` loop.

### Job 02: Display Every Other Number 0-20
Display every second number from 0 to 20 using a `for` loop with step.

### Job 03: Display Squares
Display numbers from 1 to 20 and their squares (n²).

### Job 04: Multiplication Tables
Display multiplication tables from 1 to N, where N is user-provided input.

### Job 05: Convert For Loop to While
Convert the Job 01 logic (0 to 12) from a `for` loop to a `while` loop.

### Job 06: Multiplication by 7
Use a `while` loop to display multiplication results of user-input number N by 7 (first 10 results).

### Job 07: Loop with Expression
Execute a loop 12 times and display: (iteration × 3) - 2

### Job 08: Loop with Addition
Execute a loop 12 times and display: iteration + 2

### Job 09: Even and Odd Numbers
Display all numbers from 1 to 30, labeling each as "Pair" (even) or "Impair" (odd).

## Usage

```bash
python projet\ jour\ 2.py
```

Or run directly:

```bash
python "projet jour 2.py"
```

**Note:** Jobs 04 and 06 require user input during execution.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Testing

Run the comprehensive test suite:

```bash
pytest test_projet.py -v
```

Run with coverage report:

```bash
pytest test_projet.py --cov=. --cov-report=html
```

**Test Results:**
- Total Tests: 9
- Status: All Passing ✓
- Coverage: All exercises covered

## CI/CD

This project uses **GitHub Actions** for continuous integration and continuous deployment.

**Automated Checks:**
- ✅ Run tests on Python 3.8, 3.9, 3.10, 3.11
- ✅ Code quality checks with flake8 and pylint
- ✅ Python syntax validation
- ✅ Code coverage reporting with Codecov

**Workflow triggers:**
- On every push to `main` or `Working` branches
- On pull requests to `main` or `Working` branches

View the workflow: [`.github/workflows/python-tests.yml`](.github/workflows/python-tests.yml)

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Structure

```
.
├── projet jour 2.py                          # Main exercise file with all 9 jobs
├── test_projet.py                            # Unit tests (9 comprehensive tests)
├── requirements.txt                          # Project dependencies
├── LICENSE                                   # MIT License
├── README.md                                 # This file
├── .gitignore                                # Git ignore patterns
├── .github/
│   └── workflows/
│       └── python-tests.yml                  # GitHub Actions CI/CD configuration
└── Python Jour 2 - Les Boucles.pdf          # Original course material
```

## Key Learning Outcomes

- ✅ Understanding `for` loops with ranges and steps
- ✅ Understanding `while` loops and loop control
- ✅ Nested loops (multiplication tables)
- ✅ String formatting with f-strings
- ✅ Conditional logic within loops (even/odd detection)
- ✅ User input handling with `input()` and type conversion
- ✅ Unit testing with pytest
- ✅ Automated CI/CD with GitHub Actions
- ✅ Professional project practices

## Notes

- All exercises use French variable names and output strings to match the course material
- The PDF document (`Python Jour 2 - Les Boucles.pdf`) contains the original course content and requirements
- Each job is clearly commented in the source code

## Author

Created for La Plateforme training program.
