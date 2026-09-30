# Complex Calculator

A menu-driven command-line calculator written in Python. It can add, subtract, multiply and divide **any number of values in one go**, and it can also raise a number to a power.

## Features

- Add, subtract, multiply and divide a whole list of numbers (not just two)
- Exponent (power) calculation
- Simple menu that keeps running until you choose to exit
- Clear error messages for invalid input, empty input and division by zero
- Modular code split across three files (calculations, input handling, program flow)

## Project Structure

```
complex_calculator/
├── main.py            # entry point: menus and program flow
├── operations.py      # calculation functions
└── input_handler.py   # functions that read input from the user
```

| File | What it does |
|------|--------------|
| `main.py` | Starts the program and runs the menu loops. **Run this file.** |
| `operations.py` | Contains `add`, `sub`, `multi`, `div` and `power`. |
| `input_handler.py` | Shows the menus and reads the user's choices and numbers. |

## Requirements

- Python 3 (no external libraries needed)

## How to Run

Keep `main.py`, `operations.py` and `input_handler.py` together in the same folder, open a terminal in that folder and run:

```
python main.py
```

On some systems (Linux/macOS) you may need to use `python3 main.py` instead.

## How to Use

### Main menu

| Enter | Action |
|-------|--------|
| `0` | Basic calculator: add, subtract, multiply, divide |
| `1` | Exponent: raise a number to a power |
| `2` | Exit the program |

Any other input shows an "Invalid input" message and the menu appears again.

### Basic calculator (option 0)

1. Choose an operation: `+` add, `-` subtract, `*` multiply, `/` divide. Enter `q` to go back to the main menu.
2. Enter your numbers one by one, pressing Enter after each one.
3. Type `E` (or `e`) when you have entered all the numbers. The result is displayed.
4. You return to the operation prompt and can do another calculation.

### Exponent (option 1)

Enter the number (base) and then the power. The program prints the result of `base ** power`.

## Example Session

**Adding numbers**

```
enter your choice: 0
operations: add[+] substract[-] multiply[*]  divide[/] quit[q]
enter your choice: +
enter number one by one
type 'E' or 'e' to exit the calculator
Enter a number(or 'E' to exit)10
Enter a number(or 'E' to exit)5.5
Enter a number(or 'E' to exit)E
result= 15.5
```

**Exponent**

```
enter your choice: 1
enter the number: 2
enter the power: 10
result: 1024.0
```

## Notes

- Numbers are read as decimals (floats), so results appear as `15.0` rather than `15`.
- Subtraction and division work from left to right. For example, `10, 3, 2` with `-` gives `10 - 3 - 2 = 5.0`, and `100, 5, 2` with `/` gives `100 / 5 / 2 = 10.0`.
- If any divisor (any number after the first one) is `0`, the program shows `Error: can't divide by 0.` instead of a result.
- If you type something that is not a number, the program shows `Error: Invalid input` and asks again. If you finish without entering any number, it shows `Error: no number was entered.`

## Code Overview

**`operations.py`**

- `add(number)`, `sub(number)`, `multi(number)`, `div(number)` take a list of numbers and return the result
- `power(base, exponent)` returns `base ** exponent`

**`input_handler.py`**

- `get_main_choice()` shows the main menu and returns the choice as an integer (`-1` if it is not a number)
- `get_operation_choice()` asks which operation to perform
- `get_number_list()` collects numbers until `E` or `e` is typed
- `get_exponent_inputs()` asks for the base and the power

**`main.py`**

- `run_basic_calculator()` handles option 0
- `run_exponent()` handles option 1
- `main()` runs the main menu loop

## Possible Improvements

- Add more operations (modulus, square root, percentage)
- Use exceptions for division by zero instead of returning an error message
- Add unit tests for the functions in `operations.py`
