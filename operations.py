# operations.py
# All the calculation functions of the calculator live here.


def add(number):
    return sum(number)


def sub(number):
    if not number:
        return 0
    result = number[0]
    for num in number[1:]:
        result -= num
    return result


def multi(number):
    if not number:
        return 0
    result = 1
    for num in number:
        result *= num
    return result


def div(number):
    if not number:
        return 0
    result = number[0]
    for num in number[1:]:
        if num == 0:
            return "Error: can't divide by 0."
        result /= num
    return result


def power(base, exponent):
    return base ** exponent
