from command_interface import CommandInterface
from Calculator import simpleCalculator

ci = CommandInterface()
calc = simpleCalculator()

def evaluate():
    operation = ci.operation()
    
    try: 
        integer1 = ci.input_integer()
        integer2 = ci.input_integer()
    except ValueError:
        print(ci.invalid_input())
        return

    if operation == "+":
        result = calc.add(integer1, integer2)
    elif operation == "-":
        result = calc.sub(integer1, integer2)
    elif operation == "*":
        result = calc.mult(integer1, integer2)
    elif operation == "/":
        try:
            result = calc.div(integer1, integer2)
        except ZeroDivisionError:
            print(ci.zeroDivisionError())
            return
    else: 
        print(ci.invalid_op())

    ci.answer(result)

    if ci.solve_again == True:
        evaluate()

evaluate()