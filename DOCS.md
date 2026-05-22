# Calculator Application Documentation

## Class: Calculator

### Constructor
- **Parameters:** `root: tk.Tk`
- **Purpose:** Initializes the calculator with a tkinter window

### Methods
- `_build_display()` - Creates the text display at the top
- `_build_buttons()` - Creates the calculator button grid
- `_on_button(label)` - Handles button press events
- `_evaluate()` - Evaluates the expression and shows the result

## Supported Operators

| Operator | Symbol | Example |
|----------|--------|---------|
| Addition | + | 5 + 3 = 8 |
| Subtraction | - | 5 - 3 = 2 |
| Multiplication | * | 5 * 3 = 15 |
| Division | / | 6 / 3 = 2 |

All operators are validated through the `allowed_chars` guard in the `_evaluate()` method.

## Function: main()

**Purpose:** Initializes and runs the calculator application

**Returns:** None (blocking; runs until user closes window)

## Known Limitations

- The `eval()` function is used with a character whitelist guard
- Only supports numeric operators (+, -, *, /)
- Division by zero shows "Error: Div/0"
- Invalid expressions show "Error"
- No support for parentheses or complex expressions

---

_Documentation auto-generated_
