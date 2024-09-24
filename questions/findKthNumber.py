"""
    Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
"""
def findKthNumber(n: int, k: int) -> int:
    def count_steps(curr, n):
        steps = 0
        first, last = curr, curr
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    curr = 1
    k -= 1  # Since we start from 1, so we need to find the (k-1)-th step.
    
    while k > 0:
        steps = count_steps(curr, n)
        if steps <= k:
            # Move to the next number on the same level
            curr += 1
            k -= steps
        else:
            # Move to the next level (deeper in the tree)
            curr *= 10
            k -= 1

    return curr
