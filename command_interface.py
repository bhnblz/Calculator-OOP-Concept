import pyfiglet
from colorama import Fore

# Create a class for command interface
class CommandInterface:
    # Ask for the operation
    def operation(self):
        operation = input(Fore.LIGHTCYAN_EX + "\nWhat operation do you need? [+ (addition), - (subtraction), * (multiplication), / (division), ** (power), % (modulus)]: ")
        return operation
    # Ask for first integer
    def input_integer(self):
        integer1 = float(input(Fore.LIGHTMAGENTA_EX + "Enter first integer: \n"))
        return integer1
    # Ask for second integer
    def input_integer(self):
        integer2 = float(input(Fore.LIGHTMAGENTA_EX + "\nEnter first integer: "))
        return integer2
    
    # If ValueError
    def invalid_input(self):
        print(Fore.LIGHTRED_EX + "\nERROR: Invalid input!")
    # If ZeroDivisionError
    def zeroDivisionError(self):
        print(Fore.LIGHTRED_EX + "\nERROR: Cannot divide by zero")
    # If invalid operation
    def invalid_op(self):
        print(Fore.LIGHTRED_EX + "\nERROR: Invalid operation!")
    # Print output
    def answer(self, result):
        print(Fore.LIGHTBLUE_EX + "\nAnswer: " + str(result))
    # Ask user if they want to solve again
    def solve_again(self):
        try_again = input(Fore.GREEN + "\nDo you want to solve another function? (y/n): ")
        if try_again == "y":
            return True
        elif try_again == "n":
            closing_remark = "\nThank you!"
            print(pyfiglet.figlet_format (closing_remark.center(90), font = "standard"))
            exit()