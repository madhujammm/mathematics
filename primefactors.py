def prime_factors_recursive(n, i=2):
    if n <= 1:
        return []
    if n % i == 0:
        return [i] + prime_factors_recursive(n // i, i)
    return prime_factors_recursive(n, i + 1)


#non recursive
def prime_factors_non_recursive(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors
