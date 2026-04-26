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
    int count = 0;
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null)  return 0;
        HashMap<Long, Integer> prefixSums = new HashMap<>();
        prefixSums.put(0L,1);
        dfs(root, 0L, prefixSums, (long) targetSum);
        return count;
    }

    private void dfs(TreeNode node, long prefixSum, HashMap<Long, Integer> prefixSums, long targetSum){
        long currentprefixSum = prefixSum+ (long) node.val;

        if (prefixSums.containsKey(currentprefixSum - targetSum)) count += prefixSums.get(currentprefixSum - targetSum);

        prefixSums.put(currentprefixSum,prefixSums.getOrDefault(currentprefixSum,0) +1);

        if (node.left != null) dfs(node.left, currentprefixSum, prefixSums, targetSum);
        if (node.right != null) dfs(node.right, currentprefixSum, prefixSums, targetSum);

        prefixSums.put(currentprefixSum,prefixSums.get(currentprefixSum) -1);

    }
}