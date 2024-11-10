class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there are no edges
        if not edges:
            # If there's more than one node but no edges, it can't be a connected tree
            if n > 1:
                return False
            else:
                return True  # A single node without edges is a valid tree

        # Initialize an adjacency list to represent the graph structure
        treedict = collections.defaultdict(list)
        
        # Dictionary to store each node's parent during traversal to detect cycles
        parentdict = {}
        
        # Set to keep track of visited nodes
        seen = set()

        # Build the adjacency list from the edges
        for num1, num2 in edges:
            treedict[num1].append(num2)
            treedict[num2].append(num1)
        
        # Find the node with the maximum number of neighbors to start the traversal
        maxlength = max([len(v) for k, v in treedict.items()])
        current = [k for k, v in treedict.items() if len(v) == maxlength]

        # If every node has only one neighbor, but there are more than two nodes, it can't be a tree
        if n > 2 and len(current) == n:
            return False

        # Perform BFS to explore all nodes in the graph, starting from the first node with max neighbors
        current = [current[0]]
        while current:
            nxtlevel = []  # List to store nodes for the next level of traversal
            for parent in current:
                seen.add(parent)  # Mark the current node as visited
                # Traverse all adjacent nodes (children)
                for child in treedict[parent]:
                    # If the child has already been visited, check for cycle
                    if child in seen:
                        # If the child is not the parent of the current node, a cycle exists
                        if parentdict[parent] != child:
                            return False
                    else:
                        # Mark the parent of the child and prepare it for the next level traversal
                        parentdict[child] = parent
                        nxtlevel.append(child)  # Add the child to the next level
            current = nxtlevel  # Move to the next level of nodes
        
        # Check if all nodes were visited (connected) and no cycle was found
        return len(seen) == n


        