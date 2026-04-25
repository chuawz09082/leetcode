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
    int count;
    public int goodNodes(TreeNode root) {
        count = 0;
        dfs(root, root.val);
        return count;
    }

    private void dfs(TreeNode node, int val){
        if (node.val >= val) count += 1;

        if (node.left != null){
            dfs(node.left, Math.max(val, node.left.val));
        }

        if (node.right != null){
            dfs(node.right, Math.max(val, node.right.val));
        }
    }
}