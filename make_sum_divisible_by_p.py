"""
    Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that 
    the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
    Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
    A subarray is defined as a contiguous block of elements in the array.

"""

def minSubarray(nums, p):
    total_sum = sum(nums)
    target_remainder = total_sum % p
    
    # If the total sum is already divisible by p, return 0
    if target_remainder == 0:
        return 0
    
    # Dictionary to store the index where a particular mod value is seen
    prefix_mod = {0: -1}
    current_sum = 0
    min_len = len(nums)
    
    for i, num in enumerate(nums):
        current_sum += num
        current_mod = current_sum % p
        
        # We need to find (current_mod - target_remainder) % p in the prefix_mod map
        desired_mod = (current_mod - target_remainder) % p
        
        if desired_mod in prefix_mod:
            # The length of the subarray we can remove
            min_len = min(min_len, i - prefix_mod[desired_mod])
        
        # Update the prefix_mod with the current_mod
        prefix_mod[current_mod] = i
    
    return min_len if min_len < len(nums) else -1

nums = [3, 1, 4, 2]
p = 6
print(minSubarray(nums, p))