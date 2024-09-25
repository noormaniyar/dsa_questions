"""

You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

"""
class Solution(object):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.count = 0

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()
        
        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = Solution.TrieNode()
                node = node.children[char]
                node.count += 1
        
        def score_prefixes(self, word):
            node = self.root
            total_score = 0
            for char in word:
                if char in node.children:
                    node = node.children[char]
                    total_score += node.count
                else:
                    break
            return total_score

    def sumPrefixScores(self, words):
        trie = Solution.Trie()

        for word in words:
            trie.insert(word)

        result = []

        for word in words:
            result.append(trie.score_prefixes(word))

        return result

# Example test case
words1 = ["abc", "ab", "bc", "b"]
words2 = ["abcd"]

solution = Solution()
print(solution.sumPrefixScores(words1))  # Output: [5, 4, 3, 2]
print(solution.sumPrefixScores(words2))  # Output: [4]
