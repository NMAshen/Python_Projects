# Bulletproof Python Calculator

A command-line calculator built with Python that handles user inputs safely and prevents crashes.

## Features
- **Input Validation**: Detects and exits gracefully if a user leaves a field blank.
- **Type Safety**: Uses `try-except` blocks to handle non-numeric inputs (like letters or symbols) without crashing.
- **Edge Case Protection**: Prevents `ZeroDivisionError` when dividing by zero.
- **Clean Outputs**: Automatically rounds floating-point results to 2 decimal places.

## How to Run
Ensure you have Python installed, then run:
```bash
python calculator.py
