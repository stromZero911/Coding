"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
i = 1
j = 2
k = 3 
while i < 1000:
    j = 2
    if(i+j<1000):
        while j < 1000:
            k = 3
            if(j+k<1000):
                while k < 1000:
                    if (i+j+k == 1000):
                        print(i,j,k)
                        if (i**2 + j**2 == k**2):
                            print(i*j*k,i,j,k)
                            i = j = k = 1001
                    k+=1
            j+=1
    i+=1
