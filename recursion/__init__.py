def summation(n):
    if n >= 1:
        return summation(n - 1) + n
    return n


def summation_loop(n):
    total = 1  # basecase
    for x in range(2, n+1):
        total += x
    return total


print(summation_loop(5))
