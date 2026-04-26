/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    HashMap<Integer, Integer> parents;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        parents = new HashMap<>();

        dfs(root, root.val);

        HashSet<Integer> pancestors = new HashSet<>();
        HashSet<Integer> qancestors = new HashSet<>();
        int pparent = p.val;
        int qparent = q.val;
        pancestors.add(pparent);
        qancestors.add(qparent);

        while (true){
            pparent = parents.get(pparent);
            qparent = parents.get(qparent);

            if (qancestors.contains(pparent)) return new TreeNode(pparent);
            
            pancestors.add(pparent);

            if (pancestors.contains(qparent)) return new TreeNode(qparent);
            
            qancestors.add(qparent);
        }

        
    }


    private void dfs(TreeNode node, int parent){
        parents.put(node.val, parent);

        if (node.left != null) dfs(node.left, node.val);
        if (node.right != null) dfs(node.right, node.val);
    }
}