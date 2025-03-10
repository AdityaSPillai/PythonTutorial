n = int(input("Enter the number of elements: "))

EvenCount = 0
OddCount = 0

for _ in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        EvenCount += 1
    else:
        OddCount += 1

print(f"Even numbers: {EvenCount}")
print(f"Odd numbers: {OddCount}")