"""
2. Iterators:
An iterator is an object in Python that allows us to traverse through all the elements in a 
collection (like a list or tuple) one by one. Iterators implement the __iter__() and __next__() methods.
"""


# Define a custom iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        if x > 5:  # Let's stop iteration after 5
            raise StopIteration
        self.a += 1
        return x

# Create an iterator object
my_iter = iter(MyNumbers())

# Iterate through the numbers
for num in my_iter:
    print(num)
