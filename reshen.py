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
                print("Нет корней")
            elif self.discr == 0:
                x = (- self.b - math.sqrt(self.discr))/(2 * self.a)
                print("В уравнении один корень" + '\n' + "x = " + str(format(x, '.2f')))
            else:
                x1 = (- self.b - math.sqrt(self.discr))/(2 * self.a)
                x2 = (- self.b + math.sqrt(self.discr))/(2 * self.a)
                print("В уравнении два корня:" + "\n" + "x1 =" + str(format(x1, '.2f')) + "\n" + "x2 =" + str(format(x2, '.2f')))
        except ZeroDivisionError:
            print("В процессе решения произошло деление на ноль")

    def __str__(self):
        return 'Дискриминант равен ' + format(self.discr, '.2f')

if __name__ == '__main__':
    print('Список методов класса:\n__init__(self, a, b, c)\ndiscrim(self)\nresh(self)')
