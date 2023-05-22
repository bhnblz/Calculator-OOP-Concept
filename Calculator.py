# Create a program that will calculate using four operation such as additon, subtraction, multiplication, division
class simpleCalculator:
    def __init__(self):
        print("Welcome to this calculator")
        print("Calculator is initiated..")
     
    # If addition
    def add(self, integer1, integer2):
        result = integer1 + integer2
        return result
    # If subtraction
    def sub(self, integer1, integer2):
        result = integer1 - integer2
        return result
    # If multiplication
    def mult(self, integer1, integer2):
        result = integer1 * integer2
        return result
    # If division
    def div(self, integer1, integer2):
        result = integer1 / integer2
        return result    