# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        res = ListNode()
        first = 1
        while head:
            if head.val != val:
                if first:
                    res = ListNode(head.val)
                    first = 0
                    p = res
                else:
                    p.next = ListNode(head.val)
                    p = p.next
            head = head.next
        if res.val==0:
            return
        else:
            return res

    # This method use head Node to describe the case with null value in the list.
    # Also, this method save the memory as it doesn't rebuild a list instead that
    # it just drop the specific nodes.
    def removeElements1(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        while start.next:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next
        return dummy.next

s1 = Solution()
# l = [1,2,6,3,4,5,6]
l = [1]
first = 1
for i in l:
    if first:
        exa = ListNode(val=i)
        p = exa
        first = 0
    else:
        p.next = ListNode(val=i)
        p = p.next
res1 = s1.removeElements(exa, 1)

# For this example, we should pay attention on Null result.
# Because the default setting of a List is ListNode(0) instead of NULL.