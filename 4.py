"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def reverse(n):
    rev = 0
    while n != 0:
        rev *= 10
        rev += (n%10)
        n //= 10
    return rev

def check(n):
    if n == reverse(n):
        return True
    else:
        return False

# Using the Lychrel Process
i = 999
j = 999
max = 0
while i >= 100:
    while j >= 100:
        if check(i*j):
            if((i*j)>max):
                max = i*j
                val_i = i
                val_j = j
            j = 999
            i-=1
        else:
            j-=1
    j = 999
    i-=1
print(f'Maximum value is {max} which is product of {val_i} and {val_j}')