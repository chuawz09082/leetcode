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
    int maxLength = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return maxLength;
    }

    private int dfs(TreeNode node){
        if (node == null || (node.left == null && node.right == null)) return 0;

        int left = 0;
        int right = 0;

        if (node.left != null) left = 1 + dfs(node.left);
        if (node.right != null) right = 1 + dfs(node.right);


        maxLength = Math.max(maxLength, left + right);

        return Math.max(left, right);
    }
}