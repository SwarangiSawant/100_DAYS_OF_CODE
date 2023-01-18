from replit import clear
from ART import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": division}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    to_do = "True"
    while to_do:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        check = input(
            f"Type 'y' to continue calculating with {answer}, or tyoe 'n' to exit: "
        )
        if check == "y":
            num1 = answer
        else:
            to_do = False
            clear()
            calculator()


calculator()
