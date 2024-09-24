"""

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.


"""

def fractionToDecimal(numerator: int, denominator: int) -> str:
    print('-----------------------fraction to decimal called---------------------')
    if numerator == 0:
        return "0"
    
    result = []
    print(result, '========================result===========================')
    
    
    # Determine the sign of the result
    if (numerator < 0) != (denominator < 0):
        result.append('-')
    
    # Work with absolute values of numerator and denominator
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Append the integer part
    integer_part = numerator // denominator
    result.append(str(integer_part))
    
    remainder = numerator % denominator
    if remainder == 0:
        return ''.join(result)  # No fractional part
    
    result.append('.')
    
    # Dictionary to store the index of the remainder
    remainder_dict = {}
    
    # While remainder is not zero, we calculate the decimal part
    while remainder != 0:
        # If the remainder is already in the dictionary, we found a repeating part
        if remainder in remainder_dict:
            index = remainder_dict[remainder]
            result.insert(index, '(')
            result.append(')')
            break
        
        # Store the current position of the remainder in the result
        remainder_dict[remainder] = len(result)
        
        # Multiply remainder by 10 (simulating long division) to get the next digit
        remainder *= 10
        fractional_part = remainder // denominator
        result.append(str(fractional_part))
        
        # Update remainder to reflect the current division step
        remainder = remainder % denominator
    return ''.join(result)



fractionToDecimal(numerator=7, denominator=9)