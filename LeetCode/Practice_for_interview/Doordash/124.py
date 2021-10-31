# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumUtil(self, root, res):
        if root is None:
            return 0
        ls = max(self.maxSumUtil(root.left, res), 0)
        rs = max(self.maxSumUtil(root.right, res), 0)
        nodePrice = ls + rs + root.val 
        res[0] = max(res[0], nodePrice)

        return root.val + max(ls, rs)
    def maxPathSum(self, root: TreeNode) -> int:
        INT_MIN = -2**32
        res = [-10^9]
        self.maxSumUtil(root, res)
        return res[0]

if __name__ == "__main__":
    s1 = Solution()
    case1 = TreeNode(-3)
    print(s1.maxPathSum(case1))