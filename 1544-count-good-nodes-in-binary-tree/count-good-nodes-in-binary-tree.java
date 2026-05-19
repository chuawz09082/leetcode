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
    public int goodNodes(TreeNode root) {
        if (root == null) return 0;
        
        return 1+dfs(root, root.val);
    }

    private int dfs(TreeNode node, int current){
        if (node == null) return 0;


        int left = 0;
        if (node.left != null){
            if (node.left.val < current) left = dfs(node.left, current);
            else left = 1+dfs(node.left, node.left.val);
        }

        int right = 0;
        if (node.right != null){
            if (node.right.val < current) right = dfs(node.right, current);
            else right = 1+dfs(node.right, node.right.val);
        }

        return left+right;
    }
}