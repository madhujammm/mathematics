def divisors1(n, i=1, divs=None):
    if divs is None:
        divs = []
    if i > n:
        return divs
    if n % i == 0:
        divs.append(i)
    return divisors1(n, i + 1, divs)

#non recursive
def divisors2(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)
