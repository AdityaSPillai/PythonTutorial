def IsPrime(n):
    if n <= 1:
        return False 
    
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  
    
    return True  

num = int(input("Enter a number: "))

if IsPrime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")