# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**calc-app** is a Python tkinter calculator application. It's in Phase 3, supporting basic arithmetic operators: addition (+), subtraction (-), multiplication (*), division (/), and modulo (%).

The calculator has a single entry point and class (`Calculator`) that manages the GUI, expression tracking, and evaluation logic.

## Running the Application

```bash
python3 calculator.py
```

This launches the tkinter GUI window. The calculator:
- Accepts numeric input (0-9 and decimal points)
- Supports operators: +, -, *, /, %
- Displays results with a read-only display widget
- Handles division by zero with an error message
- Provides Clear (C) and Backspace (⌫) buttons

## Architecture

### Single File Design
- **calculator.py**: Contains the `Calculator` class and `main()` entry point
  - `Calculator.__init__()`: Initializes the tkinter root and builds UI
  - `_build_display()`: Creates the read-only display widget
  - `_build_buttons()`: Creates the button grid with styling logic
  - `_on_button()`: Handles button presses (operators, digits, special functions)
  - `_evaluate()`: Evaluates the expression using `eval()` with an `allowed_chars` guard

### Key Design Details

**Expression Tracking**: The `expression` string accumulates button presses and is displayed in real time. When "=" is pressed, it's evaluated and the result becomes the new expression.

**eval() Safety**: The `_evaluate()` method uses Python's `eval()` with an `allowed_chars` whitelist guard that permits only `0-9.+-*/%`. This prevents arbitrary code execution. When adding new operators, update the `allowed_chars` set.

**Button Styling**: Three style profiles (default, operator, special) are applied based on button type. This is determined by checking `label` membership in tuples. When adding operators, update the operator tuple check.

**Error Handling**: Division by zero catches `ZeroDivisionError` explicitly; all other exceptions catch with a generic "Error" display.

## Development Commands

No external dependencies are required—tkinter is part of Python's standard library.

### Running the App
```bash
python3 calculator.py
```

### Manual Testing
Launch the app and verify:
- Number input displays correctly
- Each operator (+, -, *, /, %) works
- Chained operations evaluate correctly (e.g., 2+3*4 = 14, 10%3 = 1)
- Division by zero shows "Error: Div/0"
- Backspace removes the last character
- Clear resets the expression and display to "0"
- Decimal points work

## Continuous Integration

Two automated workflows run on main:

**PR Review** (`.github/workflows/pr-review.yml`):
- Runs on new/updated PRs that touch `**.py`
- Posts inline comments on code review findings
- Focuses on: correctness, edge cases, eval() safety, type hints, and style consistency

**Auto Documentation** (`.github/workflows/auto-docs.yml`):
- Runs on push to main after changes to `**.py`
- Auto-generates/updates README.md and DOCS.md
- Uses the `anthropics/claude-code-action` to invoke Claude Code
- Commits changes as `claude-doc-agent[bot]`

See the workflow files for specific review criteria and documentation requirements.

## Future Development

When adding operators:
1. Add the button definition to the `buttons` list in `_build_buttons()` with its row/column position
2. Update the `operator_style` check to include the new operator
3. Update `allowed_chars` in `_evaluate()` to include the operator character

When changing evaluation logic, ensure the `allowed_chars` guard remains effective and all error cases are covered.
