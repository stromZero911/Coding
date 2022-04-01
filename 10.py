"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million = 20,00,000
"""
import math

def isprime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i+=6
    return True

def getSum(n):
    val = 0
    count = 0
    while count < n:
        count+=1
        if isprime(count):
            val+=count
    print(val-n)

getSum(11)
getSum(23)
getSum(20)