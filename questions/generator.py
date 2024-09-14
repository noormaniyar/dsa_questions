"""
3. Generators:
A generator is a special type of iterator that yields values one at a time using the yield keyword instead of returning all of them at once. 
Generators are more memory-efficient than regular functions for large datasets.
"""


# Simple generator to yield square numbers
def square_numbers(n):
    for i in range(1, n+1):
        yield i * i  # Instead of return, we use yield

# Using the generator
for square in square_numbers(5):
    print(square)
