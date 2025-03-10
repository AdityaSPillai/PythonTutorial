lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

SumOfOdd = 0

for num in range(lower, upper + 1):
    if num % 2 != 0:
        SumOfOdd += num

print(f"Sum of odd numbers between {lower} and {upper} is {SumOfOdd}")