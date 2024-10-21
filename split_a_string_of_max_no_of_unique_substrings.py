"""
    Given a string s, return the maximum number of unique substrings that the given string can be split into.
    You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. 
    However, you must split the substrings such that all of them are unique.
    A substring is a contiguous sequence of characters within a string.
"""
def maxUniqueSplit(s: str) -> int:
    def backtrack(start, seen):
        if start == len(s):
            return 0
        
        max_splits = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in seen:
                seen.add(substring)
                # Recursively find the rest of the split and add 1 for the current split
                max_splits = max(max_splits, 1 + backtrack(end, seen))
                # Backtrack
                seen.remove(substring)
        return max_splits

    return backtrack(0, set())

# Example usage:
s1 = "ababccc"
s2 = "aba"
s3 = "aa"

print(maxUniqueSplit(s1))  # Output: 5
print(maxUniqueSplit(s2))  # Output: 2
print(maxUniqueSplit(s3))  # Output: 1

