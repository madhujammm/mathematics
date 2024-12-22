def power1(x, y):
    if y == 0:
        return 1
    half = power1(x, y // 2)
    if y % 2 == 0:
        return half * half
    return half * half * x

#non recursive
def power2(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        x *= x
        y //= 2
    return result
