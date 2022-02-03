from typing import List, Optional, OrderedDict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS and KMP

    # KMP part
    def computeLPSarray(self, pat, lps):
        lps[0]
        j = 1
        n = len(pat)
        len_lps = 0
        while j < n:
            if pat[len_lps] == pat[j]:
                len_lps += 1
                lps[j] = len_lps
                j += 1
            else:
                if len_lps != 0:
                    len_lps = lps[len_lps-1] 
                else:
                    lps[j] = 0
                    j += 1
        # return lps

    def KMPSearch(self, s, t) -> bool:
        m = len(s)
        n = len(t)

        lps = [0] * m

        j = 0
        self.computeLPSarray(s, lps)

        i = 0

        while i < n:
            if s[j] == t[i]:
                i += 1
                j += 1
            
            if j == m:
                j = lps[j-1]
                return True
            elif i < n and s[j] != t[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return False
    
    def getDFSOrder(self, tree, orders):
        if not tree:
            return
        orders.append(tree.val)
        if tree.left:
            self.getDFSOrder(tree.left)
        else:
            orders.append(10**5)
        if tree.right:
            self.getDFSOrder(tree.right)
        else:
            orders.append(-10**5)
            
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        dfsOrder_s, dfsOrder_t = [], []

        self.getDFSOrder(root, dfsOrder_s)
        self.getDFSOrder(subRoot, dfsOrder_t)

        return self.KMPSearch(dfsOrder_s, dfsOrder_t)


    # DFS and brute force 
    def isSubtree2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return self.isRootSubtree(root, subRoot) or self.isSubtree2(root.left, subRoot) or self.isSubtree2(root.right, subRoot)
    
    def isRootSubtree(self, root, t) -> bool:
        if not root and not t:
            return True
        if not root or not t:
            return False
        
        return root.val == t.val and self.isRootSubtree(root.left, t.left) and self.isRootSubtree(root.right, t.right)