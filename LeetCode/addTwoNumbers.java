// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int x) { val = x; }
// }
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode con = new ListNode(0);
        ListNode p = l1;
        ListNode q = l2;
        ListNode temp = con;
        int i, j;
        int flag = 0;
        while (p != null || q != null) {
            i = p.val;  // i = (p != null) ? p.val : 0
            j = q.val;  // j = (q != null) ? p.val : 0
            if (i + j + flag >= 10) { 
                temp.val = (i + j + flag) % 10;
                flag = 1;
            }
            else{
                temp.val = i + j + flag;
                flag = 0;
            }
            if (p != null) p = p.next;
            if (q != null) q = q.next;
            if (p != null || q != null) {
                temp.next = new ListNode(0);
                temp = temp.next;
            }
 /**         
 *           p = p.next;
 *           q = q.next;
 *           if (p != null) {
 *               temp.next = new ListNode(0);
 *               temp = temp.next;
 */           }
        }
        if (flag == 1) {
            temp.next = new ListNode(1);
        }
        return con;
    }
}


// In this question, I set a List without dummy head. For 15 line and 16 line, the comment parts are right codes which consider the some
// unusual test cases.
// I found if i put the codes which judge if p or q is null or not into one conditional statements, there would be a time exceed problem.

// Here is the official answer.
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
