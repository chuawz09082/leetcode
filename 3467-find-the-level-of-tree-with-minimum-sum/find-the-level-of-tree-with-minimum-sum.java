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
    // Static variables to store level sums, minimum index, and minimum sum
    static List<Long> array_num;
    static int minidx;
    static long minsum;

    public int minimumLevel(TreeNode root) {
        // Initialize the array to store the sum of node values at each level
        array_num = new ArrayList<>();

        // Populate `array_num` with level sums using the helper function
        helper(root, 0);

        // Initialize variables to find the minimum sum level
        minidx = -1;
        minsum = Long.MAX_VALUE;

        // Iterate through the level sums to find the minimum sum and its index
        for (int i = 0; i < array_num.size(); i++) {
            if (array_num.get(i) < minsum) {
                minsum = array_num.get(i);  // Update minimum sum
                minidx = i;                 // Update index of minimum sum
            }
        }

        // Return the 1-based index of the level with the minimum sum
        return minidx + 1;
    }

    // Recursive helper function to calculate level sums
    public static void helper(TreeNode root, int depth) {
        // Base case: if node is null, return
        if (root == null) {
            return;
        }

        // If this is the first node at the current depth, add its value to `array_num`
        if (depth == array_num.size()) {
            array_num.add((long) root.val);
        } else {
            // Otherwise, add the current node's value to the existing sum for this level
            array_num.set(depth, array_num.get(depth) + root.val);
        }

        // Recur for the left and right children, increasing depth by 1 for each call
        helper(root.left, depth + 1);
        helper(root.right, depth + 1);
    }
}