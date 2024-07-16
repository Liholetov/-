import math

# Если известны только катеты
adjacent_catheter = input("Введите длину прилежащего катета: ")
adjacent_catheter = int(adjacent_catheter)

opposite_catheter = input("Введите длину противолежащего катета: ")
opposite_catheter =int(opposite_catheter)

Pythagorean_Theorem = adjacent_catheter**2 + opposite_catheter**2
Pythagorean_Theorem = math.sqrt(Pythagorean_Theorem)
Pythagorean_Theorem = round(Pythagorean_Theorem, 2)

print(f"Pythagorean_Theorem = {Pythagorean_Theorem}")

# Если известны только катет и гипотенуза

catheter = input("Введите длину катета: ")
catheter = int(catheter)
hypotenuse = input("Введите длину гипотенузы: ")
hypotenuse = int(hypotenuse)

if catheter < hypotenuse:
    alternative_Pythagorean_Theorem = hypotenuse**2 - catheter**2
    alternative_Pythagorean_Theorem = math.sqrt(alternative_Pythagorean_Theorem)
    alternative_Pythagorean_Theorem = round(alternative_Pythagorean_Theorem, 2)
    print(f"alternative_Pythagorean_Theorem = {alternative_Pythagorean_Theorem}")
else:
    print("В прямоугольном треугольнике гипотенуза не может быть меньше катета или ему равна")

