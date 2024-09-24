from itertools import combinations

def minimumDifference(nums):
    n = len(nums) // 2
    total_sum = sum(nums)
    target = total_sum // 2
    
    first_half = nums[:n]
    print(first_half, '----------------------------first_half---------------------')
    second_half = nums[n:]
    print(second_half, '---------------------------second_half--------------------')
    
    def get_subset_sums(arr):
        subset_sums = [[] for _ in range(len(arr) + 1)]
        for r in range(len(arr)+1):
            for combo in combinations(arr, r):
                subset_sums[r].append(sum(combo))
        return subset_sums
    
    first_sums = get_subset_sums(first_half)
    print(first_sums, '----------------------first_sums--------------------')
    second_sums = get_subset_sums(second_half)
    print(second_sums, '---------------------second_sums-------------------')
    
    for i in range(len(second_sums)):
        second_sums[i].sort()
    
    min_diff = float('inf')
    
    for r in range(n+1):
        print(r, '-------------------r-----------------')
        for s1 in first_sums[r]:
            print(s1, '------------------s1-------------------')
            left = target - s1
            second_candidates = second_sums[n - r]
            lo, hi = 0, len(second_candidates) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                s2 = second_candidates[mid]
                current_sum = s1 + s2
                diff = abs(total_sum - 2 * current_sum)
                min_diff = min(min_diff, diff)
                print(min_diff, '-------------------------min_diff------------------------')
                if s2 < left:
                    lo = mid + 1
                else:
                    hi = mid - 1
    return min_diff


print(minimumDifference([3, 9, 7, 3]))
print(minimumDifference([-36, 36]))
print(minimumDifference([2, -1, 0, 4, -2, -9]))
