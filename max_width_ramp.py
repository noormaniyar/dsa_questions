"""
    A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
    Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
"""

def maxWidthRamp(nums):
    stack = []
    n = len(nums)
    
    # Create a stack of indices in decreasing order of nums
    for i in range(n):
        if not stack or nums[stack[-1]] > nums[i]:
            stack.append(i)
    
    max_width = 0
    
    # Traverse from right to left
    for j in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[j]:
            max_width = max(max_width, j - stack.pop())
    
    return max_width
nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
print(maxWidthRamp(nums))