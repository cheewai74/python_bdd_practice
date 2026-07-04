class Calculator(object):

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))        # Output: 8
    print(calc.subtract(5, 3))   # Output: 2
    print(calc.multiply(5, 3))   # Output: 15
    print(calc.divide(5, 0))     # Raises ValueError: Cannot divide by zero     