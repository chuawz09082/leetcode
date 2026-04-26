/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    PriorityQueue<Integer> pq;
    public int kthSmallest(TreeNode root, int k) {
        pq = new PriorityQueue<>((a,b) -> b - a);
        dfs(root, k , pq);
        return pq.poll();
    }

    private void dfs(TreeNode node, int k, PriorityQueue<Integer> pq){
        if (pq.size() == k && pq.peek() > node.val){
            pq.poll();
            pq.offer(node.val);
        } else if (pq.size() < k){
            pq.offer(node.val);
        }

        if (node.left != null) dfs(node.left, k ,pq);
        if (node.right != null) dfs(node.right, k ,pq);
    }
}