def summ(n):
    if n == 0:
        return 0
    return summ(n - 1) + n

print(summ(-1))