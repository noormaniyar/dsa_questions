"""
    Given two strings s1 and s2, return true if s2 contains a permutation
    of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.
"""
from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 > len_s2:
        return False
    # Count the frequency of characters in s1
    s1_count = Counter(s1)
    window_count = Counter()
    # Start sliding window over s2
    for i in range(len_s2):
        # Add current character to the window count
        window_count[s2[i]] += 1
        # If the window size exceeds the length of s1, remove the leftmost character
        if i >= len_s1:
            if window_count[s2[i - len_s1]] == 1:
                del window_count[s2[i - len_s1]]
            else:
                window_count[s2[i - len_s1]] -= 1
        # Compare the current window with the frequency count of s1
        if window_count == s1_count:
            return True
    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))