def reverse(n):
    rev = 0
    while n > 0:
        last_digit = n % 10  
        rev = rev * 10 + last_digit  
        n //= 10  # Remove the last digit from n
    return rev
print(reverse(1234))