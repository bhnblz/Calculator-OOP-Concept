# Create a class for command interface
class CommandInterface:
    # Ask for the operation
    def operation(self):
        operation = input("What operation do you need? [+ (addition), - (subtraction), * (multiplication), / (division)]: ")
        return operation
    # Ask for first integer
    def input_integer(self):
        integer1 = input("Enter first integer: ")
        return integer1
    # Ask for second integer
    def input_integer(self):
        integer2 = input("Enter first integer: ")
        return integer2
    
    # Print output
    def answer(self, result):
        print(result)
