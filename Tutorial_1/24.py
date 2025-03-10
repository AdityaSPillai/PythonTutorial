for num in range(100, 1001):
    sod = 0
    n = num
    
    while n > 0:
        sod += n % 10
        n //= 10

    if sod % 9 == 0:
        print(num, end=" ")