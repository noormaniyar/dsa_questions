"""
    A sequence x1, x2, ..., xn is Fibonacci-like if:
    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n
    Given a strictly increasing array arr of positive integers forming a sequence, 
    return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
    A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, 
    without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""
def lenLongestFibSubseq(arr):
    n = len(arr)
    index = {x: i for i, x in enumerate(arr)}  # Hash map to store value to index mapping
    dp = [[2] * n for _ in range(n)]  # Initialize dp array with 2, the minimum subsequence length

    max_len = 0  # Variable to track the longest Fibonacci-like subsequence
    
    # Loop through all pairs arr[i], arr[j] with i < j
    for j in range(n):
        for i in range(j):
            # arr[i] + arr[j] = arr[k], hence arr[k] = arr[j] - arr[i]
            if arr[j] - arr[i] in index:
                k = index[arr[j] - arr[i]]  # Get the index of arr[k]
                if k < i:  # Ensure that k < i (to form a valid subsequence)
                    dp[i][j] = dp[k][i] + 1  # Extend the subsequence
                    max_len = max(max_len, dp[i][j])  # Update the max length
    
    return max_len if max_len >= 3 else 0  # Return the max length, or 0 if no valid subsequence

arr  = [1,2,3,4,5,6,7,8]
print(lenLongestFibSubseq(arr))