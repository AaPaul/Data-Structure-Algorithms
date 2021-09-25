# 141. Linked List Cycle (Easy)
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        p2 = head 
        while p1 != None and p2 != None and p2.next != None:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False







# ref
# https://leetcode-cn.com/problems/linked-list-cycle/solution/xiang-jie-wei-shi-yao-yong-yi-bu-liang-b-i6xo/
