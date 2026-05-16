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

        int carry = 0;
        ListNode currentL1 = l1;
        ListNode currentL2 = l2;
        ListNode currentAns = ans;

        while (currentL1 != null && currentL2 != null){
            int digit = currentL1.val + currentL2.val + carry;
            
            currentAns.next = new ListNode(digit%10);
            carry = digit/10;

            currentL1 = currentL1.next;
            currentL2 = currentL2.next;
            currentAns = currentAns.next;

        }

        
        ListNode currentRemain;
        if (currentL1 != null) currentRemain = currentL1; 
        else currentRemain = currentL2; 

        while (currentRemain != null){
            int digit = currentRemain.val + carry;
            
            currentAns.next = new ListNode(digit%10);
            carry = digit/10;

            currentRemain = currentRemain.next;
            currentAns = currentAns.next;
        }

        if (carry > 0){
            currentAns.next = new ListNode(carry);
        }

        return ans.next;
    }
}