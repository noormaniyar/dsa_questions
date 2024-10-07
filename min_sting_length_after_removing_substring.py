"""
    You are given a string s consisting only of uppercase English letters.
    You can apply some operations to this string where, in one operation, you can remove any occurrence of 
    one of the substrings "AB" or "CD" from s.
    Return the minimum possible length of the resulting string that you can obtain.
    Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
"""

def min_length_string(s: str) -> int:
    stack = []
    
    for char in s:
        if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
            stack.pop()  # Remove "AB" or "CD"
        else:
            stack.append(char)  # Push the current character to stack
            
    return len(stack)

s = "ABFCACDB"
result = min_length_string(s)
print(result)
