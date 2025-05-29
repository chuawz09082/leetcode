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
    public TreeNode invertTree(TreeNode root) {
        if (root == null){
            return root;
        }
        TreeNode current = root;
        List<TreeNode> queue = new ArrayList<>();

        queue.add(current);

        while (!queue.isEmpty()){
            List<TreeNode> nxtLevel = new ArrayList<>();

            for (TreeNode node: queue){
                if (node.left != null){
                    nxtLevel.add(node.left);
                }
                if (node.right != null){
                    nxtLevel.add(node.right);
                }
                TreeNode left = node.left;
                TreeNode right = node.right;
                node.left = right;
                node.right = left;
            }
            queue = nxtLevel;
        }

        return root;
    }
}