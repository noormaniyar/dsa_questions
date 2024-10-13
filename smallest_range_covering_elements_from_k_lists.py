"""
    You have k lists of sorted integers in non-decreasing order. 
    Find the smallest range that includes at least one number from each of the k lists.
    We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
"""

import heapq

def smallestRange(nums):
    # Min-heap to store the tuple (value, list_index, element_index)
    min_heap = []
    max_value = float('-inf')
    
    # Initialize the heap with the first element from each list
    for i in range(len(nums)):
        heapq.heappush(min_heap, (nums[i][0], i, 0))
        max_value = max(max_value, nums[i][0])
    
    # Initialize the best range
    best_range = [-float('inf'), float('inf')]
    
    while min_heap:
        min_value, list_idx, element_idx = heapq.heappop(min_heap)
        
        # If this range is smaller, update the best range
        if max_value - min_value < best_range[1] - best_range[0]:
            best_range = [min_value, max_value]
        
        # If there are more elements in the list, add the next element to the heap
        if element_idx + 1 < len(nums[list_idx]):
            next_value = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
            max_value = max(max_value, next_value)
        else:
            # If any list is exhausted, stop
            break
    
    return best_range

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(smallestRange(nums))