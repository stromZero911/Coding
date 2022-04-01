"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?
"""
# The value is simply the LCM numeber from 1 to 20

import math
def isprime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def get_lcm(nums:list=[]):
    val = 1
    n = 1
    while n < max(nums):
        if isprime(n):
            occur = 1
            after = 0
            for j in nums:
                while j%n == 0:
                    j/=n
                    after+=1
                if after > occur:
                    occur = after
                after = 0
            print(f'{n} occurs max of {occur}')
            val *= (n**occur)
        n+=1
    print('LCM of the given numbers is',val)    
    return val
get_lcm(range(1,21))