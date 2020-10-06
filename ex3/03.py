def sum_max (a, b ,c):
    minimal = min(a, b, c)
    sum_all = a + b + c
    return sum_all - minimal


print(sum_max(1, 2, 3))
