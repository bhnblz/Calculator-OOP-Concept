# Create a class for command interface
class CommandInterface:
    # Ask for the operation
    def operation(self):
        operation = input("\nWhat operation do you need? [+ (addition), - (subtraction), * (multiplication), / (division)]: ")
        return operation
    # Ask for first integer
    def input_integer(self):
        integer1 = float(input("Enter first integer: \n"))
        return integer1
    # Ask for second integer
    def input_integer(self):
        integer2 = float(input("\nEnter first integer: "))
        return integer2
    
    # If ValueError
    def invalid_input(self):
        print("\nERROR: Invalid input!")
    # If ZeroDivisionError
    def zeroDivisionError(self):
        print("\nERROR: Cannot divide by zero")
    # If invalid operation
    def invalid_op(self):
        print("\nERROR: Invalid operation!")
    # Print output
    def answer(self, result):
        print("\nAnswer: " + str(result))
    # Ask user if they want to solve again
    def solve_again(self):
        try_again = input("\nDo you want to solve another function? (y/n): ")
        if try_again == "y":
            return True
        elif try_again == "n":
            print("\nThank you!")
            exit()