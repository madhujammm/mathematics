def trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
'''
Trailing zeros are determined by the number of times n! is divisible by powers of 5
Recursive implementation is unnecessary here because the calculation is iterative
'''
