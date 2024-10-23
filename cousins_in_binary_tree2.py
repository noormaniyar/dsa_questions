"""
    Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
    Two nodes of a binary tree are cousins if they have the same depth with different parents.
    Return the root of the modified tree.
    Note that the depth of a node is the number of edges in the path from the root node to it.
"""
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def replace_value_with_cousins(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    # Perform a level order traversal and store parent and depth information
    queue = deque([(root, None, 0)])  # (node, parent, depth)
    level_map = defaultdict(list)  # Map depth -> [(node, parent)]
    
    while queue:
        node, parent, depth = queue.popleft()
        level_map[depth].append((node, parent))
        
        if node.left:
            queue.append((node.left, node, depth + 1))
        if node.right:
            queue.append((node.right, node, depth + 1))
    
    # For each level, calculate the cousin sum for each node
    for depth, nodes in level_map.items():
        total_sum = sum(node.val for node, _ in nodes)  # Total sum of current level
        
        for node, parent in nodes:
            # Calculate the sibling sum
            sibling_sum = 0
            for other_node, other_parent in nodes:
                if other_parent == parent:  # Nodes with the same parent are siblings
                    sibling_sum += other_node.val
            
            # Cousin sum = total sum - sibling sum
            cousin_sum = total_sum - sibling_sum
            node.val = cousin_sum
    
    return root

# Utility function to print level order of tree for verification
def print_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    for level in result:
        print(level)

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Original Tree (Level Order):")
print_level_order(root)

# Replace node values with cousin sums
replace_value_with_cousins(root)

print("\nModified Tree (Level Order with Cousin Sums):")
print_level_order(root)

