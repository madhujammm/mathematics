def palin(n):
    original = n
    rev = 0
    while n > 0:
        last_digit = n % 10  # Extracting last digit
        rev = rev * 10 + last_digit  # Append.last digit to rev
        n //= 10  # Remove the last digit from n
    return original == rev  
print(palin(1221))