def singleNumber(nums):
    ones, twos = 0, 0
    
    for num in nums:
        # Update ones and twos based on current num
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    print(ones, '========================ones=========================================')
    return ones

nums = [2, 2, 3, 2]
nums = [0, 1, 0, 1, 0, 1, 99]

singleNumber(nums)