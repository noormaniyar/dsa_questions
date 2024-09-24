"""

The XOR sum of a list is the bitwise XOR of all its elements. If the list only contains one element, 
then its XOR sum will be equal to this element.

For example, the XOR sum of [1,2,3,4] is equal to 1 XOR 2 XOR 3 XOR 4 = 4, and the XOR sum of [3] is equal to 3.
You are given two 0-indexed arrays arr1 and arr2 that consist only of non-negative integers.

Consider the list containing the result of arr1[i] AND arr2[j] (bitwise AND) for every
(i, j) pair where 0 <= i < arr1.length and 0 <= j < arr2.length.

Return the XOR sum of the aforementioned list.

"""
def xor_sum_of_and(arr1, arr2):
    xor_sum = 0
    # Consider 32-bit integers (adjust if needed)
    for k in range(12):
        print(k, '-----------------------------------------------k----------------------------')
        count1 = sum((num >> k) & 1 for num in arr1)  # Count of 1s in the k-th bit in arr1
        print(count1, '----------------------count1-------------------------')
        count2 = sum((num >> k) & 1 for num in arr2)  # Count of 1s in the k-th bit in arr2
        print(count2, '-------------------------count2--------------------------')
        
        # If count1 * count2 is odd, then the k-th bit contributes to the final XOR sum
        if (count1 * count2) % 2 == 1:
            xor_sum |= (1 << k)
    
    return xor_sum


# Example Usage

# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]

arr1 = [12]
arr2 = [4]

result = xor_sum_of_and(arr1, arr2)
print(result)  # Output will be the XOR sum of the AND operations
