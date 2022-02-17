# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # root = TreeNode(postorder[-1])
        r_num = len(postorder) - 1
        def split_list(inorder: List, postorder: List, r: int):
            if r == 1:
                return TreeNode(inorder[0])
            if postorder[r] not in inorder:
                return 
            node = TreeNode(postorder[r])
            mid = inorder.index(postorder[r])
            i_left, i_right = inorder[:mid], inorder[mid+1:]
            p_left
            node.left = split_list(left,)
        root = split_list(inorder, postorder, r_num)
