"""
    Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of 
    different non-empty subsets with the maximum bitwise OR.
    An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. 
    Two subsets are considered different if the indices of the elements chosen are different.
    The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
"""

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num

        count = 0
        n = len(nums)
        for i in range(1, 1 << n):
            current_or = 0
            for j in range(n):
                if i & (1 << j):
                    current_or |= nums[j]
            if current_or == max_or:
                count += 1
        return count


obj = Solution()
# nums = [3, 1]
nums = [2, 2, 2]
print(obj.countMaxOrSubsets(nums))