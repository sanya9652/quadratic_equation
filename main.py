import reshen

def main():
    print('''This program calculates the roots of a quadratic equation,
          \t\t enter 0 for quit.
          \n The quadratic equation has the form ax^2 + bx + c, input,
          these coefficients, taking into account the sign''')
    a = b = c = 1
    while a != 0 or b != 0 or c != 0:
        try:
            a = int(input("a: "))
            b = int(input("b: "))
            c = int(input("c: "))
            savings = reshen.Square(a, b, c)    #Получаем от пользователя значения коэффициентов и передаем их в __init__
            savings.discrim()   #Вычисляем дискриминант
            print(savings)      #Выводим значение дискриминанта
            savings.resh()      #Вычисляем корни
            print()
        except ValueError:
            print("Вы ввели некорректное значение")

main()
