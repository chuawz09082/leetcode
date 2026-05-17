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
    public int kthSmallest(TreeNode root, int k) {

        TreeSet<Integer> nodes = new TreeSet<>();

        ArrayDeque<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);

        while (!queue.isEmpty()){
            TreeNode node = queue.poll();
            if (nodes.size() == k ) {
                if (nodes.last() > node.val) nodes.pollLast();
                else if (nodes.last() < node.val) continue;
            }

            nodes.add(node.val);

            if (node.right != null){
                queue.addFirst(node.right);
            }

            if (node.left != null){
                queue.addFirst(node.left);
            }

        }


        return nodes.last();
        
    }
}