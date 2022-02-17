# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def search(res, node:TreeNode):
            if node.left:
                search(res, node.left)
            if node.right:
                search(res, node.right)
            res += 1

        res = 0
        search(res, root)
        return res


