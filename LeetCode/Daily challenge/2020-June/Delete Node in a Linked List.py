# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

    # Build 2 transfer functions
    def deleteNode1(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        def getHead(head: List):
            lNode = ListNode(head[0])
            temp = lNode
            for i in head[1:]:
                p = ListNode(i)
                temp.next = p
                temp = p
            return lNode

        def transferHead(n: ListNode):
            l = []
            while n.next != None:
                l.append(n.val)
            return l

        head1 = getHead(head)
        p = head1
        while (p.val != node.val):
            before_p = p
            p = p.next
        before_p.next = node.next

        # head = transferHead(head1)

# head = [4, 5, 1, 6]
# s1 = Solution()
# l1 = s1.getHead(head)
# print(l1.val)
