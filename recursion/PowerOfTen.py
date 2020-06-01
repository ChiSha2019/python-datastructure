def powerOf10(n):
    if n == 0:
        return 1
    return powerOf10(n - 1) * 10


def powerOf10Iterative(n):
    total = 1
    for index in range(2, n + 1):
        total = total * 10
    return total
