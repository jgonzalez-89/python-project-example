# calculator/calculator.py

from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division
from utils.logger import Logger

class Calculator:
    def __init__(self):
        self.logger = Logger()

    def add(self, a, b):
        operation = Addition(a, b)
        return operation.execute()

    def subtract(self, a, b):
        operation = Subtraction(a, b)
        return operation.execute()

    def multiply(self, a, b):
        operation = Multiplication(a, b)
        return operation.execute()

    def divide(self, a, b):
        operation = Division(a, b)
        return operation.execute()