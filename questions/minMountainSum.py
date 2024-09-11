"""

You are given a 0-indexed array nums of integers.

A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]
Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.

"""


def minMountainSum(nums):
    n = len(nums)
    if n < 3:
        return -1
    
    # Step 1: Compute left_min and right_min arrays
    left_min = [float('inf')] * n
    right_min = [float('inf')] * n
    
    # Fill left_min
    current_min = float('inf')
    for i in range(1, n):
        current_min = min(current_min, nums[i - 1])
        left_min[i] = current_min
    
    # Fill right_min
    current_min = float('inf')
    for i in range(n - 2, -1, -1):
        current_min = min(current_min, nums[i + 1])
        right_min[i] = current_min
    
    # Step 2: Find the minimum mountain sum
    min_sum = float('inf')
    found = False
    for j in range(1, n - 1):
        if nums[j] > left_min[j] and nums[j] > right_min[j]:
            current_sum = nums[j] + left_min[j] + right_min[j]
            min_sum = min(min_sum, current_sum)
            found = True
    print(min_sum, '================================================min_sum====================================')
    return min_sum if found else -1


nums = [5,4,8,7,10,2]
# nums = [8,6,1,5,3]
# nums = [6,5,4,3,4,5]


minMountainSum(nums)