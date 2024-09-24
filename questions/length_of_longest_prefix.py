"""
    You are given two arrays with positive integers arr1 and arr2.

    A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. 
    For example, 123 is a prefix of the integer 12345, while 234 is not.

    A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. 
    For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

    You need to find the length of the longest common prefix between all pairs of integers (x, y) 
    such that x belongs to arr1 and y belongs to arr2.

    Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
"""

def get_common_prefix_length(a, b):
    # Convert the integers to strings to compare digit by digit
    a_str, b_str = str(a), str(b)
    i = 0
    # Compare the characters at each position
    while i < len(a_str) and i < len(b_str) and a_str[i] == b_str[i]:
        i += 1
    return i

def longest_common_prefix(arr1, arr2):
    max_prefix_length = 0
    
    # Iterate over all pairs (x, y) where x is from arr1 and y is from arr2
    for x in arr1:
        for y in arr2:
            # Get the common prefix length between x and y
            prefix_length = get_common_prefix_length(x, y)
            # Update the maximum prefix length
            max_prefix_length = max(max_prefix_length, prefix_length)
    
    return max_prefix_length

# Example 1:
arr1 = [1, 10, 100]
arr2 = [1000]
print(longest_common_prefix(arr1, arr2))  # Output: 3

# Example 2:
arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(longest_common_prefix(arr1, arr2))  # Output: 0
