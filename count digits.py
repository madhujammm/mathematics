import math
def count(n):
    cnt = 0
    while n > 0:
        n //= 10  # Floor divide {divides two numbers and rounds down to the nearest integer} to remove the last digit
        cnt += 1  
    return cnt
print(count(1002))

#using log
def count2(n):
    cnt = 0
    cnt = (int)(math.log10(n)+1)
    return cnt
print(count2(1221))

    