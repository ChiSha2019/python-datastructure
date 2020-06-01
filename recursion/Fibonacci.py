def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_iterative(n):
    num1 = 0
    num2 = 1
    total = 0
    if n <= 1:
        return n
    for i in range(1, n):
        total = num1 + num2
        num1 = num2
        num2 = total
    return total
