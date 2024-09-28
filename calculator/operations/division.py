# calculator/operations/division.py

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return self.a / self.b