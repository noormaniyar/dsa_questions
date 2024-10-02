"""
    Given an array of integers arr, replace each element with its rank.
    The rank represents how large the element is. The rank has the following rules:
    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.
"""

def arrayRankTransform(arr):
    sorted_arr = sorted(set(arr))
    rank_map = {value: rank + 1 for rank, value in enumerate(sorted_arr)}
    return [rank_map[element] for element in arr]


arr = [40, 10, 20, 30, 20]
print(arrayRankTransform(arr))


