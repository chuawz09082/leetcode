/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(0);
        ListNode current = ans;
        int total = 0;
        int carry = 0;

        while (l1 != null || l2 != null){

            total = carry;

            if (l1 != null){
                total += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                total += l2.val;
                l2 = l2.next;
            }
            current.next = new ListNode(total%10);
            current = current.next;
            carry = total / 10;
        }

        if (carry > 0) current.next = new ListNode(carry);

        return ans.next;
        
    }
}