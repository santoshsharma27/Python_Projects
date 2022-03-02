# self keywod is mandatory for calling variable names into methods
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required when we create object in python



class Calculator:
    num = 100

    # Default Constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # Syntax to create object in python
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())
