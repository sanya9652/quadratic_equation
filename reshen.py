import math

class Square:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discrim(self):
        self.discr = self.b ** 2 - 4 * self.a * self.c

    def resh(self):
        try:
            if self.discr < 0:
                print("There are no roots in the equation.")
            elif self.discr == 0:
                self.x = (- self.b - math.sqrt(self.discr))/(2 * self.a)
                print(f'''Equation has one root:
x = {"%.2f" %self.x}''')
            else:
                self.x1 = (- self.b - math.sqrt(self.discr))/(2 * self.a)
                self.x2 = (- self.b + math.sqrt(self.discr))/(2 * self.a)
                print(f'''The equation has two roots:
x1 = {"%.2f" %self.x1}
x2 = {"%.2f" %self.x2}''')
        except ZeroDivisionError:
            print("Division by zero occurred in the process of solving")

    def __str__(self):
        return f'The discriminant is equal to {"%.2f" %self.discr}'
