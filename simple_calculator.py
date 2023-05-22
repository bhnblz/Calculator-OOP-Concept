from command_interface import CommandInterface
from Calculator import simpleCalculator

ci = CommandInterface()
calc = simpleCalculator()

def evaluate():
    operation = ci.operation()

    integer1 = ci.input_integer()
    integer2 = ci.input_integer()

    if operation == "+":
        result = integer1 + integer2
        print(result)
    elif operation == "-":
        result = integer1 - integer2
        print(result)
    elif operation == "*":
        result = integer1 * integer2
        print(result)
    elif operation == "/":
        result = integer1 / integer2
        print(result)

    ci.answer(result)
evaluate()