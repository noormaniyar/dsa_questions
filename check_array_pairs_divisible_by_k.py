"""
    Given an array of integers arr of even length n and an integer k.
    We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
    Return true If you can find a way to do that or false otherwise.
"""

from collections import Counter

def canArrange(arr, k):
    remainder_count = Counter(x % k for x in arr)
    for r in range(k):
        if r == 0:
            if remainder_count[r] % 2 != 0:
                return False
        else:
            if remainder_count[r] != remainder_count[k - r]:
                return False
    return True

arr = [9, 7, 5, 3]
k = 6
print(canArrange(arr, k))
