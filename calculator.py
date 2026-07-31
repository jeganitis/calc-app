"""
Calculator Application - Phase 3
Supports: addition (+), subtraction (-),
          multiplication (*), division (/), modulo (%), square root (√)
Built with Python tkinter.
"""

import math
import tkinter as tk


class Calculator:
    """A simple GUI calculator supporting +, -, *, / operations."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self._build_display()
        self._build_buttons()

    def _build_display(self) -> None:
        """Create the text display at the top of the calculator."""
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            state="readonly",
            readonlybackground="white",
            bd=10,
            relief="flat",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew",
                     padx=10, pady=10)

    def _build_buttons(self) -> None:
        """Create the calculator button grid."""
        # Button layout: label, row, column
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 0), (".", 4, 1),
            ("+", 1, 3), ("-", 2, 3),
            ("*", 3, 3), ("%", 5, 2),
            ("/", 4, 3),
            ("=", 5, 3), ("C", 5, 0), ("⌫", 5, 1), ("√", 4, 2),
        ]
        btn_style = {
            "font":   ("Arial", 16),
            "width":  5,
            "height": 2,
            "bd":     1,
            "relief": "raised",
            "bg":     "#f0f0f0",
            "activebackground": "#d0d0d0",
        }
        operator_style = {**btn_style, "bg": "#ffd700",
                          "activebackground": "#e6c200"}
        special_style  = {**btn_style, "bg": "#ff6b6b",
                          "activebackground": "#e55555",
                          "fg": "white"}

        for label, row, col in buttons:
            if label in ("+", "-", "*", "/", "%"):
                style = operator_style
            elif label in ("=", "C", "⌫", "√"):
                style = special_style
            else:
                style = btn_style

            tk.Button(
                self.root,
                text=label,
                command=lambda l=label: self._on_button(l),
                **style,
            ).grid(row=row, column=col, padx=3, pady=3)

    def _on_button(self, label: str) -> None:
        """Handle a button press."""
        if label == "C":
            self.expression = ""
            self.display_var.set("0")

        elif label == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")

        elif label == "√":
            self._sqrt()

        elif label == "=":
            self._evaluate()

        else:
            self.expression += label
            self.display_var.set(self.expression)

    def _sqrt(self) -> None:
        """Calculate the square root of the current expression."""
        try:
            allowed_chars = set("0123456789.+-*/%")
            if not all(c in allowed_chars for c in self.expression):
                raise ValueError("Invalid characters in expression.")
            value = eval(self.expression)  # noqa: S307
            if value < 0:
                self.display_var.set("Error: Neg√")
                self.expression = ""
            else:
                result = math.sqrt(value)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display_var.set(str(result))
                self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("Error: Div/0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def _evaluate(self) -> None:
        """Evaluate the current expression and show the result."""
        try:
            # Allow +, -, *, /, % operators (Phase 3)
            allowed_chars = set("0123456789.+-*/%")
            if not all(c in allowed_chars for c in self.expression):
                raise ValueError("Invalid characters in expression.")
            result = eval(self.expression)   # noqa: S307
            # Format: hide .0 for whole numbers
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("Error: Div/0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""


def main() -> None:
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
