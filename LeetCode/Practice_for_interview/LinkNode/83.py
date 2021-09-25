# 83. Remove Duplicates from Sorted List (Easy)

# Note: this is the list after SORTED
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = head
        while p1 != None and p1.next != None:
            if p1.val == p1.next.val:
                p1.next = p1.next.next
            else:
                p1 = p1.next
        return head