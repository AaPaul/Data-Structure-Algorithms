# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTree(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            
            for i in range(start, end+1):
                left = generateTree(start, i-1)
                right = generateTree(i+1, end)
                
                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        allTrees.append(curr)
            return allTrees
        
        return generateTree(1, n) if n else []