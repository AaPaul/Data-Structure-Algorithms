# A classic BFS question.
# 层序遍历的实现
# difference between res.reversed() and list(reversed(res))
# the second one of reversing method is based on rows

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        searched = []
        res = []
        queue.append(root)
        while queue:
            # the loop in list
            res.append([q.val for q in queue])
            queue = [kid for q in queue for kid in (q.left, q.right) if kid]



            # node = queue.pop()
            # if not node.val in searched:
            #     searched.append(node.val)
            # if node.left:
            #     queue.insert(0, node.left)
            #     temp.append(node.left.val)
            # if node.right:
            #     queue.insert(0, node.right)
            #     temp.append(node.right.val)
            # if temp:
            #     res.insert(0, temp)
        return list(reversed(res))
        # res.reverse()
        # return res


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = None
    root.right.left = None
    root.right.right = TreeNode(5)
    s1 = Solution()
    res = s1.levelOrderBottom(root)
    print (res)

if __name__ == '__main__':
    main()
