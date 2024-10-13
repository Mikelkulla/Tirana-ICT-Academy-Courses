"""
Write a  Python program to create a  calculator class. Include methods for basic arithmetic operations.
"""
class Calculator:
    # Takes 2 arguments and return the sum
    def add(self, x, y):
        return x + y
    # Takes 2 arguments and return the substraction
    def substract(self, x, y):
        return x - y
    # Takes 2 arguments and return the multiplication
    def multiply(self, x, y):
        return x * y
    # Takes 2 arguemtns and return the devision
    def devide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            print("Error, zerodivision error!")
        except BaseException:
            print("Error!")

cl1 = Calculator()
x = float(input("Enter X: "))
y = float(input("Enter Y: "))

print("Sum:",cl1.add(x,y))
print("Substraction:",cl1.substract(x,y))
print("Multiplication:",cl1.multiply(x,y))
print("Devision:",cl1.devide(x,y))