# input_handler.py
# Everything that asks the user for input (menus, operator, numbers).


def get_main_choice():
    """Show the main menu and return the choice as an int (-1 if invalid)."""
    print("------WELCOME------")
    print("To add,substract, multiply and divide--Enter: 0")
    print("For exponential-- Enter: 1")
    print("To exit-- Enter 2")

    try:
        return int(input("enter your choice: "))
    except ValueError:
        return -1


def get_operation_choice():
    """Show the operations menu and return what the user typed."""
    print("operations: add[+] substract[-] multiply[*]  divide[/] quit[q]")
    return input("enter your choice: ")


def get_number_list():
    """Keep asking for numbers until the user types 'E' or 'e'."""
    number_list = []
    print("enter number one by one")
    print("type 'E' or 'e' to exit the calculator")

    while True:
        user_input = input("Enter a number(or 'E' to exit)")
        if user_input == 'E' or user_input == 'e':
            break
        try:
            num = float(user_input)
            number_list.append(num)
        except ValueError:
            print("Error: Invalid input")

    return number_list


def get_exponent_inputs():
    """Ask for the number and the power (raises ValueError if not numbers)."""
    base = float(input("enter the number: "))
    exponent = float(input("enter the power: "))
    return base, exponent
