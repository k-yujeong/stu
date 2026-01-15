# 소수 찾기
import math

prime_count = 0

N = int(input()) 

numbers = list(map(int, input().split()))

for num in numbers:
    if num < 2: 
        is_prime = False
    elif num == 2: 
        is_prime = True
    else:
        is_prime = True 
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break 
    
    if is_prime:
        prime_count += 1

print(prime_count)