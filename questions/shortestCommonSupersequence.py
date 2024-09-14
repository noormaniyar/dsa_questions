"""

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

"""

def shortestCommonSupersequence(str1, str2):
    # Get lengths of both strings
    m, n = len(str1), len(str2)
    
    # DP table for finding LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Now, build the shortest common supersequence using the DP table
    i, j = m, n
    scs = []
    
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            # If the characters match, take it into the result
            scs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # If moving upwards in the DP table gives a higher value, take str1's character
            scs.append(str1[i - 1])
            i -= 1
        else:
            # Otherwise take str2's character
            scs.append(str2[j - 1])
            j -= 1
    
    # Add remaining characters from str1 or str2
    while i > 0:
        scs.append(str1[i - 1])
        i -= 1
    while j > 0:
        scs.append(str2[j - 1])
        j -= 1
    
    # The scs list will have the supersequence in reverse order, so reverse it
    return ''.join(reversed(scs))

str1 = "abac"
str2 = "cab"
print(shortestCommonSupersequence(str1, str2))

