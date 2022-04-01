"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
res = 0 # Set initial result to 0
for i in range(1,1000): # Consider each number from 1 to 999
    if i%3 == 0 or i%5 == 0: # Check if the number is divisible by 3 or 5
        res+=i # If the number is divisible, add it to the result
print(res) # After loop has ended print value of sum