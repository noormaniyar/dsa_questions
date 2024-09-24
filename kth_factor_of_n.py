"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list 
or return -1 if n has less than k factors.
"""

def kthFactor(n, k):
    # List to store the factors of n
    factors = []
    
    # Iterate through all numbers from 1 to n
    for i in range(1, n + 1):
        # If i is a factor of n
        if n % i == 0:
            factors.append(i)
    
    # Check if k is within the number of factors
    if len(factors) >= k:
        return factors[k - 1]  # k is 1-based index
    else:
        return -1  # If there are less than k factors

# Example usage:
print(kthFactor(12, 3))  # Output: 3
print(kthFactor(7, 2))   # Output: 7
print(kthFactor(4, 4))   # Output: -1
