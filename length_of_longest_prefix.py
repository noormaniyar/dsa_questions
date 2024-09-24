"""
    You are given two arrays with positive integers arr1 and arr2.

    A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. 
    For example, 123 is a prefix of the integer 12345, while 234 is not.

    A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. 
    For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

    You need to find the length of the longest common prefix between all pairs of integers (x, y) 
    such that x belongs to arr1 and y belongs to arr2.

    Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num_str):
        node = self.root
        for char in num_str:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def find_longest_prefix(self, num_str):
        node = self.root
        length = 0
        for char in num_str:
            if char in node.children:
                length += 1
                node = node.children[char]
            else:
                break
        return length

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()

        # Insert all numbers from arr2 into the trie
        for num in arr2:
            trie.insert(str(num))
        
        max_prefix_length = 0

        # Find the longest common prefix for each number in arr1
        for num in arr1:
            prefix_length = trie.find_longest_prefix(str(num))
            max_prefix_length = max(max_prefix_length, prefix_length)

        return max_prefix_length


# Example 1:
solution = Solution()
arr1 = [1, 10, 100]
arr2 = [1000]
print(solution.longestCommonPrefix(arr1, arr2))  # Output: 3

# Example 2:
arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(solution.longestCommonPrefix(arr1, arr2))  # Output: 0

# Example 3:
arr1 = [123, 456, 789]
arr2 = [12345, 45678, 78901]
print(solution.longestCommonPrefix(arr1, arr2))  # Output: 3
