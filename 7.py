"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import math
def isprime(n):
    if n<=3:
        return n > 1
    if n%2==0 or n%3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i+=6
    return True

count = 1
i = 1
while count != 10001:
    if isprime(i):
        current = i
        i+=1
        count+=1
    i+=1
print(current)