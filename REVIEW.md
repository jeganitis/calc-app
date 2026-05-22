# Code Review Guidelines — calc-app

## What to Look For

### Critical (must fix before merge)
- Division by zero not handled
- eval() called without the allowed_chars guard
- New operators added to buttons but not to allowed_chars
- Application crashes on invalid input

### Warning (should fix)
- Missing docstring on a new method or class
- Missing type hints on function signatures
- Hardcoded strings that should be constants
- Duplicate button configuration code

### Suggestion (nice to have)
- More descriptive variable names
- Additional inline comments explaining logic
- Separating operator style config into a dict

## What NOT to Flag
- Formatting differences (we do not enforce Black in this project)
- Test coverage (tests are not required in Phase 1 or Phase 2)
- The use of eval() itself — it is intentional and guarded

## Tone
- Be constructive, not critical
- Provide a concrete fix for every warning and critical issue
- Keep comments under 100 words each
