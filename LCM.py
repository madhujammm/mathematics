#recursive
def lcm2(a, b):
    def gcd(a, b):  
        if b == 0:
            return a
        return gcd(b, a % b)
    return abs(a * b) // gcd(a, b)


#non recursive
def lcm1(a, b):
    def gcd(a, b):  # Helper non-recursive function for GCD
        while b != 0:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)
