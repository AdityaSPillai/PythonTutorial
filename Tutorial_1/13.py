def ReverseNumber(n):
    ReveresedNumber = 0
    
    while n > 0:
        digit = n % 10 
        ReveresedNumber = ReveresedNumber * 10 + digit  
        n //= 10
    
    return ReveresedNumber

num = int(input("Enter a number: "))

if num < 0:
    print(f"Reversed number: -{ReverseNumber(abs(num))}")
else:
    print(f"Reversed number: {ReverseNumber(num)}")