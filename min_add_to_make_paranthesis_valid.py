"""
    A parentheses string is valid if and only if:
    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
    Return the minimum number of moves required to make s valid.
"""
def minAddToMakeValid(s: str) -> int:
    left = 0  # Unmatched opening parentheses
    right = 0  # Unmatched closing parentheses
    
    for char in s:
        if char == '(':
            left += 1  # Expect a closing parenthesis later
        elif char == ')':
            if left > 0:
                left -= 1  # We have a matching opening parenthesis, so balance it
            else:
                right += 1  # No opening parenthesis to match, so we need an extra
    
    # Total moves required to balance both unmatched '(' and ')'
    return left + right

s = "()))"
print(minAddToMakeValid(s))