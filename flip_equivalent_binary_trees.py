class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Base case: if both are None, they are equivalent
        if not root1 and not root2:
            return True
        # If only one is None or their values are different, they are not equivalent
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # Check flip equivalence
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

# Example usage:
# Manually creating the trees from the example:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(6)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.left.left = TreeNode(6)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)

# Check if they are flip equivalent
solution = Solution()
print(solution.flipEquiv(root1, root2))  # Output: True
