# Import CommandInterface
from command_interface import CommandInterface
# Import simpleCalculator
from Calculator import simpleCalculator

# Create objects
ci = CommandInterface()
calc = simpleCalculator()

def evaluate():
    operation = ci.operation()
    try: 
        integer1 = ci.input_integer()
        integer2 = ci.input_integer()
    except ValueError:
        print(ci.invalid_input())
        return evaluate() 

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
            return evaluate()
    else: 
        print(ci.invalid_op())
        return evaluate()
    # Print the result
    ci.answer(result)
    # ASk user if want to solve again, if not then exit the program
    if ci.solve_again() == True:
        evaluate()
# Call the function
evaluate()