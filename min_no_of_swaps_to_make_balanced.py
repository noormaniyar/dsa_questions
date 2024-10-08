"""
    You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' 
    and n / 2 closing brackets ']'.
    A string is called balanced if and only if:
        It is the empty string, or
        It can be written as AB, where both A and B are balanced strings, or
        It can be written as [C], where C is a balanced string.
        You may swap the brackets at any two indices any number of times.
        Return the minimum number of swaps to make s balanced.
"""
def minSwaps(s: str) -> int:
    balance = 0
    swaps = 0
    
    for bracket in s:
        if bracket == '[':
            balance += 1
        else:  # bracket == ']'
            balance -= 1
        
        # If the balance is negative, we need a swap
        if balance < 0:
            swaps += 1
            balance = 1  # After the swap, the balance becomes +1
    
    return swaps


s = "][][["
print(minSwaps(s))