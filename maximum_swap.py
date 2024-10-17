"""
    You are given an integer num. You can swap two digits at most once to get the maximum valued number.
    Return the maximum valued number you can get.
"""
def maximumSwap(num: int) -> int:
    # Convert the number to a list of digits
    num_list = list(str(num))
    
    # Create a dictionary to store the last occurrence of each digit
    last = {int(digit): i for i, digit in enumerate(num_list)}
    
    # Traverse the number's digits
    for i, digit in enumerate(num_list):
        # Check if there's a larger digit that appears later
        for d in range(9, int(digit), -1):
            if last.get(d, -1) > i:
                # Swap the current digit with the larger digit
                num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                # Return the integer formed by the swapped digits
                return int(''.join(num_list))
    
    # If no swap is performed, return the original number
    return num

# Test cases
print(maximumSwap(2736))  # Output: 7236
print(maximumSwap(9973))  # Output: 9973
