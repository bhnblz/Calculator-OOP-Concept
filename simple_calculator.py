from command_interface import CommandInterface
from Calculator import simpleCalculator

ci = CommandInterface()
calc = simpleCalculator()

def evaluate():
    operation = ci.operation()

    integer1 = ci.input_integer()
    integer2 = ci.input_integer()

    if operation == "+":
        result = calc.add(integer1, integer2)
    elif operation == "-":
        result = calc.sub(integer1, integer2)
    elif operation == "*":
        result = calc.mult(integer1, integer2)
    elif operation == "/":
        result = calc.div(integer1, integer2)

    ci.answer(result)
evaluate()