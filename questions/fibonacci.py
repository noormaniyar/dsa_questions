"""

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test the examples
example_1 = fibonacci(2)  # Expected output: 1
example_2 = fibonacci(3)  # Expected output: 2
example_3 = fibonacci(4)  # Expected output: 3

example_1, example_2, example_3

print(example_1, example_2, example_3)
