"""
    Design a stack that supports increment operations on its elements.
    Implement the CustomStack class:
    CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
    void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
    int pop() Pops and returns the top of the stack or -1 if the stack is empty.
    void inc(int k, int val) Increments the bottom k elements of the stack by val. 
    If there are less than k elements in the stack, increment all the elements in the stack.
"""
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.maxSize = maxSize
        self.increment_arr = [0] * maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        
        idx = len(self.stack) - 1
        increment_value = self.increment_arr[idx]
        
        value = self.stack.pop() + increment_value
        
        if idx > 0:
            self.increment_arr[idx - 1] += self.increment_arr[idx]
        
        self.increment_arr[idx] = 0
        
        return value

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.increment_arr[idx] += val


# Your CustomStack object will be instantiated and called as such:
maxSize = 3
x = 1
k = 2
val = 100

obj = CustomStack(maxSize)
print(obj, '--------------------obj------------')
px = obj.push(x)
print(px, '----------------------px--------------')
param_2 = obj.pop()
print(param_2, '----------------------param_2---------------------')
oi = obj.increment(k,val)
print(oi, '----------------------------oi---------------')
