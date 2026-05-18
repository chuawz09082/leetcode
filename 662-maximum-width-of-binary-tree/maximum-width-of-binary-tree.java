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
    public int widthOfBinaryTree(TreeNode root) {

        if (root == null) return 0;

        long maxWidth = 0;

        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root,1L));

        while (!queue.isEmpty()){
            int size = queue.size();
            long min = Long.MAX_VALUE;
            long max = Long.MIN_VALUE;

            for (int i = 0; i < size; i++){
                Pair pair = queue.poll();
                min = Math.min(min, pair.pos);
                max = Math.max(max, pair.pos);

                if (pair.node.left != null) queue.offer(new Pair(pair.node.left, 2*pair.pos-1));
                if (pair.node.right != null) queue.offer(new Pair(pair.node.right, 2*pair.pos));
            }


            maxWidth = Math.max(maxWidth, max-min+1);
        }


        return (int) maxWidth;
        
    }
}

class Pair {

    TreeNode node;
    long pos;

    Pair(TreeNode node, long pos){
        this.node = node;
        this.pos = pos;
    }
}