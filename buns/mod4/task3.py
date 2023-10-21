def euclid(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return euclid(b, a % b)


print(euclid(10, 15))
