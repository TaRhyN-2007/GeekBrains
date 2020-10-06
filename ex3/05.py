def sumNumbers():
    numbers = input().split()
    for num in numbers:
        if num == '0':
            return sum([int(num) for num in numbers])
    return sum([int(num) for num in numbers]) + sumNumbers()


print(sumNumbers())
