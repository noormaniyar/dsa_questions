"""
    You are given a 0-indexed string s and a dictionary of words dictionary. 
    You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
    There may be some extra characters in s which are not present in any of the substrings.
    Return the minimum number of extra characters left over if you break up s optimally.
"""

def minExtraChar(s, dictionary):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No extra characters at the start
    
    # Convert dictionary to a set for faster lookups
    dictionary_set = set(dictionary)
    
    for i in range(1, n + 1):
        # By default, assume we can't match any word ending at i-1
        dp[i] = dp[i-1] + 1
        
        # Check for all possible words ending at index i-1
        for word in dictionary_set:
            if i >= len(word) and s[i-len(word):i] == word:
                dp[i] = min(dp[i], dp[i-len(word)])
    
    # The answer is the minimum extra characters for the whole string
    return dp[n]

# Example usage:
s1 = "leetscode"
dictionary1 = ["leet", "code", "leetcode"]
print(minExtraChar(s1, dictionary1))  # Output: 1

s2 = "sayhelloworld"
dictionary2 = ["hello", "world"]
print(minExtraChar(s2, dictionary2))  # Output: 3
