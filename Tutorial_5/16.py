import numpy as np

a = np.random.randint(0, 21, (3, 3))
b = np.random.randint(0, 21, (3, 3))

sum = a + b
dot = np.dot(a, b)
t = dot.T

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)
print("\nMatrix Addition (A + B):\n", sum)
print("\nMatrix Multiplication (A * B):\n", dot)
print("\nTransposed Product Matrix:\n", t)