# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # The list with head means that there is no node with null value as the first node instead that the first node is the head.
    def middleNode(self, head: ListNode) -> ListNode:
        count1 = 0
        s = head
        while (s != None):
            count1 += 1
            s = s.next
        # if count % 2 == 0:
        #     mid = count1 // 2 + 1
        # else:
        #     mid = (count1 // 2) + 1
        mid = count1 // 2 + 1
        s1 = head
        count = 1
        # ans = ListNode(None)
        while (s1 != None):
            if count == mid:
                ans = s1
                break
            count += 1
            s1 = s1.next
        return ans

    def middleNode_mine(self, head: ListNode) -> ListNode:
        count = 0
        s = head
        while (s.next != None):
            count += 1
            s = s.next
        # mid = (count % 2 == 0) ? (count // 2 + 1) : (count // 2)
        # if count % 2 == 0:
        #     mid = count // 2 + 1
        # else:
        #     mid = count // 2  # mid =3   +1
        mid = count // 2 + 1
        s = head
        count = 0
        while (s.next != None):
            if count == mid:
                # ans = ListNode(s.val)
                # ans.next = s.next
                ans = s
                break
            count += 1
            s = s.next
        # ans = ListNode(None)
        # while (s.next != None):
        #     if count == mid:
        #         ans.next = s
        #         break
        #     count += 1
        #     s = s.next
        return ans
        # ans = ListNode(-1)
        # while (s.next != None):
        #     if count == mid:
        #         ans.val = s.val
        #         ans.next = s.next
        #         p = ans.next
        #     elif count > mid:
        #         p.val = s.val
        #         p.next = s.next
        #         p = p.next
        #
        #     s = s.next
        #     count += 1

        # return ans


s1 = Solution()
# l1 = ListNode([1,2,3,4,5])
l1 = ListNode(None)
s = ListNode(-1)
l1.next = s
for i in range(1, 6, 1):
    s.val = i
    if i < 5:
        s.next = ListNode(-1)
        s = s.next
    else:
        s.next = None
s = s1.middleNode(l1)
while s.next is not None:
    s = s.next
    print(s.val)
