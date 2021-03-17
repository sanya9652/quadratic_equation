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
            savings = reshen.Square(a, b, c)    #We get the values of the coefficients from the user and pass them to __init__
            savings.discrim()   #Calculate the discriminant
            print(savings)      #The value of the discriminant is displayed
            savings.resh()      #Calculating the roots
            print()
        except ValueError:
            print("You entered an invalid value")

main()
