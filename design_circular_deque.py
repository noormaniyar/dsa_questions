"""
    Design your implementation of the circular double-ended queue (deque).

    Implement the MyCircularDeque class:

    MyCircularDeque(int k) Initializes the deque with a maximum size of k.
    boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
    int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
    int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
    boolean isEmpty() Returns true if the deque is empty, or false otherwise.
    boolean isFull() Returns true if the deque is full, or false otherwise.

"""
class MyCircularDeque:
    
    def __init__(self, k):
        """Initialize the deque with a maximum size of k."""
        self.k = k
        self.deque = [0] * k  # Fixed-size array for circular deque
        self.front = 0  # Front pointer
        self.rear = 0  # Rear pointer
        self.size = 0  # Current size of the deque

    def insertFront(self, value):
        """Adds an item at the front of deque. Returns true if successful, false otherwise."""
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k  # Move front pointer back
        self.deque[self.front] = value  # Insert at the front
        self.size += 1
        return True

    def insertLast(self, value):
        """Adds an item at the rear of deque. Returns true if successful, false otherwise."""
        if self.isFull():
            return False
        self.deque[self.rear] = value  # Insert at the rear
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward
        self.size += 1
        return True

    def deleteFront(self):
        """Deletes an item from the front of deque. Returns true if successful, false otherwise."""
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self):
        """Deletes an item from the rear of deque. Returns true if successful, false otherwise."""
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k  # Move rear pointer back
        self.size -= 1
        return True

    def getFront(self):
        """Returns the front item from the deque. Returns -1 if the deque is empty."""
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """Returns the last item from the deque. Returns -1 if the deque is empty."""
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.k]

    def isEmpty(self):
        """Returns true if the deque is empty, false otherwise."""
        return self.size == 0

    def isFull(self):
        """Returns true if the deque is full, false otherwise."""
        return self.size == self.k

# Your MyCircularDeque object will be instantiated and called as such:
k = 5
value = 10

obj = MyCircularDeque(k)
print(obj, '---------------obj-----------')
param_1 = obj.insertFront(value)
print(param_1, '-------------param_1------------')
param_2 = obj.insertLast(value)
print(param_1, '-------------param_2------------')
param_3 = obj.deleteFront()
print(param_1, '-------------param_3------------')
param_4 = obj.deleteLast()
print(param_1, '-------------param_4------------')
param_5 = obj.getFront()
print(param_1, '-------------param_5------------')
param_6 = obj.getRear()
print(param_1, '-------------param_6------------')
param_7 = obj.isEmpty()
print(param_1, '-------------param_7------------')
param_8 = obj.isFull()
print(param_1, '-------------param_8------------')