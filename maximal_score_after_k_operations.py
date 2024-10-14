"""
    You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
    In one operation:
    choose an index i such that 0 <= i < nums.length,
    increase your score by nums[i], and
    replace nums[i] with ceil(nums[i] / 3).
    Return the maximum possible score you can attain after applying exactly k operations.
    The ceiling function ceil(val) is the least integer greater than or equal to val.
"""
import heapq
import math

class Solution(object):
    def maxKelements(self, nums, k):
        # Convert nums to a max-heap by negating the values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        # Perform k operations
        for _ in range(k):
            # Extract the largest element
            largest = -heapq.heappop(max_heap)
            score += largest
            
            # Replace the largest number with ceil(largest / 3)
            new_val = math.ceil(largest / 3)
            
            # Manual ceiling for division by 3
            # new_val = (largest + 2) // 3  # This avoids floating-point operations
            
            # Push the new value into the heap
            heapq.heappush(max_heap, -new_val)
        
        return score


nums = [1,10,3,3,3]
k = 3
obj  = Solution()
a = obj.maxKelements(nums, k)
print(a)