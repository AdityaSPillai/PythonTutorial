import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

disc = b**2 - 4*a*c

if disc > 0:
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)
    print(f"Two real and distinct roots: {root1:.2f}, {root2:.2f}")

elif disc == 0:
    root = -b / (2 * a)
    print(f"One real and equal root: {root:.2f}")

else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(disc)) / (2 * a)
    print(f"Two complex roots: {real_part:.2f} ± {imag_part:.2f}i")