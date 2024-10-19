"""
    Given two positive integers n and k, the binary string Sn is formed as follows:
    S1 = "0"
    Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
    Where + denotes the concatenation operation, reverse(x) returns the reversed string x, 
    and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
    For example, the first four strings in the above sequence are:

    S1 = "0"
    S2 = "011"
    S3 = "0111001"
    S4 = "011100110110001"
    Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
"""

def findKthBit(n: int, k: int) -> str:
    # Helper function to find the k-th bit in Sn
    def findBit(n, k):
        if n == 1:
            return '0'
        
        length = (1 << n) - 1  # Length of Sn, which is 2^n - 1
        mid = length // 2 + 1   # The middle position
        
        if k == mid:
            return '1'
        elif k < mid:
            return findBit(n - 1, k)
        else:
            # In the second half: reverse and invert corresponds to n - (k - mid)
            return '0' if findBit(n - 1, length - k + 1) == '1' else '1'
    
    return findBit(n, k)

# Example usage:
n = 4
k = 11
print(findKthBit(n, k))  # Output should be "1"
