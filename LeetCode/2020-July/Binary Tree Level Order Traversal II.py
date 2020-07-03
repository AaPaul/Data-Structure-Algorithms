# A classic BFS question.
# 层序遍历的实现
# difference between res.reversed() and list(reversed(res))
# the second one of reversing method is based on rows

# Definition for a binary tree node.
from typing import List
from queue import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):
        if not root: return []

        Out_temp, deq = [], deque([[root, 0]])

        while deq:
            elem = deq.popleft()
            Out_temp.append([elem[0].val, elem[1]])
            if elem[0].left:
                deq.append([elem[0].left, elem[1] + 1])
            if elem[0].right:
                deq.append([elem[0].right, elem[1] + 1])

        Out = [[Out_temp[0][0]]]
        for i in range(1, len(Out_temp)):
            if Out_temp[i][1] == Out_temp[i - 1][1]:
                Out[Out_temp[i][1]].append(Out_temp[i][0])
            else:
                Out.append([Out_temp[i][0]])
        # This part need to be paying attention to which shows the reversed list
        return Out[::-1]

        # A very simple and beatiful method to implement the function
        # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        #     if not root:
        #         return []
        #     queue = []
        #     searched = []
        #     res = []
        #     queue.append(root)
        #     while queue:
        #         # the loop in list
        #         res.append([q.val for q in queue])
        #         queue = [kid for q in queue for kid in (q.left, q.right) if kid]

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
    print(res)


if __name__ == '__main__':
    main()
