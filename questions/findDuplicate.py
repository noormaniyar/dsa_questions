def findDuplicate(nums):
    # Step 1: Initialize the a and b pointers
    a = nums[0]
    b = nums[0]
    
    # Step 2: Find the intersection point of the two runners
    while True:
        a = nums[a]  # a moves by 1 step
        b = nums[nums[b]]  # b moves by 2 steps
        if a == b:  # intersection point found
            break
    
    # Step 3: Find the entrance to the cycle
    a = nums[0]  # reset a to the beginning
    while a != b:  # move both one step at a time
        a = nums[a]
        b = nums[b]
    print(a, '=============================a======================')
    return a  # a or b is now at the start of the cycle


nums = [1, 3, 4, 2, 2]
findDuplicate(nums)