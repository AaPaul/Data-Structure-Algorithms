# 160. Intersection of Two Linked Lists (Easy)

# a: The length of the list A before the intersection part
# b: the length of the list B before the intersection part
# c: the length of the intersection part
# if there is no intersection -> a + b = b + a

# a + c + b = b + c + a


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB
        while l1 != l2:
            if l1 == None:
                l1 = headB
            else:
                l1 = l1.next
            if l2 == None:
                l2 = headA
            else:
                l2 = l2.next
        return l1 