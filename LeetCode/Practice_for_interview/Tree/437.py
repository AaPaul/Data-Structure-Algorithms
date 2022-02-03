# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity is O(n), space complexity is O(n). N is the number of node
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # record the prefix from root to curr node
        prefix = defaultdict(int)
        # set the initial record. Before visit root node, the prefix = 0 starting with 1
        prefix[0] = 1
        
        # iterating the tree by dfs.
        def dfs(node, curr):
            # set boundry
            if not node:
                return 0
            # the variable which can store the number of result in this layer starting with 0
            ret = 0
            # curr is the prefix from root to this node
            curr += node.val
            
            # check if there is a node where the value between that node and curr node is targetSum.
            # The start node would be the next of that node.
            ret += prefix[curr - targetSum]
            # store the value into the prefix dictionary for next calculating
            prefix[curr] += 1
            # check left subtree and right subtree
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            # before return to the previous layer, we should delete the value stored in this layer
            prefix[curr] -= 1
            
            return ret
        
        return dfs(root, 0)