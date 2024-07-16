import math

def diskriminant():

    a = input("Введите число a: ")
    a = int(a)

    b = input("Введите число b: ")
    b = int(b)

    c = input("Введите число c: ")
    c = int(c)

    Dis_1 = b**2
    Dis_2 = 4*a*c
    Dis = Dis_1 - Dis_2
    Dis = math.sqrt(Dis)
    print(f"дискриминант = {Dis}")
    x1_numerator = -b + Dis
    x1_denominator = a * 2
    x1 = x1_numerator / x1_denominator


    x2_numerator = -b - Dis
    x2_denomirator = a * 2
    x2 = x2_numerator / x2_denomirator

    print(f" x1 = {x1} x2 = {x2}")


diskriminant()