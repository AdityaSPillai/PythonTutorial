def SumAndAverage(numbers):
    PositiveSum = 0  
    NegativeSum = 0  
    PositiveCount = 0  
    NegativeCount = 0 

    for num in numbers:
        if num > 0:
            PositiveSum += num
            PositiveCount += 1
        elif num < 0:
            NegativeSum += num
            NegativeCount += 1
   
    pos_avg = PositiveSum / PositiveCount if PositiveCount > 0 else 0
    neg_avg = NegativeSum / NegativeCount if NegativeCount > 0 else 0

    return PositiveSum, pos_avg, NegativeSum, neg_avg

nums = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

PositiveSum, pos_avg, NegativeSum, neg_avg = SumAndAverage(nums)

print(f"Sum of positive numbers: {PositiveSum}")
print(f"Average of positive numbers: {pos_avg:.2f}")
print(f"Sum of negative numbers: {NegativeSum}")
print(f"Average of negative numbers: {neg_avg:.2f}")