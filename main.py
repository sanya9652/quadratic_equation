import reshen

def main():
    print("Данная программа вычисляет корни квадратного уравнения,")
    print("\t", "для завершения введите 0")
    print("Квадратное уравнение имеет вид ax^2 + bx + c, введите" + '\n' + '\t' + "эти коэффициенты с учетом знака")
    a = b = c = 1
    while a != 0 or b != 0 or c != None:
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
