def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return a * pow(a, n - 1)
    else:
        return pow(a * a, n // 2)


print(pow(3, 4))
