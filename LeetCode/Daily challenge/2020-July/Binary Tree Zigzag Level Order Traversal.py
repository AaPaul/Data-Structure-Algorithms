# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        searched = []
        queue = []
        res = []
        queue.append(root)
        count = 0
        while queue:
            if count % 2 == 0:
                res.append([q.val for q in queue])
            else:
                # l = [q.val for q in queue]
                # l.reverse()
                # res.append(l)
                res.append(list(reversed([q.val for q in queue])))
            queue=[k for q in queue for k in (q.left, q.right) if k]
            count += 1
        
        return res

# Note: list.reverse() returns nothing. If we want the reversed list, we need to do it step by step or call reversed() function.

        