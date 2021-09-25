# 206. Reverse Linked List (Easy)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 尾插法
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p2 = ListNode(-1)
        p1 = head

        while p1 != None:
            temp = p1.next
            p1.next = p2.next
            p2.next = p1
            p1 = temp
        return p2

    # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        node = head.next
        new_head = self.reverseList(node)
        node.next = head
        head.next = None

        return new_head