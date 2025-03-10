def IsArmstrong(num):
    temp = num
    digits = 0
    sop = 0
    
    n = num
    while n > 0:
        n //= 10
        digits += 1

    n = temp
    while n > 0:
        digit = n % 10
        sop += digit ** digits
        n //= 10

    return temp == sop

num = int(input("Enter a number: "))

if IsArmstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")