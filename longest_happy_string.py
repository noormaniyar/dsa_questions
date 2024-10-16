"""
    A string s is called happy if it satisfies the following conditions:
    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.
    Given three integers a, b, and c, return the longest possible happy string. 
    If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
    A substring is a contiguous sequence of characters within a string.
"""

import heapq

def longestHappyString(a: int, b: int, c: int) -> str:
    # Create a max heap with the available characters
    max_heap = []
    
    # Only add characters that have non-zero counts
    if a > 0:
        heapq.heappush(max_heap, (-a, 'a'))
    if b > 0:
        heapq.heappush(max_heap, (-b, 'b'))
    if c > 0:
        heapq.heappush(max_heap, (-c, 'c'))
    
    result = []
    
    while max_heap:
        # Pop the character with the most occurrences
        count1, char1 = heapq.heappop(max_heap)
        if len(result) >= 2 and result[-1] == result[-2] == char1:
            # If adding char1 would create three consecutive same characters, try the next character
            if not max_heap:
                break  # If there's no other character to use, we're done
            count2, char2 = heapq.heappop(max_heap)
            result.append(char2)
            count2 += 1  # Decrease the count of char2 since we've used one instance
            if count2 != 0:
                heapq.heappush(max_heap, (count2, char2))  # Reinsert if there's any left
            heapq.heappush(max_heap, (count1, char1))  # Reinsert char1 for the next round
        else:
            # Otherwise, we can safely add char1
            result.append(char1)
            count1 += 1  # Decrease the count of char1 since we've used one instance
            if count1 != 0:
                heapq.heappush(max_heap, (count1, char1))  # Reinsert if there's any left
    
    return ''.join(result)


a = 1
b = 1
c = 7
print(longestHappyString(a, b, c))