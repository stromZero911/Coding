"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math
def maxPrimeFactor(n):
    maxPrime = -1
    while n%2 == 0:
        maxPrime=2
        n/=2
    for i in range(3,int(math.sqrt(n)),2):
        while n%i == 0:
            maxPrime = i
            n = n/i
        
    if n > 2:
        maxPrime=n
    
    return int(maxPrime)

print(maxPrimeFactor(600851475143))