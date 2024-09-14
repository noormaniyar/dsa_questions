# A generator that generates a range of numbers
def number_gen(n):
    for i in range(1, n+1):
        yield i

# A decorator to log the numbers being generated
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Generating numbers up to {args[0]}:")
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator to the generator function
@log_decorator
def number_gen_decorated(n):
    for i in range(1, n+1):
        yield i

# Using the decorated generator
for number in number_gen_decorated(5):
    print(number)
