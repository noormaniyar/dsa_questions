"""
    There are n balls on a table, each ball has a color black or white.
    You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
    In each step, you can choose two adjacent balls and swap them.
    Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
"""

class Solution(object):
    def minimumSteps(self, s):
        white_count = 0
        swap_count = 0
        
        # Iterate through the string to count swaps
        for ch in s:
            if ch == '1':
                white_count += 1
            elif ch == '0':
                swap_count += white_count  # Every '1' needs to pass all the '0's before it
        
        return swap_count


sol = Solution()
print(sol.minimumSteps("010101"))  # Output: 6
print(sol.minimumSteps("100"))   # Output: 0
print(sol.minimumSteps("101010"))  # Output: 9
