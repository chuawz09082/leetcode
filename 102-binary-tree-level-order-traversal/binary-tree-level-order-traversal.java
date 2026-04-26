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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> nodes = new ArrayList<>();

        if (root == null) return nodes;

        ArrayDeque<TreeNode> queue = new ArrayDeque<>(Arrays.asList(root));

        while (!queue.isEmpty()){

            int n = queue.size();
            List<Integer> current = new ArrayList<>();

            for (int i = 0; i < n; i++){
                TreeNode node = queue.pollFirst();
                current.add(node.val);
                if (node.left != null) queue.addLast(node.left);
                if (node.right != null) queue.addLast(node.right);
            }

            nodes.add(current);
        }

        return nodes;
        
    }
}