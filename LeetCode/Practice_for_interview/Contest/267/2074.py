# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h_list = []
        p = head
        k = 1
        while p:
            temp = []
            for i in range(k):
                temp.append(p.val)
                p = p.next
                if p is None:
                    break
            if (len(temp) % 2) == 0:
                temp = temp[::-1]
            h_list.append(temp)      
            k += 1
        h = None
        n = len(h_list)
        i = n-1
        while i>=0:
            n = h_list[i]
            m = len(n)
            j = m - 1
            while j >= 0:
                h = ListNode(n[j], h)
                j -= 1
            i -= 1
        return h
            
            