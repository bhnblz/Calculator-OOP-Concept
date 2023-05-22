# Create a class for command interface
class CommandInterface:
    # Ask for the operation
    def operation(self):
        operation = input("What operation do you need? [+ (addition), - (subtraction), * (multiplication), / (division)]: ")
        return operation
    # Ask for first integer
    # Ask for second integer