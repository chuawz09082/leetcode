/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        // Base case: if the root is null or it’s a leaf node, simply return the root
        if (root == null || (root.left == null && root.right == null)) {
            return root;
        }

        // Initialize a stack to store nodes at the current level, starting with the root
        Stack<Node> stack = new Stack<>();
        stack.add(root);
        
        // `current` is used to link nodes horizontally at each level
        Node current = root;
        
        // `nodeleft` tracks the leftmost node at each level, used for moving down to the next level
        Node nodeleft = current.left;

        // Outer loop to process each level until all nodes are connected
        while (!stack.isEmpty()) {
            // Stack to hold nodes for the next level
            Stack<Node> nextlevel = new Stack<>();
            
            // Loop through each node in the current level
            for (Node node : stack) {
                // If the node has children, add them to the `nextlevel` stack
                if (node.left != null) {
                    nextlevel.add(node.left);
                    nextlevel.add(node.right);
                }
            }

            // Connect each node in the current level stack to its next node
            for (int i = 1; i < stack.size(); i++) {
                current.next = stack.get(i);  // Link current node to the next node in the level
                current = current.next;       // Move `current` to the next node
            }

            // Reset `current` to the leftmost node of the next level
            current = nodeleft;

            // Move `nodeleft` to the leftmost child of the next level, if it exists
            if (nodeleft.left != null) {
                nodeleft = nodeleft.left;
            }

            // Set `stack` to `nextlevel` to process the next level in the next iteration
            stack = nextlevel;
        }

        // Return the modified tree with `next` pointers connected
        return root;
    }
}