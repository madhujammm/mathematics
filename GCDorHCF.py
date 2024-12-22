#recursive
def gcdrecursive(a, b):
    if b == 0:
        return a
    return gcdrecursive(b, a % b)

#non recursive
def gcdnon_recursive(a, b):
    while b != 0:
        a, b = b, a % b
    return a

