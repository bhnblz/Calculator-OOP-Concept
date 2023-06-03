from Calculator import simpleCalculator
# Child class
class BheaCalculator(simpleCalculator):
    # If integer1(base) is raised to integer2(exponent)
    def power(self, base, exponent):
        result = base ** exponent
        return result 
    # Getting the remainder
    def modulus(self, integer1, integer2):
        result = integer1 % integer2
        return result