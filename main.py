# COMPLEX CALCULATOR
# Run this file to start the program:  python main.py

from operations import add, sub, multi, div, power
from input_handler import (
    get_main_choice,
    get_operation_choice,
    get_number_list,
    get_exponent_inputs,
)


def run_basic_calculator():
    """Add / subtract / multiply / divide a list of numbers."""
    while True:
        choice = get_operation_choice()

        if choice == 'q':
            print("Thank You!")
            break
        if choice not in ['+', '-', '/', '*', 'q']:
            print("invalid input")
            continue

        number_list = get_number_list()
        if not number_list:
            print("Error: no number was entered.")
            continue

        if choice == '+':
            print("result=", add(number_list))
        elif choice == '-':
            print("result=", sub(number_list))
        elif choice == '*':
            print("result=", multi(number_list))
        elif choice == '/':
            print("result=", div(number_list))


def run_exponent():
    """Raise a number to a power."""
    try:
        base, exponent = get_exponent_inputs()
        print("result:", power(base, exponent))
    except ValueError:
        print("Error: Please enter valid number")


def main():
    while True:
        op = get_main_choice()

        if op == 0:
            run_basic_calculator()
        elif op == 1:
            run_exponent()
        elif op == 2:
            print("THANKS!")
            break  # stop the program
        else:
            print("Invalid input,Please enter valid input")


if __name__ == "__main__":
    main()
