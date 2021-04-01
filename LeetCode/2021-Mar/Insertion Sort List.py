# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            # if (curr.val > curr.next.val):
            if curr.next and curr.next.val < curr.val:
                temp = curr.next
                curr.next = curr.next.next
                print(1)
                self.insertNode(head, temp)
                # curr = curr.next
            else:
                curr = curr.next
        return head
    
    def insertNode(self, head:ListNode, node:ListNode) -> ListNode:
        curr = head
        prev = ListNode(None)
        while curr and curr.val > node.val:
            prev = curr
            curr = curr.next
        if prev is None:
            node.next = head
            head = node
        else:
            prev.next = node
            node.next = curr
        return head
            
                
                