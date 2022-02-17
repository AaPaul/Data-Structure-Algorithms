# Definition for a binary tree node.
from queue import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        num_old, level_old, max_width = 1, 1, 0 # the first two numbers represent the most left node in each layer.
        queue = deque([[level_old, num_old, root]])
        
        while queue:
            [l, num, node] = queue.popleft()
            if l > level_old:
                level_old = l
                num_old = num
            max_width = max(max_width, num - num_old + 1)
            if node.left:
                queue.append([l+1, num*2, node.left])
            if node.right:
                queue.append([l+1, num*2+1, node.right])
                
        return max_width

s1= Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = None
root.right.left = TreeNode(9)
print(s1.widthOfBinaryTree(root))

        
# In a loop, the elements in a list can be use as sperated variables if we allocate a name for them
# For problems related binary tree, we often use BFS or DFS. In this question, time complexity is O(n)
# where n is the number of nodes. If use DFS, the time complexity would be O(h) where h is the height of the tree.

# Binary tree
# Relationships between children (C) and the corresponding parent (P)
# position: left child: C = 2P   right child: C = 2P + 1


# Ref.
# https://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/
# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/726732/Python-10-lines-BFS-explained-with-figure