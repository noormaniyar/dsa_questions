"""
    You are given the root of a binary tree and a positive integer k.
    The level sum in the tree is the sum of the values of the nodes that are on the same level.
    Return the kth largest level sum in the tree (not necessarily distinct). 
    If there are fewer than k levels in the tree, return -1.
    Note that two nodes are on the same level if they have the same distance from the root.
"""
import heapq
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return -1
        
        # Queue for BFS traversal
        queue = deque([root])
        level_sums = []
        
        # Traverse the tree level by level
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Accumulate the sum of node values at the current level
                level_sum += node.val
                
                # Append child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the current level sum to the list
            level_sums.append(level_sum)
        
        # If there are fewer than k levels, return -1
        if len(level_sums) < k:
            return -1
        
        # Use heapq to find the kth largest sum
        return heapq.nlargest(k, level_sums)[-1]


# Construct a sample tree:
#         5
#        / \
#       2   9
#      /   / \
#     1   8   7

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.right.left = TreeNode(8)
root.right.right = TreeNode(7)

sol = Solution()
k = 2
print(sol.kthLargestLevelSum(root, k))  # Expected output: 16 (level sums: [5, 11, 16])
