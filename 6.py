"""
The sum of the squares of the first ten natural numbers is, 385
The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares 
of the first ten natural numbers and the square of the sum is 2640
Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
"""
# Refer (a+b+c)^2 = a^2 + b^2 + c^2 + 2(ab+bc+ca)
answer = 0
i = j = 100
while i > 0:
    while j > 0:
        if i!=j:
            answer += (i*j)
            j-=1
        else:
            j-=1
    i-=1
    j = 100
print(f'Answer is {answer}')
        