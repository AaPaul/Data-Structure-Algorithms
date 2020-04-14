# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 1  # means the start node

    # Method 1 in O(N) time complexity
    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        def diameter(node: TreeNode):
            if not node:
                return 0
            left = diameter(node.left)
            right = diameter(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        diameter(root)
        return self.ans - 1  # we want the length of path instead of the number of visited nodes

    # Method 2 in O(N^2) time complexity
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node: TreeNode):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            return max(left, right) + 1

        # print(height(root))
        def diameter(node: TreeNode):
            if not node:
                return 0
            l_height = height(node.left)
            r_height = height(node.right)

            l_diameter = diameter(node.left)
            r_diameter = diameter(node.right)

            return max(l_height + r_height + 1, max(l_diameter, r_diameter))

        print(diameter(root) - 1)
        # if not root: # should consider the special case: []
        #     return 0
        # else:
        #     return diameter(root) - 1


lst = [4, 2, 5, 1, 3]
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
a = tree.left
a.left = TreeNode(4)
a.right = TreeNode(5)

s1 = Solution()
s1.diameterOfBinaryTree(tree)
# Note:
"""
1. Create a tree

2. The key point is that we need to understand the diameter is the number that is based on the height of the tree.

3. Method 1: Using a variable to record the max diameter so that we do not need to visit another time to find the maximum diameter
of the subnode

4. Unfamiliar with the operation about the binary tree. Need more practise.

5. If you face a question about a tree, just mock the process in runtime of the program manually which can help you further understand
the mechanism.
"""
# Reference
# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
# https://leetcode.com/problems/diameter-of-binary-tree/solution/
